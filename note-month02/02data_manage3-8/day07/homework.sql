查看MySQL状态 : sudo  service  mysql  status  （按q退出查看）
启动/停止/重启服务：sudo  service  mysql    start/stop/restart
连接数据库mysql -u -p        mysql -u root -p
查看已有库
show databases;

创建库
create database books character set utf8;
查看当前所在库
select database();
切换库
use books;
创建表
create table book(id int primary key auto_increment,
bookname varchar (50)not null,
price decimal (5,2),
remark text comment "备注信息",
pid int not null,
wid int not null,
foreign key (pid) references publish(id),
foreign key (wid) references writer(id)
);
create table publish(id int primary key auto_increment,
publishname varchar (50)not null
);
create table writer(id int primary key auto_increment,
writername varchar(30) not null
);
==查看表
show tables;
==查看表结构
desc book;

insert into publish (publishname)
values
("作家出版社"),
("科学技术出版社"),
("北京十月文艺出版社"),
("人民文学出版社");
insert into writer (writername)
values
('路遥'),
('霍金'),
('钱钟书'),
('村上春树'),
('塞林格'),
('余华');
insert into book (bookname,wid,pid,price,remark)
values ('《平凡的世界》',1,1,88,"青年励志"),
('《果壳中的宇宙》',2,2,50,"探索宇宙"),
('《旧文四篇》',3,1,40,"中国史"),
('《挪威的森林》',4,3,70,"恋爱小说"),
('《时间简史》',2,4,60,"探索宇宙"),
('《且听风吟》',4,4,50,"经典小说"),
('《海边的卡夫卡》',4,1,80,"经典小说"),
('《麦田里的守望者》',5,2,100,"现代经典小说"),
('《石语》',3,4,55,"中国史"),
('《围城》',3,4,40,"讽刺小说"),
('《活着》',6,1,45,"友情"),
('《鲜血梅花》',6,4,56,"民族故事");
+----+-----------------------------+--------+--------------------+-----+-----+
| id | bookname                    | price  | remark             | pid | wid |
+----+-----------------------------+--------+--------------------+-----+-----+
|  1 | 《平凡的世界》              |  88.00 | 青年励志           |   1 |   1 |
|  2 | 《果壳中的宇宙》            |  50.00 | 探索宇宙           |   2 |   2 |
|  3 | 《旧文四篇》                |  40.00 | 中国史             |   1 |   3 |
|  4 | 《挪威的森林》              |  70.00 | 恋爱小说           |   3 |   4 |
|  5 | 《时间简史》                |  60.00 | 探索宇宙           |   4 |   2 |
|  6 | 《且听风吟》                |  50.00 | 经典小说           |   4 |   4 |
|  7 | 《海边的卡夫卡》            |  80.00 | 经典小说           |   1 |   4 |
|  8 | 《麦田里的守望者》          | 100.00 | 现代经典小说       |   2 |   5 |
|  9 | 《石语》                    |  55.00 | 中国史             |   4 |   3 |
| 10 | 《围城》                    |  40.00 | 讽刺小说           |   4 |   3 |
| 11 | 《活着》                    |  45.00 | 友情               |   1 |   6 |
| 12 | 《鲜血梅花》                |  56.00 | 民族故事           |   4 |   6 |
+----+-----------------------------+--------+--------------------+-----+-----+
