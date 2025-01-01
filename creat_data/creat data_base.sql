-- Спочатку видаляємо залежні таблиці (якщо існують):
DROP TABLE IF EXISTS grades;
DROP TABLE IF EXISTS subjects;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS teachers;
DROP TABLE IF EXISTS groups;

-- Створюємо таблиці:
CREATE TABLE groups (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE teachers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    date_of_birth DATE,
    group_id INT NOT NULL,
    CONSTRAINT fk_group
        FOREIGN KEY (group_id)
        REFERENCES groups (id)
        ON DELETE CASCADE
);

CREATE TABLE subjects (
    id SERIAL PRIMARY KEY,
    subject_name VARCHAR(100) NOT NULL,
    teacher_id INT NOT NULL,
    CONSTRAINT fk_teacher
        FOREIGN KEY (teacher_id)
        REFERENCES teachers (id)
        ON DELETE CASCADE
);

CREATE TABLE grades (
    id SERIAL PRIMARY KEY,
    student_id INT NOT NULL,
    subject_id INT NOT NULL,
    grade_value INT NOT NULL,
    grade_date DATE NOT NULL DEFAULT CURRENT_DATE,
    CONSTRAINT fk_student
        FOREIGN KEY (student_id)
        REFERENCES students (id)
        ON DELETE CASCADE,
    CONSTRAINT fk_subject
        FOREIGN KEY (subject_id)
        REFERENCES subjects (id)
        ON DELETE CASCADE
);
