import os
path = "D:\MyPyProject"
def listAllFilesName(path):
    '''
    这是一个自定义函数,可实现递归遍历目录下所有文件
    :param path: 需要的参数是文件夹的完整路径
    :return: None，没有返回值
    '''
    路径下的所有文件 = []
    dir0 = os.listdir(path)
    for dir_i in dir0:
        possibleDir = os.path.join(path, dir_i)
        if os.path.isdir(possibleDir):
            listAllFilesName(possibleDir)
        else:
            # print(possibleDir)
            路径下的所有文件.append(possibleDir)
    return 路径下的所有文件


print(listAllFilesName(path))
# print(listAllFilesName.__doc__)  # 显示函数声明内容

# 上级目录中的所有文件
# allFilesInCurrentDir = [i for i in os.listdir('../') if not os.path.isdir(i)]
# allFilesInCurrentDir = [i for i in os.listdir('./') if not os.path.isdir(i)]
# print(allFilesInCurrentDir)
# print([i+'\b' for i in os.listdir('./') if not os.path.isdir(i)])