SELECT t.name AS teacher_name,
       sub.subject_name
FROM teachers t
JOIN subjects sub ON t.id = sub.teacher_id
WHERE t.name = 'Wyatt Hoover';