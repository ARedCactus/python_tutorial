def fun_1(n):
    a = [1, 2, 3]
    def add():
        a.append(n)
        return a
    return add

fun = fun_1(4)
print(fun())

n1 = 1    #全局变量不可修改
def fun_2():
    n1 = 2
    n1 += 1
    print("inside n1:", n1)

fun_2()
print("outside n1:", n1)

def func_3():
    global n1    #函数内添加 global 修饰 引用全局变量 n1
    n1 += 1

func_3()
print("global n1 outside:", n1)