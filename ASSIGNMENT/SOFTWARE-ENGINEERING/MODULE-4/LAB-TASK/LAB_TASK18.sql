-- nsert additional rows, then use ROLLBACK to undo the last insert operation.
-- 1. Use the database
USE LABTASK;

-- 2. Start a new transaction
START TRANSACTION;

-- 3. Insert some rows
INSERT INTO courses (course_id, course_name) VALUES (201, 'Cloud Computing');
INSERT INTO courses (course_id, course_name) VALUES (202, 'Machine Learning');

-- 4. Check the table (You will see 201 and 202 here)
SELECT * FROM courses;

-- 5. Undo the inserts since the last START TRANSACTION
ROLLBACK;

-- 6. Verify they are gone
-- (The table will now look exactly as it did before Step 2)
SELECT * FROM courses;