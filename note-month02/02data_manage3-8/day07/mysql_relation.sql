CREATE TABLE user (
  id int primary key AUTO_INCREMENT,
  name varchar(30),
  passwd varchar(30) NOT NULL,
  phonenum char(11) NOT NULL
);

CREATE TABLE massage (
  id int primary key AUTO_INCREMENT,
  uid int NOT NULL,
  photo varchar(30) ,
  tetle varchar(30),
  mytime datetime,
  local varchar(30),
  FOREIGN KEY (uid) REFERENCES user (id)
);

CREATE TABLE user_massage (
   id int primary key auto_increment,
   uid int NOT NULL,
   mid int NOT NULL,
   remark text,
   thumbs_up bit,
   FOREIGN KEY (uid) REFERENCES user (id),
   FOREIGN KEY (mid) REFERENCES massage (id)
);