# 函数头def 函数名（参数列表）：
# 函数名：遵循变量的命名规则
# say_hi()  # 此句不能执行，必须先定义，后执行
# print('这是函数定义之前的代码')
def say_hi():
    # 函数体－实现函数功能
    print('hello,', end='')
    print('这是函数say_hi()执行时的代码')
# 函数外的其它代码
# print('这是函数定义之后的代码')
# 函数的调用,不调用不会执行
# say_hi()
# print('这是函数调用之后的代码')
def goodMorning():
    say_hi()  # 函数内部可调用函数
    print('Good morning everyone!')
goodMorning()
