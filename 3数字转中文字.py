# num = 1243246675890
#
# ch = "零一二三四五六七八九"
# num_str = str(num)
# res = ""
#
# for i in num_str:
#     res += ch[int(i)]
# print(res)
def numToChinese1():
    num = input('请输入一个正整数：')
    myString = "零一二三四五六七八九"
    result = ""
    for i in num:
        result += myString[int(i)]
    return result
def numToChinese2():
    num = input('请输入一个正整数：')
    myString = "零一二三四五六七八九"
    result = ""
    for i in num:
        result += myString[int(i)]
    return num, result

print(numToChinese1())
print(numToChinese2())
