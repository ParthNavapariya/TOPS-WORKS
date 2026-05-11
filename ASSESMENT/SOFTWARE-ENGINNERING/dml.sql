USE LABTASK;

INSERT INTO users (user_id, name, email, created_at) VALUES 
(1, 'Parth Shah', 'parth@example.com', '2026-05-11'),
(2, 'Amita Patel', 'amita@example.com', '2026-05-11'),
(3, 'Jay Mehra', 'jay@example.com', '2026-05-11'),
(4, 'Sonia Varma', 'sonia@example.com', '2026-05-11'),
(5, 'Rohan Das', 'rohan@example.com', '2026-05-11');

INSERT INTO categories (category_id, category_name) VALUES 
(1, 'Food'), 
(2, 'Rent'), 
(3, 'Entertainment');


INSERT INTO expenses (expense_id, user_id, category_id, amount, expense_date) VALUES 
(101, 1, 1, 500.00, '2026-05-01'),
(102, 1, 2, 15000.00, '2026-05-01'),
(103, 2, 1, 750.50, '2026-05-02'),
(104, 3, 3, 1200.00, '2026-05-03'),
(105, 4, 1, 300.00, '2026-05-04'),
(106, 5, 2, 12000.00, '2026-05-05'),
(107, 1, 3, 2000.00, '2026-05-06'),
(108, 1, 1, 450.00, '2026-05-07'),
(109, 1, 1, 600.00, '2026-05-08'),
(110, 1, 3, 150.00, '2026-05-09');


UPDATE expenses SET amount = 550.00 WHERE expense_id = 101;


DELETE FROM expenses WHERE amount < 200.00;