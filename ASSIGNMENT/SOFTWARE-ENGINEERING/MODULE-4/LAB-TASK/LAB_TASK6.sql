

-- use databse
use SCHOOL_DB

-- 

CREATE TABLE TEACHER2 (teacher_id int PRIMARY KEY,teacher_name varchar(10) NOT NULL ,subject varchar(11) NOT NULL ,email varchar(20) UNIQUE );


CREATE TABLE students3 (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(50),
    teacher_id INT,
    FOREIGN KEY (teacher_id) REFERENCES teacher1(teacher_id)
);