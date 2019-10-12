def math_func(type):
    if type == 'square':
        return lambda n: n * n  # ①
    else:
        return lambda n: n * n * n  # ③
func1 = math_func("cube")
print(func1(5))  # 输出125
func2 = math_func("square")
print(func2(10))  # 输出100
