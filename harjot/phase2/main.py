from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy.orm import Session
from typing import List
import database, models, schema, crud

models.Base.metadata.create_all(bind=database.engine)
app=FastAPI(title="schoolportal")

def get_db():           #common function
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/students",response_model=List[schema.StudentResponse])
def get_allstudent(db:Session=Depends(get_db)):
    return crud.get_students(db)

@app.post("/students",response_model=List[schema.StudentResponse])
def enroll_student(student:schema.StudentCreate,db:Session=Depends(get_db)):
    db_student=crud.get_student(db,roll=student.roll)
    if db_student:
        raise HTTPException(status_code=400,detail="Student already registered")
    return crud.create_students(db, student=student)