class E:
    def __init__(self, a = int, b = int) -> None:
        self.__a = a
        self.__b = b
    
    def get_a(self):
        return self.__a
    
    def get_b(self):
        return self.__b

if __name__ == '__main__':
    e = E(1,2)
    print(e.get_a(), e.get_b())
    