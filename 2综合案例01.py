# 100内3与5的倍数总和
print('方法一：', end=" ")
sum_ = 0
for i in range(1, 101):
    if (i % 3 == 0) or (i % 5 == 0):
        # print(i)
        sum_ = sum_ + i
print(sum_)

print('方法二：', end=" ")
print(sum([i for i in range(1, 101) if i % 3 == 0 or i % 5 == 0]))

print('方法三：', end=" ")
# print({*range(3, 101, 3)})
print(sum({*range(3, 101, 3), *range(5, 101, 5)}))

