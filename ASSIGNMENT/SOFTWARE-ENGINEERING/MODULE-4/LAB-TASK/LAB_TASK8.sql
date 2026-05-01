-- Modify the courses table by adding a column course_duration using the ALTER
-- command

-- use databse
use SCHOOL_DB

-- 

CREATE TABLE cources1 (cources_id int PRIMARY KEY,cource_name varchar(10),cource_credits int);


ALTER TABLE cources1
ADD (cource_duration int);

