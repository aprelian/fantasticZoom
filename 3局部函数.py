def mathFunc(str, num):
    name = 'mathFunc'
    def square(n):  # 计算平方
        nonlocal name
        name = 'math_func'
        return n * n
    def cube(n):  # 计算立方
        return n * n * n
    def factorial(n):  # 计算阶乘
        result = 1
        for index in range(2, n + 1):
            result *= index
        return result
    if str == "square":
        return name, square(num), name  # 调用
    elif str == "cube":
        return cube(num)
    else:
        return factorial(num)
print(mathFunc("cube", 3))
print(mathFunc("", 3))
print(mathFunc("square", 3))
