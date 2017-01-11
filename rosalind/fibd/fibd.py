# def fibd(nn, mm):
#     # generation
#     gen = [0] * (nn)
#     gen[0] = 1
#     gen[1] = 1
#     print("1:1")
#     print("2:1")
#     for i in range(2,nn):
#         gen[i] = gen[i-1] + gen[i-2]
#         # print("add ",gen[i-1],gen[i-2])
#         if i >= mm:
#             print("sub", gen[i-mm])
#             gen[i] -= gen[i-mm]
#         print("{}:{}".format(i+1,gen[i]))
#     print(gen)
#     return gen[i]

def step(age):
    temp = sum(age[1:])
    for j in range(len(age)-1, 0, -1):
        age[j] = age[j-1]
    age[0] = temp
    return age

def fibd(nn, mm):
    age = [0] * (mm)
    age[0] = 1
    print(age)
    for i in range(1, nn):
        step(age)
        print(age)
    return sum(age)

age = [1,0,0]
assert step(age) == [0, 1, 0]
assert fibd(6, 3) == 4
assert fibd(95, 16) == 31420276473714305295
