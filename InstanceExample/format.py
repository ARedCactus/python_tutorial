str_1 = "A:{}  B:{}".format("hello", "world")
print(str_1)

# 可指定位置
str_2 = "A:{0} B:{1} C:{0}".format("hello", "world")
print(str_2)

# 可以传入对象
class instance(object):
    def __init__(self, value) -> None:
        self.value_ = value

num = instance(6)
print("A:{0.value_}".format(num))

# 格式化 数字
print("A:{:.2f}".format(3.1415926))