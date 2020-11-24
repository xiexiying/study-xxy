create function st() returns int
begin
return (select score from cls order by score desc limit 1);
end
$$
delimiter ;
变量
delimiter $$
create function st1() returns int
begin
declare score1 float;
declare score2 float;
set score1=(select score from cls where id=1);
select score from cls where id =2 into score2;
return score1+score2;
end $$
