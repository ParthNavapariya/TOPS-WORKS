-- Create a SAVEPOINT before updating the courses table, and use it to roll back
-- specific changes.

-- 1. Start the transaction
START TRANSACTION;

-- 2. Insert a new course (This will be kept)
INSERT INTO courses (course_id, course_name) 
VALUES (301, 'Cyber Security');

-- 3. Create a SAVEPOINT
-- This marks a specific spot in time
SAVEPOINT before_update;

-- 4. Perform an UPDATE (The change we might want to undo)
UPDATE courses 
SET course_name = 'ADVANCED Cyber Security' 
WHERE course_id = 301;

-- 5. Check the table (You'll see the name is currently 'ADVANCED')
SELECT * FROM courses;

-- 6. Roll back to the savepoint
-- This undoes the UPDATE, but keeps the INSERT from Step 2
ROLLBACK TO SAVEPOINT before_update;

-- 7. Verify the result
-- The name should be back to 'Cyber Security', but the row still exists!
SELECT * FROM courses;

-- 8. Finalize the remaining changes
COMMIT;