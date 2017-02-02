import csv
import json
import math
import pandas
import requests
import time

# connections = ['FIOS', 'Cable', '3G', 'Dial']
connections = ['FIOS', 'Cable', 'LTE', '3G', '2G', 'Dial', 'Bad', 'Terrible']
# connections = ['FIOS', 'Terrible']
# TODO: change www.reddit.com to reddit.com
urls = ['http://bellard.org',
        'http://danluu.com',
        'https://news.ycombinator.com/',
        'https://danluu.com',
        'http://jvns.ca',
        'https://jvns.ca',
        'https://fgiesen.wordpress.com',
        'https://google.com',
        'https://www.joelonsoftware.com',
        'https://bing.com',
        'https://reddit.com/',
        'https://signalvnoise.com',
        'https://amazon.com',
        'https://steve-yegge.blogspot.com',
        'https://blog.codinghorror.com',
        'http://blog.regehr.org',
        'https://blog.regehr.org']
# urls = ['https://danluu.com',
#         'http://danluu.com']
num_runs = 10

key = ''
with open('key.txt') as f:
    key = f.readline().rstrip()

hostname = ''
with open('hostname.txt') as f:
    hostname = f.readline().rstrip()


payload = {'url': 'http://danluu.com/',
           'k':key,
           'f':'json',  # return json results.
           'noheaders':'1',  # don't save headers
           'fvonly':'1',  # first view only
           'runs':num_runs,
           'noopt':'1'  # disable optimization checks???
}

conn_props = {}
with open('connections.json','r') as jsonf:
    conn_props = json.load(jsonf)


def send_test_request(payload):    
    print('sending request')
    req = requests.get('http://{}/runtest.php'.format(hostname), params=payload)
    result = req.json()
    print(result)
    if result['statusText'] != 'Ok':
        print("send_test_request FAILED!!!!")
        raise Exception('test_request status not Ok')
    return result['data']['jsonUrl']

def poll_test_result(json_url):
    num_attempts = 0
    result = {}
    while True:
        print("{}: attempt {}".format(json_url, num_attempts))
        req_result = requests.get(json_url)
        num_attempts += 1
        if req_result.status_code == 200 or num_attempts > 100:
            result = req_result.json()
            # print(req_result.json())
            if result['statusCode'] == 200:
                break
        time.sleep(5)

    result = req_result.json()
    return result

def save_json_urls(payload, urls, connections):
    csvf = open('/tmp/wpt_urls.csv', 'w', newline='')
    writer = csv.writer(csvf)
    writer.writerow(['url','connection','wpt_json'])
    # TODO: swap loop ordering to avoid hammering a single URL ~100 times in a row.
    for uu in urls:
        for cc in connections:
            # payload['location'] = "Dulles.{}".format(cc)
            # payload['location'] = "Dulles.custom"
            payload['location'] = "micro_oregon_wptdriver.custom"
            payload['url'] = uu
            payload['bwDown'] = conn_props[cc]['bwDown']
            payload['bwUp'] = conn_props[cc]['bwUp']
            payload['latency'] = conn_props[cc]['latency']
            payload['plr'] = conn_props[cc]['plr']
            json_url = send_test_request(payload)
            # Don't have https set up on local server (yet?)
            # if json_url.startswith('http'):
            #     json_url = 'https' + json_url[4:]
            writer.writerow([uu, cc, json_url])
            print("{},{},{}".format(uu, cc, json_url))
        
            #result = poll_test_result(json_url)
            # print_results(result, cc)

def get_test_results():
    csvf_urls = open('/tmp/wpt_urls.csv')
    reader = csv.reader(csvf_urls)
    header = next(reader)
    assert header == ['url','connection','wpt_json']

    csvf_results = open('/tmp/wpt_results.csv', 'w', newline='')
    writer = csv.writer(csvf_results)

    per_conn = {}
    per_url = {}

    for row in reader:
        failed = False
        url = row[0]
        connection = row[1]
        wpt_json = row[2]

        if not url in per_url:
            per_url[url] = {}
            per_url[url]['bytesIn'] = 0
            # per_url[url]['requests'] = 0
            per_url[url]['connections'] = 0

        if not url in per_conn:
            per_conn[url] = {}

        if not connection in per_conn[url]:
            per_conn[url][connection] = []

        result = poll_test_result(wpt_json)

        # if result['data']['successfulFVRuns'] != num_runs:
        #     failed = True
        #     print("Failing {}:{} on sucessfulFVRuns".format(url, connection))
        #     per_conn[url][connection] = "X"
        runs = result['data']['runs']
        complete_times = []
        for run in range(1, num_runs+1):
            # print(result['data']['runs'][str(run)]['firstView'])
            if 'visualComplete' in runs[str(run)]['firstView']:
                complete_times.append(float(runs[str(run)]['firstView']['visualComplete'])/1000)
            else:
                complete_times.append(float('inf'))

            # TODO: reported sizes seem to be wrong for large sites. Need to figure out why.
            if 'bytesIn' in runs[str(run)]['firstView']:
                bytes_in = runs[str(run)]['firstView']['bytesIn']
                if per_url[url]['bytesIn'] < bytes_in:
                    per_url[url]['bytesIn'] = bytes_in

            # # TODO: this number may be wrong due to flakiness or something?
            # # TODO: need to fail test based on not enough requests/connections?
            # if 'requestsFull' in runs[str(run)]['firstView']:
            #     requests = runs[str(run)]['firstView']['requestsFull']
            #     if per_url[url]['requests'] < requests:
            #         per_url['requests'] = requests

            if 'connections' in runs[str(run)]['firstView']:
                connections = runs[str(run)]['firstView']['connections']
                if per_url[url]['connections'] < connections:
                    per_url[url]['connections'] = connections

        complete_times.sort()
        per_conn[url][connection] = complete_times

    # TODO: dump results periodically instead of at the end
    # Running a full set of tests can take a day and we shouldn't have to
    # attach a debugger to the process to inspect results before it's finished.
    with open('/tmp/wpt_per_url.json','w') as jsonf:
        json.dump(per_url, jsonf)

    with open('/tmp/wpt_per_conn.json','w') as jsonf:
        json.dump(per_conn, jsonf)

