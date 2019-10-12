# class People:
#     planet = '地球'  #定义一个类属性
#     def run(self, name='xxx'):  # 定义run方法
#         self.name = name  # name是实例属性
#         print('%s在%s上跑。' % (self.name, self.planet))
#
# p1 = People()  # 实例化p1
# p1.run('阿牛')  # 通过p1调用run方法，传入参数
# print(p1.name, p1.planet)
#
# p2 = People()
# p2.run('小王')
# print(p2.name, p2.planet)
#
# p3 = People()
# p3.name = 'qqq'
# p3.run()
# print(p3.name, p3.planet)


# class Person:
#     planet = '地球'
#
#     # python中的初始化方法
#     def __init__(self, name='x', age=1):
#         # 下面为Person对象增加2个实例属性
#         self.name = name
#         self.age = age
#         print('初始化时会自动运行。')
#
#     # 下面定义了一个实例方法
#     def watchTV(self, content):
#         print(content)
#
# p1 = Person('Alfago')
# print(p1.name, p1.age)
# p1.watchTV('看电视')

class Person:
    planet = '地球'
    def __init__(self, name='x', age=1):
        self.name = name
        self.age = age
    def watchTV(self, content):
        print(content)

p1 = Person('Alfago')
# 可通过实例对象访问实例属性与类属性
print(p1.name, p1.age, p1.planet)
# 可通过类访问类属性
print(Person.planet)
# 不能通过类访问实例属性，下面代码会报错
# print(Person.name)  # AttributeError:

