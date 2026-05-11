-- Create two tables: departments and employees. Perform an INNER JOIN to
-- display employees along with their respective departments.

-- Create the Departments table
CREATE TABLE departmentsss (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50) NOT NULL
);

-- Create the Employees table
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50) NOT NULL,
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES departmentsss(dept_id)
);

-- Insert sample data
INSERT INTO departmentsss (dept_id, dept_name) VALUES 
(1, 'IT'), 
(2, 'Human Resources'), 
(3, 'Finance');

INSERT INTO employees (emp_id, emp_name, dept_id) VALUES 
(1011, 'Parth', 1), 
(1022, 'Amita', 2), 
(1033, 'Jay', 1),
(1044, 'Sonia', 3);