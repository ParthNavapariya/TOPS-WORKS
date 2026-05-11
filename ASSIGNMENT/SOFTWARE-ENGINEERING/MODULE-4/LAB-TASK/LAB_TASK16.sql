-- Revoke the INSERT permission from user1 and give it to user2.
USE LABTASK;

-- 2. Remove INSERT permission from user1
-- Try this first (Table Level):
REVOKE INSERT ON courses FROM 'user1'@'localhost';

-- IF THE ABOVE FAILS, use this (Database Level):
-- REVOKE INSERT ON LABTASK.* FROM 'user1'@'localhost';

-- 3. Give INSERT permission to user2
GRANT INSERT ON courses TO 'user2'@'localhost';

-- 4. Verify the changes
SHOW GRANTS FOR 'user1'@'localhost';
SHOW GRANTS FOR 'user2'@'localhost';