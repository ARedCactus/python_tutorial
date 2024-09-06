class parent:
    x_ = 1

    def __init__(self, x = int) -> None:
        parent.x_ = x

    def get_x(self) -> int:
        return parent.x_
    
    def func_parent(void) -> None:
        pass

class child(parent):
    def __init__(self, x=int) -> None:
        super(child, self).__init__(x)

    def func_child(void) -> None:
        pass

if __name__ == '__main__':
    c = child(3)
    c.func_parent()
    c.func_child()
    c.get_x()