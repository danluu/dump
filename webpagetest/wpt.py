import requests
import time

# connections = ['FIOS', 'Cable', '3G', 'Dial']
connections = ['FIOS', 'Dial']

key = ''
with open('key.txt') as f:
    key = f.readline().rstrip()

payload = {'url': 'http://danluu.com/',
           'k':key,
           'f':'json',  # return json results.
           'noheaders':'1',  # don't save headers
           'fvonly':'1',  # first view only
           'noopt':'1'  # disable optimization checks???
}

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
        print("Polling attempt {}".format(num_attempts))
        req_result = requests.get(json_url)
        num_attempts += 1
        if req_result.status_code == 200 or num_attempts > 100:
            result = req_result.json()
            print(req_result.json())
            if result['statusCode'] == 200:
                break
        time.sleep(5)

    result = req_result.json()
    return result

def print_results(result, connection):
    successful_runs = result['data']['successfulFVRuns']
    bytes_in = result['data']['average']['firstView']['bytesIn']
    num_reqs = result['data']['average']['firstView']['requests']
    tt_complete = result['data']['average']['firstView']['visualComplete']

    print("successful_runs: {}".format(successful_runs))
    print("num_reqs: {}".format(num_reqs))
    print("tt_complete: {}".format(tt_complete))


for cc in connections:
    payload['location'] = "Dulles.{}".format(cc)
    json_url = send_test_request(payload)
    # json_url = 'http://www.webpagetest.org/jsonResult.php?test=170127_BG_CF'
    
    result = poll_test_result(json_url)
    print_results(result, cc)
