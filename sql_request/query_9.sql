SELECT DISTINCT sub.subject_name
FROM students s
JOIN grades g ON s.id = g.student_id
JOIN subjects sub ON g.subject_id = sub.id
WHERE s.name = 'Albert Oconnell'
ORDER BY sub.subject_name;
