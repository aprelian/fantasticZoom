class Person:
    pass

p = Person()
# 给实例对象增加属性
p.age = 18
p.hight = 180
p.sex = "男"
p.pets = ["小猫", "二哈"]
print(p.age)
p.pets.append("小灰灰")
# 查看实例对象的所有属性
print(p.__dict__)
# 访问实例对象的属性
print(p.sex)
print(id(p.pets))
# 删除实例对象属性
del p.age
print(p.__dict__)
