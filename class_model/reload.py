class Vec:
    def __init__(self, a = int, b = int) -> None:
        self.a_ = a
        self.b_ = b
    
    def __add__(self, input):
        return Vec(self.a_ + input.a_, self.b_ + input.b_)
    
if __name__ == '__main__':
    v1, v2 = Vec(1,2), Vec(3, 4)
    v3 = v1 + v2
    print(v3.a_, v3.b_)