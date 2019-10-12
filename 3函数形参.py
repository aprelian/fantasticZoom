def map(data, fn):  # fn--函数类型的形参
    result = []
    for e in data:
        result.append(fn(e))
    return result
def square(n):  # 计算平方
    return n * n
def cube(n):  # 计算立方
    return n * n * n
data = [1, 2, 3, 8, 9]
# 调用两次map()函数，每次调用传入不同函数
print("计算数组元素的平方")
print(map(data, square))
print("计算数组元素的立方")
print(map(data, cube))
