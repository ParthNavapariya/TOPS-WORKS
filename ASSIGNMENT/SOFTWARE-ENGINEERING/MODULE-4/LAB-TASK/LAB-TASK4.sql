--  Write SQL queries to retrieve all students whose age is greater than 10.

-- use databse
USE SCHOOL_db


--  create table
CREATE TABLE STUDENT4 (STUDENT_ID int ,STUDENT_NAME varchar(20),AGE int, ADDRESS varchar(30));

-- insert data
insert into STUDENT4 values(1,"parth",25,"paldi"),
						(2,"maulik",23,"parimal"),
                        (3,"miki",24,"cgroad"),
                        (4,"pria",22,"university"),
                        (5,"pini",21,"nikol");
                        
                        -- whose age is greater than 10
                        select * from STUDENT4 WHERE AGE > 10