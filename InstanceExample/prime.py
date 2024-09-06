import math

def CountPrimes(n1, n2):
    num = 0
    for x in range(n1, n2):
        flag = 1
        for i in range(2, int(math.sqrt(x+1)+1)):
            if x%i== 0:
                flag = 0
                break
        if flag == 1:
            print(x, end=" ")
            num += 1
    return num

num = CountPrimes(2, 200)
print("\nall nums: ", num)

    