-- Delete a course with a specific course_id from the courses table using the DELETE
-- command.

-- use databse
use SCHOOL_DB

-- 

CREATE TABLE cources4 (cources_id int PRIMARY KEY,cource_name varchar(10),cource_credits int);


ALTER TABLE cources4
ADD (cource_duration int);

insert into cources4 values(1,"backend",4,5),
(2,"frontend",3,3),
(3,"mean",2,2),
(4,"social",1,1);


DELETE FROM cources4 
WHERE cources_id = 4;

select * from cources4