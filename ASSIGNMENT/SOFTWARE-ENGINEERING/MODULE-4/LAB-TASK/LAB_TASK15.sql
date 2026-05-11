 -- Create two new users user1 and user2 and grant user1 permission to SELECT
-- from the courses table.
-- Select Database
USE labtask;

CREATE TABLE IF NOT EXISTS courses (
  course_id INT PRIMARY KEY,
  course_name VARCHAR(100)
);
CREATE USER 'user1'@'localhost' IDENTIFIED BY 'user123';

CREATE USER 'user2'@'localhost' IDENTIFIED BY 'user123';
-- Grant SELECT permission on courses table to user1
GRANT SELECT ON labtask.courses TO 'user1'@'localhost';

-- Apply changes
FLUSH PRIVILEGES;


