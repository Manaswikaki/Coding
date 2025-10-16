WITH primary_candidates AS (
    SELECT
        employee_id,
        department_id
    FROM Employee
    WHERE primary_flag = 'Y'
),
employee_counts AS (
    SELECT
        employee_id,
        COUNT(*) AS dept_count
    FROM Employee
    GROUP BY employee_id
)
SELECT
    p.employee_id,
    p.department_id
FROM primary_candidates p
UNION ALL
SELECT
    e.employee_id,
    e.department_id
FROM Employee e
JOIN employee_counts c
  ON e.employee_id = c.employee_id
WHERE c.dept_count = 1
ORDER BY employee_id;