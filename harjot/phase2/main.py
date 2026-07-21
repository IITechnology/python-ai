from fastapi import FastAPI,Depends,HTTPException # type: ignore
from sqlalchemy.orm import Session # type: ignore
from typing import List
from fastapi.middleware.cors import CORSMiddleware # type: ignore
import database, models, schema, crud

models.Base.metadata.create_all(bind=database.engine)

app=FastAPI(title="schoolportal")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():           #common function
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/students",response_model=List[schema.StudentResponse])
def get_allstudent(db:Session=Depends(get_db)):
    return crud.get_students(db)

@app.post("/students", response_model=schema.StudentResponse)
def enroll_student(student:schema.StudentCreate,db:Session=Depends(get_db)):
    db_student=crud.get_student(db,roll=student.roll)
    if db_student:
        raise HTTPException(status_code=400,detail="Student already registered")
    return crud.create_students(db, student=student)

@app.post("/students/{roll}/courses",response_model=schema.CourseResponse)
def create_course(roll:int,course:schema.CourseCreate,db:Session=Depends(get_db)):
    db_student=crud.get_student(db,roll=roll)
    if not db_student:
        raise HTTPException(status_code=400,detail="Student not found")
    return crud.add_course(db,cousre=course,roll=roll)

@app.delete("/students/{roll}")
def remove_student(roll: int,db: Session = Depends(get_db)):
    student = crud.delete_student(db, roll)
    if student is None:
        raise HTTPException(status_code=404,detail="Student not found")
    return {"message": "Student deleted successfully"}