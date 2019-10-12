class Pets:
    pass
    def say(self):
        print('宠物叫。')
class cat(Pets):
    def __init__(self, name):
        Pets.__init__(self)
        self.name = name
    def say(self):
        print('%s喵喵叫。' % self.name)
class dog(Pets):
    def __init__(self, name):
        Pets.__init__(self)
        self.name = name
    def say(self):
        print('%s汪汪叫。' % self.name)

p1 = Pets()
p2 = cat('小花猫')
p3 = dog('二哈')

p1.say()
p2.say()
p3.say()
