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