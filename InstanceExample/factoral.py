def op(num):
    if not isinstance(num, int):
        print("error format")
        exit(-1)
    output, temp = 0, 1
    for x in range(1, num+1):
        temp *= x
        output += temp
    return output

for x in map(op, [20]):
    print(x)

        