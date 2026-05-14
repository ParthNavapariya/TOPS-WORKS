--  Create a database called library_db and a table books with columns: book_id,
-- title, author, publisher, year_of_publication, and price. Insert five records into
-- the table


CREATE DATABASE library_db

use library_db

create table books (book_id int,title varchar(10),author varchar(10),publisher varchar(10),year_of_publication int,price int);

insert into books value(1,"janam","priytan","ratna",2022,500),
(2,"mian","rinka","manthan",2021,300),
(3,"udan","priytanam","ratnam",2020,200),
(4,"miniti","siniki","munki",2012,300),
(5,"jf","w","bu",2022,200);