-- Insert three records into the courses table using the INSERT comman.
use databse
use SCHOOL_DB

-- 

CREATE TABLE cources2 (cources_id int PRIMARY KEY,cource_name varchar(10),cource_credits int);


ALTER TABLE cources2
ADD (cource_duration int);

insert into cources2 values(1,"backend",4,5),
(2,"frontend",3,3),
(3,"mean",2,2),
(4,"social",1,1);

