import psycopg2

conn = psycopg2.connect(database="flask_db", host="localhost", user="postgres", password="1523", port="5432")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE USERS (ID SERIAL PRIMARY KEY, NAME VARCHAR);''')
cursor.execute('''INSERT INTO USERS (NAME) VALUES ('Nathan'),('joao'),('maria'),('victor');''')

conn.commit()
cursor.close()
conn.close()
