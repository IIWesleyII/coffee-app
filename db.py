import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()


CREATE_BEANS_TABLE = 'CREATE TABLE IF NOT EXISTS beans (id SERIAL PRIMARY KEY, name TEXT, method TEXT, rating INTEGER);'
INSERT_BEAN = 'INSERT INTO beans (name,method,rating) VALUES (%s,%s,%s);'
GET_ALL_BEANS = 'SELECT * FROM beans'
GET_BEANS_BY_NAME = 'SELECT * FROM beans WHERE name = %s;'
GET_BEST_PREPARATION_FOR_BEAN = '''
SELECT * FROM beans
WHERE name = %s
ORDER BY rating DESC
LIMIT 1;
'''

def connect():
    try:
        conn = psycopg2.connect(
            user ='postgres',
            password= os.getenv('DB_PASSWORD'),
            host='localhost',
            database='coffee-app'
        )
    except ConnectionError as exc:
        raise RuntimeError('Failed to open database') from exc

    return conn
    

def create_table(conn): 
    with conn:
        cursor = conn.cursor()
        cursor.execute(CREATE_BEANS_TABLE)
        cursor.close()


def add_bean(conn,name,method,rating):
    with conn:
        cursor = conn.cursor()
        cursor.execute(INSERT_BEAN, (name,method,rating))
        cursor.close()


def get_all_beans(conn):
    with conn:
        cursor = conn.cursor()
        cursor.execute(GET_ALL_BEANS)
        result = cursor.fetchall()
        cursor.close()
        return result
        

def get_beans_by_name(conn, name):
    with conn:
        cursor = conn.cursor()
        cursor.execute(GET_BEANS_BY_NAME, (name,))
        result = cursor.fetchall()
        cursor.close()
        return result
       

def get_best_preparation_by_bean(conn,name):
    with conn:
        cursor = conn.cursor()
        cursor.execute(GET_BEST_PREPARATION_FOR_BEAN, (name,))
        result = cursor.fetchall()
        cursor.close()
        return result