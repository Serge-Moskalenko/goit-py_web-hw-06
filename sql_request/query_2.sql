SELECT s.id AS student_id,
       s.name AS student_name,
       AVG(g.grade_value) AS avg_grade
FROM students s
JOIN grades g ON s.id = g.student_id
JOIN subjects sub ON sub.id = g.subject_id
WHERE sub.subject_name = 'Computer Science'
GROUP BY s.id, s.name
ORDER BY avg_grade DESC
LIMIT 1;
