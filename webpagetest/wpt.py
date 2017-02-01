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
urls = ['https://danluu.com',
        'http://danluu.com',
        'https://jvns.ca',
        'http://jvns.ca',
        'https://www.joelonsoftware.com',
#        'https://steve-yegge.blogspot.com',
#        'https://fgiesen.wordpress.com',
        'https://google.com',
        'https://bing.com',
        'https://amazon.com',
        'https://blog.codinghorror.com',
        'https://news.ycombinator.com/',
        'https://www.reddit.com/']
# TODO: add https://signalvnoise.com
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
        bytes_in_max = 0
        requests_max = 0
        connections_max = 0
        for run in range(1, num_runs+1):
            # print(result['data']['runs'][str(run)]['firstView'])
            if 'visualComplete' in runs[str(run)]['firstView']:
                complete_times.append(float(runs[str(run)]['firstView']['visualComplete'])/1000)
            else:
                complete_times.append(float('inf'))

            # TODO: reported sizes seem to be wrong for large sites. Need to figure out why.
            if 'bytesIn' in runs[str(run)]['firstView']:
                bytes_in = runs[str(run)]['firstView']['bytesIn']
                if bytes_in_max < bytes_in:
                    bytes_in_max = bytes_in

            # TODO: this number may be wrong due to flakiness or something?
            # TODO: need to fail test based on not enough requests/connections?
            if 'requestsFull' in runs[str(run)]['firstView']:
                requests = runs[str(run)]['firstView']['requestsFull']
                if requests_max < requests:
                    requests_max = requests

            if 'connections' in runs[str(run)]['firstView']:
                connections = runs[str(run)]['firstView']['connections']
                if connections_max < connections:
                    connections_max = connections

        complete_times.sort()
        per_conn[url][connection] = complete_times

        per_url[url]['bytesIn'] = bytes_in_max
        per_url[url]['requests'] = requests_max
        per_url[url]['connections'] = connections_max

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
    header = ['url','size','reqs','conns'] + connections
    writer.writerow(header)
    for uu in urls:
        current_row = [uu,
                       per_url[uu]['bytesIn'],
                       per_url[uu]['requests'],
                       per_url[uu]['connections']]
        for cc in connections:
            current_row.append(per_conn[uu][cc][idx])
        writer.writerow(current_row)

def display_float(x):
    if x < 1:
        return '%10.2f' % x
    elif x < 10:
        return '%10.1f' % x
    else:
        return '%10.0f' % x

# TODO: generate gradients from end points instead of using giant constants.
greens = ["#F7FCFD", "#F3F9F9", "#EFF6F5", "#EBF3F2", "#E7F0EE", "#E3EDEB", "#DFEAE7", "#DBE7E3", "#D7E4E0", "#D3E1DC", "#CFDED9", "#CBDBD5", "#C7D8D1", "#C4D6CE", "#C0D3CA", "#BCD0C7", "#B8CDC3", "#B4CAC0", "#B0C7BC", "#ACC4B8", "#A8C1B5", "#A4BEB1", "#A0BBAE", "#9CB8AA", "#98B5A6", "#94B2A3", "#91B09F", "#8DAD9C", "#89AA98", "#85A794", "#81A491", "#7DA18D", "#799E8A", "#759B86", "#719883", "#6D957F", "#69927B", "#658F78", "#628D74", "#5E8A71", "#5A876D", "#568469", "#528166", "#4E7E62", "#4A7B5F", "#46785B", "#427557", "#3E7254", "#3A6F50", "#366C4D", "#326949", "#2F6746", "#2B6442", "#27613E", "#235E3B", "#1F5B37", "#1B5834", "#175530", "#13522C", "#0F4F29", "#0B4C25", "#074922", "#03461E", "#00441B"]
greens.reverse()
reds = ["#FFF7EC", "#FCF3E8", "#FAEFE4", "#F8EBE0", "#F6E7DD", "#F4E3D9", "#F2DFD5", "#F0DBD1", "#EED7CE", "#ECD3CA", "#EACFC6", "#E8CBC2", "#E6C7BF", "#E4C4BB", "#E2C0B7", "#E0BCB3", "#DEB8B0", "#DCB4AC", "#DAB0A8", "#D8ACA4", "#D6A8A1", "#D4A49D", "#D2A099", "#D09C95", "#CE9892", "#CC948E", "#CA918A", "#C88D86", "#C68983", "#C4857F", "#C2817B", "#C07D77", "#BD7974", "#BB7570", "#B9716C", "#B76D68", "#B56965", "#B36561", "#B1625D", "#AF5E59", "#AD5A56", "#AB5652", "#A9524E", "#A74E4A", "#A54A47", "#A34643", "#A1423F", "#9F3E3B", "#9D3A38", "#9B3634", "#993230", "#972F2C", "#952B29", "#932725", "#912321", "#8F1F1D", "#8D1B1A", "#8B1716", "#891312", "#870F0E", "#850B0B", "#830707", "#810303", "#7F0000"]

def gradient(colors, low, high, value):
    max_idx = len(colors) - 1
    bucket_size = (high - low) / max_idx
    bucket = int((value - low) / bucket_size)
    return colors[bucket]

def pandas_style(val):
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


def csv_to_html():
    print("Converting csv to HTML")
    df = pandas.read_csv('/tmp/wpt_table_50.csv')

    print(df)
    
    # df.to_html doesn't save style info, so we use this hack instead.
    # Not using background_gradient because it has data-dependent bugs that sometimes cause nonsensical gradients.
    html = (
        df.style
        .applymap(pandas_style,
                  subset=pandas.IndexSlice[:,connections])
        .render()
        )

    with open('/tmp/wpt.html', 'w') as out:
        out.write(html)

# save_json_urls(payload, urls, connections)
# get_test_results()
# make_csv_table('/tmp/wpt_table_50.csv', 4)
# make_csv_table('/tmp/wpt_table_90.csv', 8)
# csv_to_html()
