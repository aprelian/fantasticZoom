'''增删改
数据存放位置：
 show variables like '%dir%';
C:\ProgramData\MySQL\MySQL Server 5.5\data
'''
import pymysql

# 创建连接
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='zzz', db='library')
# 创建游标
cursor = conn.cursor()

# 执行SQL，并返回收影响行数
effect_row = cursor.execute("update book set name = '1zz2'")

# 执行SQL，并返回受影响行数
# effect_row = cursor.execute("update hosts set host = '1.1.1.2' where nid > %s", (1,))

# 执行SQL，并返回受影响行数
# effect_row = cursor.executemany("insert into hosts(host,color_id)values(%s,%s)", [("1.1.1.11",1),("1.1.1.11",2)])


#执行sql语句
# sql='select * from user where username="%s" and password="%s"' %(user,pwd) #注意%s需要加引号，就是一条基本的sql语句,事先要在user表中插入数据，这样查询才会有结果
sql='SELECT * FROM book;' #注意%s需要加引号，就是一条基本的sql语句,事先要在user表中插入数据，这样查询才会有结果
print(sql)
res=cursor.execute(sql) #执行sql语句，返回sql查询成功的记录数目,我只在表中插入一条记录，查询成功最多所以也就一条记录数
print(res)

'''part2'''
# sql='insert into user (username,oassword) values (%s,%s)'
# res=cursor.execute(sql,("xingxing","123"))                  #执行sql语句，返回sql成功插入的记录数
# print(res)

'''part3 插入'''
sq_='insert into book(name,data) values(%s,%s);'
res=cursor.executemany(sq_,[("xingxing","111"),("yueliang","222"),("taiyang","333")]) #可以同时插入多行记录，执行sql语句，返回sql影响成功的行数
print(res)

'''part4 修改'''
# sql='update user set username=%s , password = %s where id=%s'
# res=cursor.execute(sql,['love','1314',5]) #执行sql语句，返回sql影响成功的行数,修改记录中id=5，将用户名该为love,密码改为1314
# print(res)               #成功修改一条记录内容

'''part5 删除'''
# sql= 'delete from user where id = %s'
# res=cursor.execute(sql,2)               #删除指定的某一条记录，删除第二掉记录
# print(res)

# 提交，不然无法保存新建或者修改的数据
conn.commit()

# 关闭游标
cursor.close()
# 关闭连接
conn.close()
