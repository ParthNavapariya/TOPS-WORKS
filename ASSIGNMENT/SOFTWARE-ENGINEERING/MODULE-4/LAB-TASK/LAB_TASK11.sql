-- • Lab 2: Update the course duration of a specific course using the UPDATE command.

-- use databse
use SCHOOL_DB

-- 

CREATE TABLE cources3 (cources_id int PRIMARY KEY,cource_name varchar(10),cource_credits int);


ALTER TABLE cources3
ADD (cource_duration int);

insert into cources3 values(1,"backend",4,5),
(2,"frontend",3,3),
(3,"mean",2,2),
(4,"social",1,1);

update cources3 set cource_duration = 4  where cources_id = 2;

 