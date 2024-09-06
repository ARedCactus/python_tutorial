if __name__ == '__main__':
    a = 1
    eval('print(a)')
    namespace = {'a': 1, 'b': 2}
    result = eval('a + b', namespace)
    print(result)