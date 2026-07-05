Fast API setup with hello world.
## What is Fast API?
Fast API is a modern, fast , web framework for building APIs with python.
## What is API?

##uvicorn main:app --reload
main: refers to the python file, (main.py)
app: refers to fast api object created inside the main
--reload: refers to automatically restarts the server when code changed

## swager 
to open the swager to navigate to browser: 'localhost:8000/docs'

## SQLITE
this is python's native package, no complex installation needed, data is directly stored in local file, 

## SQLITE Flow
5 steps: # these are predefined structure

1. Connect to db file: connection= sqlite3.connect("txtfilename.db") # this is to tell path
2. Create an execution cursor: cursor=connection.cursor() # this is to tell on which line you are
3. Execute sql query: cursor.execute("qeury")
4. Commit transational changes: connection.commit()
5. Close the connection: connection.close()

# ##ORM ( SQLALchemy)
-- "select * from table" // syntax error, secuirty vulenrablity and poor scale.
## OBJECT RELATIONSHIP MODAL its automatically intract with SQL DB using pure Obeject Orientation

* Instead of ** SQL TABLES ** we have to write ** Python Classes **
* Instead of ** SQL ROW ** we have to write ** Python Objects **
* Instead of ** Query Execute ** we have to write ** Python methods ( ` session.add() `, ` session.query() `,   ) **

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_URL = "sqlite:///./school.db"
engine = create_engine(DB_URL)
sessionLocal = sessionmaker(autocommit=False, autoflush= False, bind=engine )




