def math_func(type):
    def square(n):  # 局部函数，计算平方
        return n * n
    def cube(n):  # 局部函数，计算立方
        return n ** 3
    # 返回局部函数
    if type == "square":
        return square
    else:
        return cube
# 调用get_math_func()，返回嵌套函数
func = math_func("cube")  # 得到cube函数
print(func(5))  # 输出125
print((math_func("square"))(10))  # 输出100

