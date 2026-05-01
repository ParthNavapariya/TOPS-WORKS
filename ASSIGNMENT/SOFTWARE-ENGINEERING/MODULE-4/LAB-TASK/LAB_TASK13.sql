-- • Lab 1: Retrieve all courses from the courses table using the SELECT statement.
-- use databse
use SCHOOL_DB

-- 

CREATE TABLE cources7 (cources_id int PRIMARY KEY,cource_name varchar(10),cource_credits int);


ALTER TABLE cources7
ADD (cource_duration int);

INSERT INTO cources7 VALUES
(1,'backend',4,5),
(2,'frontend',3,3),
(3,'mean',2,2),
(4,'social',1,1);


select * from cources7