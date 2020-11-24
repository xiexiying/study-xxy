create database stulast11 character set utf8;

create table class(cid int primary key auto_increment,
                  caption char(4) not null);
+-----+--------------+
| cid | caption      |
+-----+--------------+
|   1 | 三年二班     |
|   2 | 三年三班     |
|   3 | 三年一班     |
+-----+--------------+
create table teacher(tid int primary key auto_increment,
                    tname varchar(32) not null);
+-----+--------------+
| tid | tname        |
+-----+--------------+
|   1 | 波多老师     |
|   2 | 苍老师       |
|   3 | 小泽老师     |
+-----+--------------+
create table student(sid int primary key auto_increment,
                    sname varchar(32) not null,
                    gender enum('male','female','others') not null default 'male',
                    class_id int,
                    foreign key(class_id) references class(cid)
                    on update cascade
                    on delete cascade);
+-----+--------+--------+----------+
| sid | sname  | gender | class_id |
+-----+--------+--------+----------+
|   1 | 钢蛋   | female |        1 |
|   2 | 铁锤   | female |        1 |
|   3 | 山炮   | male   |        2 |
|   4 | 彪哥   | male   |        3 |
+-----+--------+--------+----------+
create table course(cid int primary key auto_increment,
                   cname varchar(16) not null,
                   teacher_id int,
                   foreign key(teacher_id) references teacher(tid)
                   on update cascade
                   on delete cascade);
+-----+--------+------------+
| cid | cname  | teacher_id |
+-----+--------+------------+
|   1 | 生物   |          1 |
|   2 | 体育   |          1 |
|   3 | 物理   |          2 |
+-----+--------+------------+
create table score(sid int primary key auto_increment,
                  student_id int,
                  course_id int,
                  number int(3) not null,
                  foreign key(student_id) references student(sid)
                   on update cascade
                   on delete cascade,
                   foreign key(course_id) references course(cid)
                   on update cascade
                   on delete cascade);
+-----+------------+-----------+--------+
| sid | student_id | course_id | number |
+-----+------------+-----------+--------+
|   1 |          1 |         1 |     60 |
|   2 |          1 |         2 |     59 |
|   3 |          2 |         2 |    100 |
|   4 |          3 |         2 |     78 |
|   5 |          4 |         3 |     66 |
+-----+------------+-----------+--------+

insert into class(caption) values('三年二班'),('三年三班'),('三年一班');
insert into teacher(tname) values('波多老师'),('苍老师'),('小泽老师');
insert into student(sname,gender,class_id) values('钢蛋','female',1),('铁锤','female',1),('山炮','male',2),('彪哥','male',3);
insert into course(cname,teacher_id) values('生物',1),('体育',1),('物理',2);
insert into score(student_id,course_id,number) values(1,1,60),(1,2,59),(2,2,100),(3,2,78),(4,3,66);

1. 查询每位老师教的课程数量（将右表匹配不上的也能加进来，left的话小泽老师不会统计出来）
select t.tname,count(c.teacher_id) from course as c
right join teacher as t on c.teacher_id=t.tid
group by t.tname;
2. 查询学生的信息及学生所在班级信息
select * from student,class where student.class_id=class.cid;
select * from student inner join class on student.class_id=class.cid;
3. 查询各科成绩最高和最低的分数,形式 : 课程ID  课程名称 最高分  最低分(课程id怎么表示不出来报错，不依赖列)
+cid后报错信息：Expression #1 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'stulast11.c.cid' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by

原错误代码：select  c.cname as 课程名称, max(s.number) as 最高分,min(s.number) as 最低分
from score as s right join course as c
on s.course_id=c.cid group by c.cname; #group by 的不是第一列，在查询的时候第一列cid就不依赖列了

select c.cid as 课程ID,c.cname as 课程名称, max(s.number) as 最高分,min(s.number) as 最低分
from score as s left join course as c
on s.course_id=c.cid group by c.cid;
4. 查询平均成绩大于85分的所有学生学号,姓名和平均成绩
select st.sid, st.sname,avg(s.number) from score as s inner join student as st
on st.sid=s.student_id group by st.sid having avg(s.number)>85;
5. 查询课程编号为2且课程成绩在80以上的学生学号和姓名
select st.sid,st.sname from student as st inner join score as s
on st.sid=s.student_id where s.course_id=2 and s.number>80;
6. 查询各个课程及相应的选修人数
select  c.cname,count(s.student_id) from score as s inner join course as c
on s.course_id=c.cid group by c.cname;
为啥left join和right join结果一样？