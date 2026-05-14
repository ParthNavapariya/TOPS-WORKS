-- Retrieve all members who joined the library before 2022. Use appropriate SQL syntax
-- with WHERE and ORDER BY.


use library_db

create table memberss (member_id int,member_name varchar(10),date_of_membership date,email varchar(20));

INSERT INTO memberss VALUES
(1,"rahul","2026-03-02","rahul@gmail.com"),
(2,"priya","2026-02-03","priya@gmail.com"),
(3,"ronak","2026-04-04","ronak@gmail.com"),
(4,"priyank","2032-05-04","priyank@gmail.com"),
(5,"rina","2311-02-04","rina@gmail.com"),
(6,"pinal","2021-03-04","pinal@gmail.com");


select * from memberss where date_of_membership < '2022-1-1' order by date_of_membership;
