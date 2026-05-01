-- : Write SQL queries to retrieve specific columns (student_name and age) from the
-- students table.

-- use databse
USE SCHOOL_db


--  create table
CREATE TABLE STUDENT3 (STUDENT_ID int ,STUDENT_NAME varchar(20),AGE int, ADDRESS varchar(30));

-- insert data
insert into STUDENT3 values(1,"parth",25,"paldi"),
						(2,"maulik",23,"parimal"),
                        (3,"miki",24,"cgroad"),
                        (4,"pria",22,"university"),
                        (5,"pini",21,"nikol");
                        
                        -- specefic column
                        select STUDENT_NAME , AGE  from STUDENT3