
class Person:
    planet = '地球'
    def __init__(self, name='x', age=1):
        self.name = name
        self.age = age
    def watchTV(self, content):
        print(content)

#单继承示例
class Student(Person):
    university = '武汉科技大学'
    def __init__(self,name,age,grade,specialty):
        #调用父类的构函
        Person.__init__(self, name, age)
        self.grade = grade
        self.specialty = specialty
    #覆写父类的方法
    def learn(self):
        print("%s,%d岁,在%s专业%s年级学习。"% \
              (self.name,self.age,self.specialty,self.grade))

stu1 = Student('Marion', 21, '三', 'GIS')
stu1.learn()
stu1.watchTV('watching TV.')
print(stu1.planet)

class Athletes:
    def __init__(self, sports='running', age=22):
        self.sports = sports
        self.age = age

class StuAth(Student, Athletes):
    def __init__(self, *args):
        Student.__init__(self, *args[0:4])
        Athletes.__init__(self, args[4], args[1])
    def __str__(self):
        return ('I am %s.' % (self.name))
    def beGoodAt(self):
        print("%s,%d岁,在%s专业%s年级学习,擅长%s。" % \
              (self.name, self.age, self.specialty,\
               self.grade, self.sports))
    def watchTV(self):  # 方法的重写
        print("%s is watching %s match." % (self.name, self.sports))
stu2 = StuAth('Tazan', 22, '四', 'GIS','gymnastics')
print(stu2)
stu2.beGoodAt()
stu2.learn()
stu2.watchTV()
