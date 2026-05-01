-- nsert five records into the students table and retrieve all records using the SELECT
-- statement.

-- use databse
USE SCHOOL_db


--  create table
CREATE TABLE STUDENT2 (STUDENT_ID int ,STUDENT_NAME varchar(20),AGE int, ADDRESS varchar(30));

-- insert data
insert into STUDENT2 values(1,"parth",25,"paldi"),
						(2,"maulik",23,"parimal"),
                        (3,"miki",24,"cgroad"),
                        (4,"pria",22,"university"),
                        (5,"pini",21,"nikol");
                        
                        select * from STUDENT2