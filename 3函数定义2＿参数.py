# 参数：在调用函数时，向函数提供数据
# 无参数
def line1():
    print('___________')
line1()

# 使用参数
def line2(width):
    print('_' * width)
line2(20)

# 使用多个参数
def line3(char1, width):
    print(char1 * width)
line3(chr(9787), 30)

def line4():
    pass
line4()
