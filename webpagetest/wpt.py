import csv
import json
import pandas
import requests
import time

# connections = ['FIOS', 'Cable', '3G', 'Dial']
# connections = ['FIOS', 'Cable', 'Dial', 'Terrible']
connections = ['FIOS', 'Terrible']
# urls = ['https://danluu.com',
#         'http://danluu.com',
#         'https://jvns.ca',
#         'http://jvns.ca',
#         'https://www.joelonsoftware.com',
#         'https://blog.codinghorror.com']
urls = ['https://danluu.com',
        'http://danluu.com']
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
        connection_max = 0
        for run in range(1, num_runs+1):
            # print(result['data']['runs'][str(run)]['firstView'])
            if 'visualComplete' in runs[str(run)]['firstView']:
                complete_times.append(float(runs[str(run)]['firstView']['visualComplete']))
            else:
                complete_times.append(float('inf'))

            if 'bytesIn' in runs[str(run)]['firstView']:
                bytes_in = runs[str(run)]['firstView']['bytesIn']
                if bytes_in_max < bytes_in:
                    bytes_in_max = bytes_in

            # TODO: this number may be wrong due to flakiness or something?
            if 'requestsFull' in runs[str(run)]['firstView']:
                requests = runs[str(run)]['firstView']['requestsFull']
                if requests_max < requests:
                    requests_max = requests

            if 'connections' in runs[str(run)]['firstView']:
                connection = runs[str(run)]['firstView']['connections']
                if connection_max < connection:
                    connection_max = connection

        complete_times.sort()
        per_conn[url][connection] = complete_times
        per_url[url]['bytesIn'] = bytes_in_max
        per_url[url]['requests'] = requests_max
        per_url[url]['connections'] = connection_max
                    
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

def csv_to_html():
    print("Converting csv to HTML")
    df = pandas.read_csv('/tmp/wpt_table.csv')
    print(df)
    df.to_html('/tmp/wpt.html',index=False)

# save_json_urls(payload, urls, connections)
# get_test_results()
# make_csv_table('/tmp/wpt_table.csv', 4)
# csv_to_html()
    
    
