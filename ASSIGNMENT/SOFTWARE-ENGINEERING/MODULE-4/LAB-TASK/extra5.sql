-- Add a CHECK constraint to ensure that the price of books in the books table is
-- greater than 0.

USE library_db;

create table bookks (bookks_id INT,	book_name varchar(10),book_price int);

insert into bookks values (1,"sqlbooks",-100),
(2,"pythob",100),
(3,"html",20);


UPDATE bookks
SET book_price = 100
WHERE bookks_id = 1;

ALTER TABLE bookks
ADD CONSTRAINT chk_book_price
CHECK (book_price > 0);