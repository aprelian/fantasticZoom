'''
安装mysql

在DOS命令窗口输入
mysql -h localhost -u root -p
回车 进入mysql数据库，其中-h表示服务器名，localhost表示本地；-u为数据库用户名，root是mysql默认用户名；-p为密码，如果设置了密码，可直接在-p后链接输入，如：-p123456，用户没有设置密码，显示Enter password时，直接回车即可。
注意，如果你的mysql没有安装在C盘下，你需要先使用DOS命令进入mysql的安装目录下的bin目录中。以我的电脑为例，方法如下：输入D:进入D盘，在输入cd D:\Tools\MySQL5.5.25\bin进入到mysql的bin目录下才可以输入 mysql -hlocalhost -uroot -p

输入show databases；显示你有的数据库（mysql数据库中的命令必须以分号结尾“；”）

如果要退出mysql数据库，输入exit;回车

--进入sql服务后首先查看有哪些数据库
show databases;

--若没有新建一个
CREATE DATABASE library;

--使用数据库
use library;


--查看有哪些表
show tables;

--新建表：CREATE TABLE xxxx();
--书：书名和作者
CREATE TABLE book(name char(20),author char(20));
--读者：人名、借书日期以及性别
CREATE TABLE reader(name char(20),date int(10),sex char(5));

--再次查看一下表

--查看表的内容：SELECT * FROM xxx;
SELECT * FROM book;
SELECT * FROM reader;

--插入内容到表：INSERT INTO xxx VALUES();
INSERT INTO book VALUES('c language','niuren')
INSERT INTO book VALUES('java','lihairen')
INSERT INTO book VALUES('python','yjj')

INSERT INTO reader VALUES('kumata'.20180530,'man');
INSERT INTO reader(name,sex) VALUES('kusada','man');
INSERT INTO reader(name,date) VALUES('wuyifan',20187475);

'''