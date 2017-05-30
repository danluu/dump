import random

def quickselect(aa, k):
    if (len(aa) == 1):
        return aa[0]
    
    pivot = aa[random.randint(0,len(aa)-1)]

    lt = []
    eq = []
    gt = []

    for x in aa:
        if x < pivot:
            lt.append(x)
        elif x == pivot:
            eq.append(x)
        else:
            gt.append(x)

    # print(k)
    # print("{} | {} | {} | {}".format(pivot,lt,eq,gt))
    
    if k < len(lt):
        return quickselect(lt,k)
    elif k >= len(lt) + len(eq):
        return quickselect(gt,k - (len(lt) + len(eq)))
    else:
        return eq[0]
    

assert(quickselect([0,1,2,3,4,5],3) == 3)
assert(quickselect([5,4,3,2,1,0],3) == 3)
for i in range(0,10):
    l = [5,4,3,2,1,0]
    random.shuffle(l)
    assert(quickselect(l,3) == 3)

assert(quickselect([0,1,2,3,4,5],4) == 4)
    
