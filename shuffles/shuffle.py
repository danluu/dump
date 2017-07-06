import random

# Going to range(len(a)) means that we pointlessly swap the last element with itself!
def shuffle(a):    
    for i in range(len(a) - 1):
        j = random.randint(i, len(a) - 1)
        a[i], a[j] = a[j], a[i]
    return a

def sattolo(a):    
    for i in range(len(a) - 1):
        j = random.randint(i+1, len(a) - 1)
        a[i], a[j] = a[j], a[i]
    return a

def is_derangement(a):
    return True

def derangement(n):
    a = list(range(n))
    while not is_derangement(a):
        a = shuffle(a)
    return a

def check_uniformity(fn):
    length = 5
    bins = [[0 for junk0 in range(length)] for junk1 in range (length)]
    for i in range(1000):
        result = fn(list(range(0,length)))
        for j in range(len(result)):
            new_idx = result[j]
            bins[j][new_idx] += 1
    return bins

def walk_cycle(a):
    seen = set()
    node = 0
    while not node in seen:
        seen.add(node)
        node = a[node]
    return len(seen)
        

def verify_cycle():
    for length in range(3, 40):
        for i in range(1000):
            result = sattolo(list(range(0,length)))
            assert(walk_cycle(result) == length)
        

# print(check_uniformity(shuffle))
# print(check_uniformity(sattolo))

verify_cycle()
