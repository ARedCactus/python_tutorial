from math import sqrt

def WangShu(num):
    arr = []
    num_copy = num
    for x in range(1, num):
        if num%x == 0:
            arr.append(x)
    return sum(arr) == num_copy

for x in range(2, 1000):
    if WangShu(x) == True:
        print(x)
