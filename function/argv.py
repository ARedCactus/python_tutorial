def func(argc, *argv):
    for x in argv:
        print(x, end=' ')
    return

if __name__ == '__main__':
    func(3, 'a', 'b', 'c')