-- 1. Ensure you are using the correct database
USE LABTASK;

-- 2. Start a transaction (Best practice when using COMMIT)
START TRANSACTION;

-- 3. Insert rows into the courses table
-- Note: Replace 'Course Name' and 'ID' with your actual column names/values
INSERT INTO courses (course_id, course_name) 
VALUES (101, 'Database Management Systems');

INSERT INTO courses (course_id, course_name) 
VALUES (102, 'Data Structures and Algorithms');

INSERT INTO courses (course_id, course_name) 
VALUES (103, 'Web Development');

-- 4. Save the changes permanently to the database
COMMIT;

-- 5. Verify the data is there
SELECT * FROM courses;