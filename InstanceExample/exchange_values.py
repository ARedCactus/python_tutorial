def Exchange(a, b):
    a, b = b, a
    return (a, b)

if __name__ == '__main__':
    x = 100
    y = 200
    x, y = Exchange(x, y)
    print(x, y)