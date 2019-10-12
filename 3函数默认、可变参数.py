
def stuMessage1(name, age, wt=60, ht=1.5):
    print('使用默认参数：')
    print('%s，%d岁，体重%dkg,身高%.2fm。' % (name,age,wt,ht))
stuMessage1('哪吒',15, 50)

def stuMessage2(name, age, wt=60, ht=1.5):
    print('使用关键字参数：')
    print('%s，%d岁，体重%dkg,身高%.2fm。' % (name,age,wt,ht))
stuMessage2(wt=200, ht=2.2, name='魔山',age=45)

def stuMessage3(name, age, wt, ht, *books, **scores):
    print('使用可变参数：')
    print('%s，%d岁，体重%dkg,身高%.2fm。' % (name,age,wt,ht))
    print('学习的课程有：', " ".join(books), end=".\n")
    print('books为元组类型：', books)
    print('scores为字典类型：', scores)
stuMessage3('小灰灰',9, 40, 1.5, "Python教程", 'GIS', 语文=89, 数学=99)


def test(name, message):
    print("用户: ", name)
    print("消息: ", message)


my_list = ['悟空', '来python课程取经吧。']
test(*my_list)
