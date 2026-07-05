import sqlite3
DB_FILE="student_records.db"
def init_db():                              #initialize the database
    connection= sqlite3.connect(DB_FILE)
    cursor=connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS STUDENTS (
                rollnumber INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                marks REAL  
                   )
    ''')
    connection.commit()
    print(f"Database and Student Table is Created.")
    connection.close()

def add_student(rollnumber: int, name: str, marks: float):            #initialize the database
    connection= sqlite3.connect(DB_FILE)
    cursor=connection.cursor()
    cursor.execute('''
        INSERT INTO STUDENTS (rollnumber,name,marks) VALUES(?,?,?) 
    ''', (rollnumber,name,marks)
    )
    connection.commit()
    print(f"Student Created Successfully.")
    connection.close()
def view_all_students():
    connection= sqlite3.connect(DB_FILE)
    cursor=connection.cursor()
    cursor.execute('SELECT * FROM STUDENTS')
    records = cursor.fetchall()
    for row in records:
        print(f" Roll:{row[0]} | Name: {row[1]} | Marks: {row[2]} ")
    connection.close()

init_db()
#add_student(1,"harjot",19.5)
#add_student(2,"gitesh",12.3)
#add_student(3,"daksh",14.5)
#add_student(4,"harjot",19.5)
view_all_students()
    # Roll:1 | Name: harjot | Marks: 19.5
    # Roll:2 | Name: gitesh | Marks: 12.3
    # Roll:3 | Name: daksh | Marks: 14.5
    # Roll:4 | Name: harjot | Marks: 19.5

