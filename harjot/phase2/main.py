from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

import database
import models
import schema
import crud

# ----------------------------------------------------
# Create Database Tables
# ----------------------------------------------------
models.Base.metadata.create_all(bind=database.engine)

# ----------------------------------------------------
# FastAPI App
# ----------------------------------------------------
app = FastAPI(title="School Portal")

# ----------------------------------------------------
# CORS
# ----------------------------------------------------
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
# SIGNUP
# ==========================================================

@app.post(
    "/signup",
    response_model=schema.UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def signup(
    user: schema.SignupCreate,
    db: Session = Depends(database.get_db),
):
    existing_user = crud.get_user_by_roll(db, user.roll)

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="User already registered.",
        )

    return crud.create_user(db, user)


# ==========================================================
# STUDENTS
# ==========================================================

@app.get(
    "/students",
    response_model=List[schema.StudentWithCourses],
)
def get_all_students(
    db: Session = Depends(database.get_db),
):
    return crud.get_students(db)


@app.post(
    "/students",
    response_model=schema.StudentResponse,
    status_code=status.HTTP_201_CREATED,
)
def enroll_student(
    student: schema.StudentCreate,
    db: Session = Depends(database.get_db),
):
    existing_student = crud.get_student(db, student.roll)

    if existing_student:
        raise HTTPException(
            status_code=400,
            detail="Student already exists.",
        )

    return crud.create_student(db, student)


@app.delete("/students/{roll}")
def delete_student(
    roll: int,
    db: Session = Depends(database.get_db),
):
    student = crud.delete_student(db, roll)

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found.",
        )

    return {
        "message": "Student deleted successfully."
    }


# ==========================================================
# COURSES
# ==========================================================

@app.post(
    "/students/{roll}/courses",
    response_model=schema.CourseResponse,
)
def add_course(
    roll: int,
    course: schema.CourseCreate,
    db: Session = Depends(database.get_db),
):
    student = crud.get_student(db, roll)

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found.",
        )

    return crud.add_course(
        db=db,
        course=course,
        roll=roll,
    )


# ==========================================================
# ROOT
# ==========================================================

@app.get("/")
def root():
    return {
        "message": "School Portal API Running"
    }