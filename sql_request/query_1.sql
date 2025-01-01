WITH student_avg AS (
    SELECT s.id AS student_id,
           s.name AS student_name,
           AVG(g.grade_value) AS avg_grade
    FROM students s
    JOIN grades g ON s.id = g.student_id
    GROUP BY s.id, s.name
)
SELECT student_id, student_name, avg_grade
FROM student_avg
ORDER BY avg_grade DESC
LIMIT 5;