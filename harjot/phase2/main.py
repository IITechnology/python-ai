from typing import List

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import database
import models
import schema
import crud


# ==========================================================
# DATABASE INITIALIZATION
# ==========================================================

models.Base.metadata.create_all(bind=database.engine)


# ==========================================================
# FASTAPI APPLICATION
# ==========================================================

app = FastAPI(
    title="School Portal API",
    version="1.0.0",
    description="Backend API for School Portal"
)


# ==========================================================
# CORS CONFIGURATION
# ==========================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ==========================================================
# DATABASE DEPENDENCY
# ==========================================================

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ==========================================================
# ROOT
# ==========================================================

@app.get("/")
def root():
    return {
        "status": "success",
        "message": "School Portal API Running"
    }


# ==========================================================
# SIGNUP
# ==========================================================

@app.post(
    "/signup",
    response_model=schema.UserResponse,
    status_code=status.HTTP_201_CREATED
)
def signup(
    user: schema.SignupCreate,
    db: Session = Depends(get_db)
):
    """
    Register a new user.
    """

    existing = crud.get_user_by_roll(
        db,
        user.roll
    )

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Roll number already registered."
        )

    return crud.create_user(
        db,
        user
    )


# ==========================================================
# CREATE STUDENT PROFILE
# ==========================================================

@app.post(
    "/students",
    response_model=schema.StudentResponse,
    status_code=status.HTTP_201_CREATED
)
def create_student(
    student: schema.StudentCreate,
    db: Session = Depends(get_db)
):
    """
    Create student profile.

    Roll number must already exist in Users table.
    """

    db_student = crud.create_student(
        db,
        student
    )

    if db_student is None:
        raise HTTPException(
            status_code=404,
            detail="Signup first using this Roll Number."
        )

    return db_student


# ==========================================================
# UPDATE STUDENT PROFILE
# ==========================================================

@app.put(
    "/students/{roll}",
    response_model=schema.StudentResponse
)
def update_student(
    roll: int,
    student: schema.StudentUpdate,
    db: Session = Depends(get_db)
):
    """
    Update student details.
    """

    db_student = crud.update_student(
        db=db,
        roll=roll,
        student=student
    )

    if db_student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found."
        )

    return db_student


# ==========================================================
# GET ALL STUDENTS
# ==========================================================

@app.get(
    "/students",
    response_model=List[schema.StudentResponse]
)
def get_students(
    db: Session = Depends(get_db)
):
    """
    Get all student profiles.
    """

    return crud.get_students(db)


# ==========================================================
# GET SINGLE STUDENT
# ==========================================================

@app.get(
    "/students/{roll}",
    response_model=schema.StudentResponse
)
def get_student(
    roll: int,
    db: Session = Depends(get_db)
):
    """
    Get one student profile.
    """

    student = crud.get_student(
        db,
        roll
    )

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found."
        )

    return student


# ==========================================================
# ADD COURSE
# ==========================================================

@app.post(
    "/students/{roll}/courses",
    response_model=schema.CourseResponse,
    status_code=status.HTTP_201_CREATED
)
def add_course(
    roll: int,
    course: schema.CourseCreate,
    db: Session = Depends(get_db)
):
    """
    Assign a course to a student.
    """

    db_course = crud.add_course(
        db=db,
        roll=roll,
        course=course
    )

    if db_course is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found."
        )

    return db_course


# ==========================================================
# GET STUDENT COURSES
# ==========================================================

@app.get(
    "/students/{roll}/courses",
    response_model=List[schema.CourseResponse]
)
def get_student_courses(
    roll: int,
    db: Session = Depends(get_db)
):
    """
    Get all courses of a student.
    """

    courses = crud.get_student_courses(
        db=db,
        roll=roll
    )

    if courses is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found."
        )

    return courses


# ==========================================================
# DELETE STUDENT
# ==========================================================

@app.delete("/students/{roll}")
def delete_student(
    roll: int,
    db: Session = Depends(get_db)
):
    """
    Delete a student profile.
    """

    deleted = crud.delete_student(
        db=db,
        roll=roll
    )

    if deleted is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found."
        )

    return {
        "message": "Student deleted successfully."
    }
