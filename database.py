import mysql.connector

def load_courses():
    conn = mysql.connector.connect(host='localhost', user='root', password='12345678', database='orientdb')
    mycursor = conn.cursor()
    mycursor.execute("SELECT * FROM courses")
    result = mycursor.fetchall()
    columns = [desc[0] for desc in mycursor.description]
    courses = [dict(zip(columns, row)) for row in result]
    conn.close()
    return courses