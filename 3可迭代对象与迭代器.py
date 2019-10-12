# 可迭代对象：
# print(range(3))
# for i in range(3): print(i, end='')
# for i in 'abc': print(i, end='')
# for i in ['e', 'f', 'g']: print(i, end='')
# for i in {'i':10, 'j':20}: print(i,  end='')


iter1 = iter(range(3))
print(iter1.__next__())
print(next(iter1))
print(next(iter1))
# print(next(iter1)) 报错StopIteration