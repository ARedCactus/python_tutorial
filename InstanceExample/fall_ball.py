def FallBall(height, num):
    arr = [height]
    for x in range(num):
        height /= 2
        arr.append(height)
    print(arr)
    return (sum(2*arr[1:-2], arr[0]), arr[-1])

value = FallBall(100.0, 10)
print(value)