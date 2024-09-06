class E:
    def __init__(self, x):
        self.x_ = x

    def func_argv(argc, *argv):
        for x in argv:
            print(x, end=' ')
    
    def get__class__(obj):
        print(obj.__class__, end='')
        return ''
    
if __name__ == '__main__':
    e = E(2)
    print(e.x_)
    print(e.get__class__())