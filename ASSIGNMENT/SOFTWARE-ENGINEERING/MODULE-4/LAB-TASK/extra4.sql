--  Write SQL queries to display the titles of books published by a specific author. Sort the
-- results by year_of_publication in descending order.

use library_db

create table membersss (    book_id INT,
    title VARCHAR(50),
    author_name VARCHAR(50),
    year_of_publication INT);

INSERT INTO membersss VALUES
(1,"Wings of Fire","A P J Abdul Kalam",1999),
(2,"Ignited Minds","A P J Abdul Kalam",2002),
(3,"The Guide","R K Narayan",1958),
(4,"India 2020","A P J Abdul Kalam",1998),
(5,"Malgudi Days","R K Narayan",1943);

SELECT * FROM membersss order by Year_of_publication desc;