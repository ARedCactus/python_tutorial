# 求最大公约数 
def GetMaxPrime(a, b):
    return b if a%b==0 else GetMaxPrime(b, a%b)

def Factorization(num):
    arr = []
    if not isinstance(num, int) or num<=0:
        print("error num format")
        exit(0)
    elif num in [1]:
        arr.append(num)
        return arr
    while num not in [1]:
        for x in range(2, num+1):
            if num % x == 0:
                num //= x
                arr.append(x)
                break
    return arr

arr = Factorization(100)
print(arr)

