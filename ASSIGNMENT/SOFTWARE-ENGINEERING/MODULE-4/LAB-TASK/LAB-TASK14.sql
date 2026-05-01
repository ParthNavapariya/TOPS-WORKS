-- Lab 3: Limit the results of the SELECT query to show only the top two courses using LIMIT.
-- use databse
use SCHOOL_DB

-- 

CREATE TABLE cources9 (cources_id int PRIMARY KEY,cource_name varchar(10),cource_credits int);


ALTER TABLE cources9
ADD (cource_duration int);

INSERT INTO cources9 VALUES
(1,'backend',4,5),
(2,'frontend',3,3),
(3,'mean',2,2),
(4,'social',1,1);



SELECT * FROM cources9
LIMIT 2;