

# # 闭包+函数形参fc+inner中调用fc()
# def mkHumanInital(fc):
#     def inner():
#         print('显示创建人物前的画面。')
#         fc()
#         print('显示创建人物后的画面。')
#     return inner
#
# # 功能函数
# def mkHuman():
#     import random
#     nameList = ['张三', '李四', '王五', '赵六']
#     ageList = [i+1 for i in range(60)]
#     name = random.choice(nameList)
#     age = random.choice(ageList)
#     print('创建了3D人物，姓名：%s，年龄：%d。' % (name, age))
#
# # 调用闭包函数，将需要装饰的函数mkHuman作为参数传入
# # 返回的函数用需要装饰的函数名接收
# mkHuman = mkHumanInital(mkHuman)
#
# # 业务代码
# mkHuman()
# mkHuman()
# 闭包+函数形参fc+inner中调用fc()
def mkHumanInital(fc):
    def inner(*args, **kwargs):
        print('显示创建人物前的画面。')
        fc(*args, **kwargs)
    return inner

@mkHumanInital
def mkHuman(ht=1.8, wt=180):
    import random
    nameList = ['张三', '李四', '王五', '赵六']
    ageList = [i+1 for i in range(60)]
    name = random.choice(nameList)
    age = random.choice(ageList)
    print('创建了3D人物，姓名：%s，年龄：%d。' % (name, age))
    print('姓名：%s的身高是：%.2fdm,体重：%dkg。' % (name, ht, wt))

# 业务代码
mkHuman(1.6, wt=150)
mkHuman()


