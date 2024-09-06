#   python 3.0+ 除号变成  //

def water_flowwe(n1, n2):
    arr = []
    for x in range(n1, n2+1):
        a = x // 100
        b = x // 10 % 10
        c = x % 10
        if x == a*a*a + b*b*b + c*c*c:
            arr.append(x)
    return arr

arr_ = water_flowwe(100, 999)
print(arr_)