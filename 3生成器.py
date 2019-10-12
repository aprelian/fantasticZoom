def odd():
    n=1
    while True:
        yield n
        n+=2
odd_num = odd()
count = 0
for i in odd_num:
    if count >= 10:
        print("")
        break
    print(i, end="  ")
    count += 1

# odd_num = odd()
print(next(odd_num))
print(next(odd_num))
print(next(odd_num))
