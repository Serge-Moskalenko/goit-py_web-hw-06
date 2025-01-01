SELECT t.name AS teacher_name,
       AVG(g.grade_value) AS avg_teacher_grade
FROM teachers t
JOIN subjects sub ON t.id = sub.teacher_id
JOIN grades g ON g.subject_id = sub.id
WHERE t.name = 'Kendra Vasquez'
GROUP BY t.id, t.name;