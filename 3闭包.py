
def outer():  # 外层函数
    b = '_' * 50
    def inner():  # 内层函数
        #内层函数中用到了外层函数的变量
        print(b)
    # 外函数的返回值是内函数的引用
    return inner

fuction = outer()
fuction()

def outer(a):  # 外层函数
    def inner():  # 内层函数
        #内层函数中用到了外层函数的变量
        print(a)
    # 外函数的返回值是内函数的引用
    return inner

fuction = outer("闭包确实有点绕！")
fuction()
