import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()
try:
    conn = psycopg2.connect(
        user ='postgres',
        password= os.getenv('DB_PASSWORD'),
        host='localhost',
        database='coffee-app'
    )
    
    
    with conn:
        cursor = conn.cursor()
        cursor.execute(
            'CREATE TABLE beans (id SERIAL PRIMARY KEY, name TEXT, method TEXT, rating INTEGER);'
        )

        print('yipeeeee')

        cursor.close()
        
except ConnectionError as exc:
    raise RuntimeError('Failed to open database') from exc
