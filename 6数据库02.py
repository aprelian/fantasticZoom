'''查'''
import pymysql

# 创建连接
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='zzz', db='library')
# 创建游标
cursor = conn.cursor()

sql = 'SELECT * FROM book;' #注意%s需要加引号，就是一条基本的sql语句,事先要在user表中插入数据，这样查询才会有结果

res = cursor.execute(sql) #执行sql语句，返回sql查询成功的记录数目,我只在表中插入一条记录，查询成功最多所以也就一条记录数
cursor.scroll(3, mode='absolute')  # 相对绝对位置移动，第一个参数是相对绝对位置移动的记录条个数
# cursor.scroll(1,mode='relative') # 相对当前位置移动，第一个参数是相对当前位置移动的记录条个数

#通过fetchone、fetchmany、fetchall拿到查询结果
res1 = cursor.fetchone()              #以元组的形式，返回查询记录的结果，默认是从第一条记录开始查询
# res2=cursor.fetchone()            #会接着上一次的查询记录结果继续往下查询
# # res3=cursor.fetchone()
# res4=cursor.fetchmany(2)           #查询两条记录会以元组套小元组的形式进行展示
# # res5=cursor.fetchall()

#打印查询的最终结果到终端
print(res1)
# print(res2)
# print(res3)
# print(res4)
# print(res5)                         #会元组套小元组的形式将表中的左右记录头查询出来展示在终端
# print('%s行数据'%rows)

# 提交，不然无法保存新建或者修改的数据
conn.commit()

# 关闭游标
cursor.close()
# 关闭连接
conn.close()
