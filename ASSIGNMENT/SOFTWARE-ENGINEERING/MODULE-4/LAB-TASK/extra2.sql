-- Create a table members in library_db with columns: member_id, member_name,
-- date_of_membership, and email. Insert five records into this table.

use library_db

create table members (member_id int,member_name varchar(10),date_of_membership int,email varchar(20));

insert into members value (1,"rahul",2-3-2026,"rahul@gmail.co,"),
(2,"priya",3-2-2026,"priya@gmail.com"),
(3,"ronak",4-4-2026,"ronak@gmail.com"),
(4,"priyank",4-5-2032,"priyank@gmail.com"),
(5,"rina",4-2-2311,"rina@gmail.com");

insert into members value (6,"pinal",4-3-2021,"pinal@gmail.com");