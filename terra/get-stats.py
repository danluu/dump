import json
import urllib.request
import time

# First month: http://terra.snellman.net/app/results/v2/2013/02
for year in range(2013, 2016):
    for month in range(1, 12):
        if year >= 2013 and month >= 2:
            urlpath = "http://terra.snellman.net/app/results/v2/{0}/{1}".format(year, month)
            filepath = "{0}.{1}.json".format(year, month)
            print(urlpath)
            urldata = urllib.request.urlopen(urlpath)
            jsondata = json.load(urldata)
            with open(filepath, 'w') as outfile:
                json.dump(jsondata, outfile)
            time.sleep(1)

            
            

# j = json.load(data)
# print j
# l = json.dumps(j)
# print l
