SELECT gr.name AS group_name,
       s.id AS student_id,
       s.name AS student_name
FROM groups gr
JOIN students s ON gr.id = s.group_id
WHERE gr.name = 'Group 440'
ORDER BY student_name;

