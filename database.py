import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

def load_courses():
    conn = mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
    mycursor = conn.cursor()
    mycursor.execute("SELECT * FROM courses")
    result = mycursor.fetchall()
    columns = [desc[0] for desc in mycursor.description]
    courses = [dict(zip(columns, row)) for row in result]
    conn.close()
    return courses

def load_course(id):
    conn = mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
    mycursor = conn.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM courses WHERE id = %s", (id,))
    row = mycursor.fetchone()
    conn.close()
    if row is None:
        return {"error": "Course record does not exist!"}
    else:
         return row
    
def add_application_to_db(course_id, application):
    conn = mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
    mycursor = conn.cursor()
    sql_query = "INSERT INTO applications (course_id, name, email, phone, motivation) VALUES (%s, %s, %s, %s, %s)"
    
    data = (
        course_id,
        application.get('name'),
        application.get('email'),
        application.get('phone'),
        application.get('motivation')
    )
    mycursor.execute(sql_query, data)
    conn.commit()
    conn.close()

