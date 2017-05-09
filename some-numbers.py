from datetime import datetime

base_rate = 174
extra = 204

def days_until():
    d1 = datetime.now()
    d2 = datetime.strptime("2017-07-16", "%Y-%m-%d")
    return abs((d2 - d1).days)

extra_rate = (365 / days_until()) * extra
print(extra_rate + base_rate)
