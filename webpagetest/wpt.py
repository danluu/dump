import csv
import json
import pandas
import requests
import time

# connections = ['FIOS', 'Cable', '3G', 'Dial']
connections = ['FIOS', 'Cable', 'Dial', 'Terrible']
urls = ['https://danluu.com',
        'http://danluu.com',
        'https://jvns.ca',
        'http://jvns.ca',
        'https://www.joelonsoftware.com',
        'https://blog.codinghorror.com']
num_runs = 2

key = ''
with open('key.txt') as f:
    key = f.readline().rstrip()

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
    req = requests.get('http://www.webpagetest.org/runtest.php', params=payload)
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
            payload['location'] = "Dulles.custom"
            payload['url'] = uu
            payload['bwDown'] = conn_props[cc]['bwDown']
            payload['bwUp'] = conn_props[cc]['bwUp']
            payload['latency'] = conn_props[cc]['latency']
            payload['plr'] = conn_props[cc]['plr']
            json_url = send_test_request(payload)
            if json_url.startswith('http'):
                json_url = 'https' + json_url[4:]
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
            per_conn[url][connection] = {}

        result = poll_test_result(wpt_json)

        if result['data']['successfulFVRuns'] != num_runs:
            failed = True
            per_conn[url][connection] = "X"
        else:
            bytesIn = result['data']['average']['firstView']['bytesIn']
            connections = result['data']['average']['firstView']['connections']
            requests = result['data']['average']['firstView']['requests']
            visualComplete = result['data']['average']['firstView']['visualComplete']

            # TODO: look at each run and pull out %-ile info.
            if 'bytesIn' in per_url[url]:
                if bytesIn < per_url[url]['bytesIn']:
                    failed = True
            else:
                per_url[url]['bytesIn'] = bytesIn

            per_url[url]['connections'] = connections

            if 'requests' in per_url[url]:
                if requests < per_url[url]['requests']:
                    failed = True
            else:
                per_url[url]['requests'] = requests

        if failed:
            per_conn[url][connection] = "X"
        else:
            per_conn[url][connection] = visualComplete


                    
    with open('/tmp/wpt_per_url.json','w') as jsonf:
        json.dump(per_url, jsonf)

    with open('/tmp/wpt_per_conn.json','w') as jsonf:
        json.dump(per_conn, jsonf)


def make_csv_table():
    print("Making csv table")
    per_url = {}
    with open('/tmp/wpt_per_url.json','r') as jsonf:
        per_url = json.load(jsonf)

    per_conn = {}
    with open('/tmp/wpt_per_conn.json','r') as jsonf:
        per_conn = json.load(jsonf)

    csvf = open('/tmp/wpt_table.csv', 'w', newline='')
    writer = csv.writer(csvf)
    header = ['url','size','reqs','conns'] + connections
    writer.writerow(header)
    for uu in urls:
        current_row = [uu,
                       per_url[uu]['bytesIn'],
                       per_url[uu]['requests'],
                       per_url[uu]['connections']]
        for cc in connections:
            current_row.append(per_conn[uu][cc])
        writer.writerow(current_row)

def csv_to_html():
    print("Converting csv to HTML")
    df = pandas.read_csv('/tmp/wpt_table.csv')
    print(df)
    df.to_html('/tmp/wpt.html',index=False)

# save_json_urls(payload, urls, connections)
# get_test_results()
# make_csv_table()
# csv_to_html()
    
    
