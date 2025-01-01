import random
import logging
import psycopg2
from faker import Faker
from psycopg2 import DatabaseError

DB_NAME = "postgres"
DB_USER = "myDB"
DB_PASSWORD = 12345
DB_HOST = "localhost"
DB_PORT = 5432

fake = Faker()


def create_connection():
    conn = psycopg2.connect(
        dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
    )
    conn.autocommit = True
    return conn


def insert_groups(conn, num_groups=3):
    group_ids = []
    try:
        with conn.cursor() as cur:
            for _ in range(num_groups):
                group_name = f"Group {fake.unique.pyint(min_value=1, max_value=999)}"
                cur.execute(
                    """
                    INSERT INTO groups (name) VALUES (%s) RETURNING id;
                """,
                    (group_name,),
                )
                new_id = cur.fetchone()[0]
                group_ids.append(new_id)
        return group_ids
    except DatabaseError as e:
        logging.error(e)
        conn.rollback()


def insert_teachers(conn, min_teachers=3, max_teachers=5):
    teacher_ids = []
    num_teachers = random.randint(min_teachers, max_teachers)
    try:
        with conn.cursor() as cur:
            for _ in range(num_teachers):
                name = fake.name()
                cur.execute(
                    """
                    INSERT INTO teachers (name) VALUES (%s) RETURNING id;
                """,
                    (name,),
                )
                new_id = cur.fetchone()[0]
                teacher_ids.append(new_id)
        return teacher_ids
    except DatabaseError as e:
        logging.error(e)
        conn.rollback()


def insert_subjects(conn, teacher_ids, min_subjects=5, max_subjects=8):
    subject_ids = []
    num_subjects = random.randint(min_subjects, max_subjects)
    subject_names = [
        "Mathematics",
        "History",
        "Chemistry",
        "Biology",
        "Physics",
        "Literature",
        "Computer Science",
        "Economics",
        "Geography",
    ]
    random.shuffle(subject_names)
    chosen_subjects = subject_names[:num_subjects]
    try:
        with conn.cursor() as cur:
            for sub_name in chosen_subjects:
                teacher_id = random.choice(teacher_ids)
                cur.execute(
                    """
                    INSERT INTO subjects (subject_name, teacher_id) 
                    VALUES (%s, %s) RETURNING id;
                """,
                    (sub_name, teacher_id),
                )
                new_id = cur.fetchone()[0]
                subject_ids.append(new_id)
        return subject_ids
    except DatabaseError as e:
        logging.error(e)
        conn.rollback()


def insert_students(conn, group_ids, min_students=30, max_students=50):

    student_data = []
    num_students = random.randint(min_students, max_students)
    try:
        with conn.cursor() as cur:
            for _ in range(num_students):
                student_name = fake.name()
                date_of_birth = fake.date_of_birth(minimum_age=16, maximum_age=30)
                group_id = random.choice(group_ids)
                cur.execute(
                    """
                    INSERT INTO students (name, date_of_birth, group_id) 
                    VALUES (%s, %s, %s) RETURNING id;
                """,
                    (student_name, date_of_birth, group_id),
                )
                new_id = cur.fetchone()[0]
                student_data.append((new_id, group_id))
        return student_data
    except DatabaseError as e:
        logging.error(e)
        conn.rollback()


def insert_grades(conn, student_data, subject_ids, max_grades_per_subject=20):
    try:
        with conn.cursor() as cur:
            for st_id, _ in student_data:
                for subj_id in subject_ids:

                    num_grades = random.randint(0, max_grades_per_subject)
                    for _ in range(num_grades):
                        grade_value = random.randint(0, 100)
                        grade_date = fake.date_between(
                            start_date="-1y", end_date="today"
                        )
                        cur.execute(
                            """
                            INSERT INTO grades (student_id, subject_id, grade_value, grade_date)
                            VALUES (%s, %s, %s, %s);
                        """,
                            (st_id, subj_id, grade_value, grade_date),
                        )
    except DatabaseError as e:
        logging.error(e)
        conn.rollback()


def main():
    conn = create_connection()

    group_ids = insert_groups(conn, num_groups=3)
    teacher_ids = insert_teachers(conn, min_teachers=3, max_teachers=5)
    subject_ids = insert_subjects(conn, teacher_ids, min_subjects=5, max_subjects=8)
    student_data = insert_students(conn, group_ids, min_students=30, max_students=50)
    insert_grades(conn, student_data, subject_ids, max_grades_per_subject=20)

    conn.close()
    print("Done")


if __name__ == "__main__":
    main()
