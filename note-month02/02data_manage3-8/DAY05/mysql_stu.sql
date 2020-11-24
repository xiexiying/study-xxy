create table hobby(id int primary key auto_increment,name varchar (30)not null,
hobby set("sing","dance","draw"))
#插入
insert into class values (1,'lucy','w',20,88),(2,'tom','m',20,78);
insert into class (name,sex,age,score) values ('lucy','w',20,88),('tom','m',20,78);

mysql> desc hobby;
+--------+----------------------------+------+-----+---------+----------------+
| Field  | Type                       | Null | Key | Default | Extra          |
+--------+----------------------------+------+-----+---------+----------------+
| id     | int(11)                    | NO   | PRI | NULL    | auto_increment |
| name   | varchar(30)                | NO   |     | NULL    |                |
| hobby  | set('sing','draw','dance') | YES  |     | NULL    |                |
| level  | char(1)                    | YES  |     | NULL    |                |
| price  | decimal(7,0)               | YES  |     | NULL    |                |
| remark | text                       | YES  |     | NULL    |                |
+--------+----------------------------+------+-----+---------+----------------+

mysql> desc class;
+-------+---------------------+------+-----+---------+----------------+
| Field | Type                | Null | Key | Default | Extra          |
+-------+---------------------+------+-----+---------+----------------+
| id    | int(11)             | NO   | PRI | NULL    | auto_increment |
| name  | varchar(30)         | NO   |     | NULL    |                |
| sex   | enum('w','m','o')   | YES  |     | NULL    |                |
| age   | tinyint(3) unsigned | YES  |     | NULL    |                |
| score | float               | YES  |     | 0       |                |
+-------+---------------------+------+-----+---------+----------------+

insert into hobby (name,hobby,level,price,remark) values ('lucy','sing,dance',"A",20000,"有天分"),
('tom','dance',"A",10000,"舞蹈天才");
insert into hobby (name,hobby,level,price,remark) values ('jenny','draw',"B",10000,"just soso"),
('jim','dance',"A",15000,"舞蹈天才2");
insert into hobby (name,hobby,level,price) values ('tidy','draw',"A",10000),
('mary','dance',"C",15000);
mysql> select * from hobby;
+----+-------+------------+-------+-------+---------------+
| id | name  | hobby      | level | price | remark        |
+----+-------+------------+-------+-------+---------------+
|  1 | lucy  | sing,dance | A     | 20000 | 有天分        |
|  2 | tom   | dance      | A     | 10000 | 舞蹈天才      |
|  3 | jenny | draw       | B     | 10000 | just soso     |
|  4 | jim   | dance      | A     | 15000 | 舞蹈天才2     |
|  5 | tidy  | draw       | A     | 10000 | NULL          |
|  6 | mary  | dance      | C     | 15000 | NULL          |
+----+-------+------------+-------+-------+---------------+

mysql> select * from class;
+----+-------+------+------+-------+
| id | name  | sex  | age  | score |
+----+-------+------+------+-------+
|  1 | jenny | w    |   18 |    91 |
|  2 | tidy  | m    |   17 |    89 |
|  3 | mary  | w    |   19 |     0 |
|  4 | jim   | m    |   17 |     0 |
|  5 | lucy  | w    |   20 |    88 |
|  6 | tom   | m    |   20 |    78 |
+----+-------+------+------+-------+
+-------------------+-------------+------+-----+---------+----------------+
| Field             | Type        | Null | Key | Default | Extra          |
+-------------------+-------------+------+-----+---------+----------------+
| id                | int(11)     | NO   | PRI | NULL    | auto_increment |
| athlete           | varchar(32) | YES  |     | NULL    |                |
| birthday          | date        | YES  |     | NULL    |                |
| registration_time | datetime    | YES  |     | NULL    |                |
| performance       | time        | YES  |     | NULL    |                |
+-------------------+-------------+------+-----+---------+----------------+
5 rows in set (0.01 sec)
mysql> desc marathon;
+-------------------+-------------+------+-----+---------+----------------+
| Field             | Type        | Null | Key | Default | Extra          |
+-------------------+-------------+------+-----+---------+----------------+
| id                | int(11)     | NO   | PRI | NULL    | auto_increment |
| athlete           | varchar(32) | YES  |     | NULL    |                |
| birthday          | date        | YES  |     | NULL    |                |
| registration_time | datetime    | YES  |     | NULL    |                |
| performance       | time        | YES  |     | NULL    |                |
+-------------------+-------------+------+-----+---------+----------------+


mysql> insert into marathon (athlete,birthday,performance) values
("nnnn","1999-10-9","2:26:38");

alter table marathon modify registration_time datetime defult now();
+----+-----------+--------+---------+--------+---------+
| id | name      | gender | country | attack | defense |
+----+-----------+--------+---------+--------+---------+
|  1 | 曹操      | 男     | 魏      |    256 |      63 |
|  2 | 张辽      | 男     | 魏      |    328 |      69 |
|  3 | 甄姬      | 女     | 魏      |    168 |      34 |
|  4 | 夏侯渊    | 男     | 魏      |    366 |      83 |
|  5 | 刘备      | 男     | 蜀      |    220 |      59 |
|  6 | 诸葛亮    | 男     | 蜀      |    170 |      54 |
|  7 | 赵云      | 男     | 蜀      |    377 |      66 |
|  8 | 张飞      | 男     | 蜀      |    370 |      80 |
|  9 | 孙尚香    | 女     | 蜀      |    249 |      62 |
| 10 | 大乔      | 女     | 吴      |    190 |      44 |
| 11 | 小乔      | 女     | 吴      |    188 |      39 |
| 12 | 周瑜      | 男     | 吴      |    303 |      60 |
| 13 | 吕蒙      | 男     | 吴      |    330 |      71 |
+----+-----------+--------+---------+--------+---------+
查找所有蜀国人信息，按照攻击力排名
select * from sanguo where country ="蜀" order by attack;
将赵云攻击力设置为360，防御设置为70
update sanguo set attack=360,defense=70 where name ="赵云";
吴国英雄攻击力超过300的改为300，最多改2个
update  sanguo set attack=300 where country="吴" and attack>300 limit 2;
查找攻击力超过200的魏国英雄名字和攻击力并显示为姓名， 攻击力
select name as 姓名, attack as 攻击力 from sanguo where attack>200;
所有英雄按照攻击力降序排序，如果相同则按照防御生序排序
select * from sanguo order by attack ,defense;
查找名字为3字的
select name from sanguo where name like "___";
查找攻击力比魏国最高攻击力的人还要高的蜀国英雄
select * from sanguo where country ="蜀" and attack>
(select attack from sanguo where country ="魏" order by attack desc limit 1);

select * from (select * from sanguo where country ="蜀") as s where s. attack>
(select attack from sanguo where country ="魏" order by attack desc limit 1);
找到魏国防御力排名2-3名的英雄
select * from sanguo order by defense desc limit 2 offset 1;
查找所有女性角色中攻击力大于180的和男性中攻击力小于250的
select * from sanguo where gender="女" and attack >180 union
select * from sanguo where gender="男" and attack <250