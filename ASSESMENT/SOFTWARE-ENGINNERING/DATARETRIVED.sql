-- Join નો ઉપયોગ કરીને બધી વિગતો જોવી
SELECT e.expense_date, e.amount, u.name, c.category_name
FROM expenses e
INNER JOIN users u ON e.user_id = u.user_id
INNER JOIN categories c ON e.category_id = c.category_id;

-- કેટેગરી મુજબ ટોટલ ખર્ચો
SELECT c.category_name, SUM(e.amount) AS total_amount
FROM expenses e
JOIN categories c ON e.category_id = c.category_id
GROUP BY c.category_name;

-- સૌથી વધુ ખર્ચ કરનાર યુઝર મુજબ સોર્ટિંગ
SELECT u.name, SUM(e.amount) AS total_spent
FROM users u
JOIN expenses e ON u.user_id = e.user_id
GROUP BY u.name
ORDER BY total_spent DESC;