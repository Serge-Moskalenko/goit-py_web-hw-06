from connection import create_connection


def execute_query_from_file(file_path):

    conn = create_connection()
    try:
        with conn.cursor() as cursor:
            with open(file_path, "r") as f:
                sql = f.read()
                cursor.execute(sql)
                rows = cursor.fetchall()
                return rows
    except Exception as e:
        print(f"Ошибка выполнения запроса: {e}")
    finally:
        conn.close()


if __name__ == "__main__":
    results = execute_query_from_file("sql_request/query_9.sql")

    for row in results:
        print(row)
