SELECT e.employee_id, e.first_name, e.last_name, d.department_name, p.employee_position_title
FROM msdbom.employee e
LEFT JOIN msdbom.department d ON e.department_id = d.department_id
LEFT JOIN msdbom.employee_position p ON e.employee_position_id = p.employee_position_id
ORDER BY e.first_name;