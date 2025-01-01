import psycopg2

DB_NAME = "postgres"
DB_USER = "myDB"
DB_PASSWORD = 12345
DB_HOST = "localhost"
DB_PORT = 5432


def create_connection():
    conn = psycopg2.connect(
        dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
    )
    conn.autocommit = True
    return conn
