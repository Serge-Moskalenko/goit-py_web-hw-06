-- query_10.sql

SELECT DISTINCT sub.subject_name
FROM teachers t
JOIN subjects sub ON t.id = sub.teacher_id
JOIN grades g ON g.subject_id = sub.id
JOIN students s ON s.id = g.student_id
WHERE t.name = 'Terri Maldonado'
  AND s.name = 'Stacey Wilkerson'
ORDER BY sub.subject_name;
