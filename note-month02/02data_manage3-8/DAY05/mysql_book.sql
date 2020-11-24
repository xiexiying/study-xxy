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
create table book(id int primary key auto_increment,name varchar (50)not null,
writer varchar(30) not null,publishing_house varchar (50) ,
price decimal (5,2),remark text comment "备注信息" );
==查看表
show tables;
==查看表结构
desc book;
 +------------------+--------------+------+-----+---------+----------------+
| Field            | Type         | Null | Key | Default | Extra          |
+------------------+--------------+------+-----+---------+----------------+
| id               | int(11)      | NO   | PRI | NULL    | auto_increment |
| name             | varchar(50)  | NO   |     | NULL    |                |
| writer           | varchar(30)  | NO   |     | NULL    |                |
| publishing_house | varchar(50)  | YES  |     | NULL    |                |
| price            | decimal(5,2) | YES  |     | NULL    |                |
| remark           | text         | YES  |     | NULL    |                |
+------------------+--------------+------+-----+---------+----------------+

--插入数据
insert into book (name,writer,publishing_house,price,remark)
values ('《平凡的世界》','路遥',"作家出版社",88,"青年励志"),
('《果壳中的宇宙》','霍金',"湖南科学技术出版社",50,"探索宇宙"),
('《穆斯林的葬礼》','霍达',"作家出版社",40,"爱情悲剧"),
('《挪威的森林》','村上春树',"北京十月文艺出版社",70,"恋爱小说"),
('《基督山伯爵》','大仲马',"人民文学出版社",60,"浪漫传奇"),
('《教父》','马里奥·普佐',"花城出版社",50,"黑帮故事"),
('《苏菲的世界》','乔斯坦·贾德',"作家出版社",80,"哲学史"),
('《麦田里的守望者》','塞林格',"译林出版社",100,"现代经典小说"),
('《万历十五年》','黄仁宇',"三联书店出版社",55,"中国史"),
('《围城》','钱钟书',"上海晨光出版社",40,"讽刺小说"),
('《活着》','余华',"作家出版社",45,"友情"),
('《尘埃落定》','阿来',"人民文学出版社",56,"民族故事");
select * from book;
+----+-----------------------------+-------------------+-----------------------------+--------+--------------------+
| id | name                        | writer            | publishing_house            | price  | remark             |
+----+-----------------------------+-------------------+-----------------------------+--------+--------------------+
|  1 | 《平凡的世界》              | 路遥              | 作家出版社                  |  88.00 | 青年励志           |
|  2 | 《果壳中的宇宙》            | 霍金              | 湖南科学技术出版社          |  50.00 | 探索宇宙           |
|  3 | 《穆斯林的葬礼》            | 霍达              | 作家出版社                  |  40.00 | 爱情悲剧           |
|  4 | 《挪威的森林》              | 村上春树          | 北京十月文艺出版社          |  70.00 | 恋爱小说           |
|  5 | 《基督山伯爵》              | 大仲马            | 人民文学出版社              |  60.00 | 浪漫传奇           |
|  6 | 《教父》                    | 马里奥·普佐       | 花城出版社                  |  50.00 | 黑帮故事           |
|  7 | 《苏菲的世界》              | 乔斯坦·贾德       | 作家出版社                  |  80.00 | 哲学史             |
|  8 | 《麦田里的守望者》          | 塞林格            | 译林出版社                  | 100.00 | 现代经典小说       |
|  9 | 《万历十五年》              | 黄仁宇            | 三联书店出版社              |  55.00 | 中国史             |
| 10 | 《围城》                    | 钱钟书            | 上海晨光出版社              |  40.00 | 讽刺小说           |
| 11 | 《活着》                    | 余华              | 作家出版社                  |  45.00 | 友情               |
| 12 | 《尘埃落定》                | 阿来              | 人民文学出版社              |  56.00 | 民族故事           |
+----+-----------------------------+-------------------+-----------------------------+--------+--------------------+
1. 统计每位作家出版图书的平均价格
select writer,avg(price) from book group by writer;
2. 统计每个出版社出版图书数量
select publishing_house,count(publishing_house) from book group by publishing_house;
select publishing_house,count(*) from book group by publishing_house;
3. 查看总共有多少个出版社
select count(distinct publishing_house) from book ;
4. 筛选出那些出版过超过50元图书的出版社，并按照其出版图书的平均价格降序排序
select publishing_house,avg (price) from book group  by publishing_house
having max(price)>50 order by avg (price) desc;

5. 统计同一时间出版图书的最高价格和最低价格
select press_date,max(price),min(price) from book group by press_date;