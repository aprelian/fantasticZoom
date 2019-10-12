# class Pets:
#     def __init__(self, name,type):
#         self.name = name
#         self.type = type
#
#     def __str__(self,):
#         return ('I am %s,the %s.' % (self.name, self.type))
#
# pet1 = Pets('xiao_hei', 'dog')
# print(pet1)

class Books:
    def __init__(self, bookName):
        self.bookname = bookName
        self.lineIndex = 0
        with open(self.bookname, 'r') as book_:
            self.lines = book_.readlines()
        print(self.lines[0])
    def __iter__(self):
        return self
    def __next__(self):
        self.lineIndex += 1
        if self.lineIndex > 1000:
            print("-"*60)
            print('您的阅读权限？请加入会员再...')
            raise StopIteration
        return self.lines[self.lineIndex]

for line in Books('4红高粱.txt'):
    print(line)

# book = Books('4红高粱.txt')
# print(next(book))
# print(next(book))

