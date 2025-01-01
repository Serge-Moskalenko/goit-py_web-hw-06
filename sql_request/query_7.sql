SELECT gr.name AS group_name,
       sub.subject_name,
       s.name AS student_name,
       g.grade_value,
       g.grade_date
FROM groups gr
JOIN students s ON gr.id = s.group_id
JOIN grades g ON s.id = g.student_id
JOIN subjects sub ON sub.id = g.subject_id
WHERE gr.name = 'Group 700'
  AND sub.subject_name = 'Chemistry'
ORDER BY s.name, g.grade_date;
