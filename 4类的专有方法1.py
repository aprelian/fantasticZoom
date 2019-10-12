'''
__ iter__

如果一个类想被用于for … in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。 比如
以斐波那契数列（Fibonacci sequence）为例，写一个Fib类，可以作用于for循环：

'''


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 200:
            raise StopIteration()
        return self.a


for n in Fib():
    print(n)

'''
__ getitem__

Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行,它不能像List那样按下标取出元素，要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：'''


class Fib2(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a


f = Fib2()
print('f[100]:', f[100])

'''
__getitem__()方法也可以实现list的切片操作，不过要加一个判断：'''


class Fib3(object):
    def __getitem__(self, n):
        if isinstance(n, int):  # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):  # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


f = Fib3()
print('f[5:20]:', f[5:20])
