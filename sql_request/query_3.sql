SELECT gr.name AS group_name,
       AVG(g.grade_value) AS avg_grade
FROM groups gr
JOIN students s ON gr.id = s.group_id
JOIN grades g ON s.id = g.student_id
JOIN subjects sub ON sub.id = g.subject_id
WHERE sub.subject_name = 'Physics'
GROUP BY gr.id, gr.name
ORDER BY gr.name;