def make_csv_table(filename, idx):
    print("Making csv table")
    per_url = {}
    with open('/tmp/wpt_per_url.json','r') as jsonf:
        per_url = json.load(jsonf)

    per_conn = {}
    with open('/tmp/wpt_per_conn.json','r') as jsonf:
        per_conn = json.load(jsonf)

    csvf = open(filename, 'w', newline='')
    writer = csv.writer(csvf)
    header = ['url','size','cons'] + connections
    writer.writerow(header)
    for uu in urls:
        current_row = [uu,
                       per_url[uu]['bytesIn'],
                       # per_url[uu]['requests'],
                       per_url[uu]['connections']]
        for cc in connections:
            current_row.append(per_conn[uu][cc][idx])
        writer.writerow(current_row)

def float_style(x):
    if x < 1:
        return '%10.2f' % x
    elif x < 9.95:
        return '%10.1f' % x
    else:
        return '%10.0f' % x

def size_style(x):
    x = x / 1000000
    if x < 1:
        return '%10.2f' % x
    elif x < 10:
        return '%10.1f' % x
    else:
        return '%10.0f' % x

greens = ['#f7fcfd','#e5f5f9','#ccece6','#99d8c9','#66c2a4','#41ae76','#238b45','#006d2c','#00441b']
greens.reverse()
reds = ['#fff7ec','#fee8c8','#fdd49e','#fdbb84','#fc8d59','#ef6548','#d7301f','#b30000','#7f0000']

def gradient(colors, low, high, value):
    max_idx = len(colors) - 1
    bucket_size = (high - low) / max_idx
    bucket = int((value - low) / bucket_size)
    return colors[bucket]

def conn_bg_style(val):
    if val == float('inf'):
        color = reds[len(reds)-1]
        return 'background-color: {}'.format(color)
    elif val > 2:
        color = gradient(reds, math.log2(2.0), math.log2(360.0), math.log2(val))
        return 'background-color: {}'.format(color)
    elif val < 1:
        color = gradient(greens, 0.0, 1.0, val)
        return 'background-color: {}'.format(color)
    else:
        return 'background-color: white'

def conn_fg_style(val):
    if val == float('inf'):
        return 'color: white'
    else:
        return 'color: black'

def size_bg_style(val):
    if val > 1000000:
        color = gradient(reds, math.log2(1000000), math.log2(30000000), math.log2(val))
        return 'background-color: {}'.format(color)
    elif val < 500000:
        color = gradient(greens, 0.0, 500000, val)
        return 'background-color: {}'.format(color)
    else:
        return 'background-color: white'


def csv_to_html():
    print("Converting csv to HTML")
    df = pandas.read_csv('/tmp/wpt_table_50.csv')

    print(df)
    
    # df.to_html doesn't save style info, so we use this hack instead.
    # Not using background_gradient because it has data-dependent bugs that sometimes cause nonsensical gradients.
    html = (
        df.style
        .applymap(conn_bg_style,
                  subset=pandas.IndexSlice[:,connections])
        .applymap(conn_fg_style,
                  subset=pandas.IndexSlice[:,connections])
        .applymap(size_bg_style,
                  subset=pandas.IndexSlice[:,'size'])
        .format(float_style,
                subset=pandas.IndexSlice[:,connections])
        .format(size_style,
                subset=pandas.IndexSlice[:,'size'])
        .render()
        )

    with open('/tmp/wpt.html', 'w') as out:
        out.write(html)

# save_json_urls(payload, urls, connections)
# get_test_results()
# make_csv_table('/tmp/wpt_table_50.csv', 4)
# make_csv_table('/tmp/wpt_table_90.csv', 8)
# csv_to_html()
