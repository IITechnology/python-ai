# ==========================================================
# IMPORTS
# ==========================================================

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session

import models
import schema
import crud

from database import Base, SessionLocal, engine

# ==========================================================
# CREATE DATABASE TABLES
# ==========================================================

Base.metadata.create_all(bind=engine)

# ==========================================================
# FASTAPI APP
# ==========================================================

app = FastAPI(

    title="School Portal API",

    version="2.0.0",

    description="Student Management Portal Backend"

)


# ==========================================================
# CORS
# ==========================================================

app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]

)


# ==========================================================
# DATABASE DEPENDENCY
# ==========================================================

def get_db():

    db = SessionLocal()

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

        "message": "School Portal Backend Running",

        "version": "2.0"

    }
# ==========================================================
# AUTHENTICATION ROUTES
# ==========================================================

@app.post(
    "/signup",
    response_model=schema.StudentResponse,
    status_code=201
)
def signup(
    user: schema.UserSignup,
    db: Session = Depends(get_db)
):

    # -------------------------------
    # Check Roll Number
    # -------------------------------

    if crud.roll_exists(db, user.roll):

        raise HTTPException(
            status_code=400,
            detail="Roll Number already registered."
        )

    # -------------------------------
    # Check Email
    # -------------------------------

    if crud.email_exists(db, user.email):

        raise HTTPException(
            status_code=400,
            detail="Email already registered."
        )

    # -------------------------------
    # Create Student
    # -------------------------------

    student = crud.signup(db, user)

    return student


# ==========================================================
# LOGIN
# ==========================================================

@app.post(
    "/login",
    response_model=schema.LoginResponse
)
def login(
    credentials: schema.UserLogin,
    db: Session = Depends(get_db)
):

    student = crud.login(db, credentials)

    if student is None:

        raise HTTPException(
            status_code=401,
            detail="Invalid Roll Number or Password."
        )

    return {

        "message": "Login Successful",

        "student": student

    }
# ==========================================================
# STUDENT ROUTES
# ==========================================================

@app.get(
    "/students",
    response_model=list[schema.StudentResponse]
)
def get_students(
    db: Session = Depends(get_db)
):

    return crud.get_students(db)


# ==========================================================

@app.get(
    "/students/{roll}",
    response_model=schema.StudentResponse
)
def get_student(
    roll: int,
    db: Session = Depends(get_db)
):

    student = crud.get_student(db, roll)

    if student is None:

        raise HTTPException(

            status_code=404,

            detail="Student not found."

        )

    return student


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

    try:

        updated_student = crud.update_student(
            db,
            roll,
            student
        )

    except ValueError as e:

        raise HTTPException(

            status_code=400,

            detail=str(e)

        )

    if updated_student is None:

        raise HTTPException(

            status_code=404,

            detail="Student not found."

        )

    return updated_student


# ==========================================================

@app.delete("/students/{roll}")
def delete_student(
    roll: int,
    db: Session = Depends(get_db)
):

    student = crud.delete_student(
        db,
        roll
    )

    if student is None:

        raise HTTPException(

            status_code=404,

            detail="Student not found."

        )

    return {

        "message": "Student deleted successfully."

    }


# ==========================================================
# DASHBOARD STATISTICS
# ==========================================================

@app.get("/stats")
def dashboard_stats(
    db: Session = Depends(get_db)
):

    return {

        "students": crud.total_students(db),

        "courses": crud.total_courses(db)

    }
# ==========================================================
# COURSE ROUTES
# ==========================================================

@app.post(
    "/students/{roll}/courses",
    response_model=schema.CourseResponse,
    status_code=201
)
def add_course(
    roll: int,
    course: schema.CourseCreate,
    db: Session = Depends(get_db)
):

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

@app.get(
    "/students/{roll}/courses",
    response_model=list[schema.CourseResponse]
)
def get_courses(
    roll: int,
    db: Session = Depends(get_db)
):

    courses = crud.get_courses(
        db,
        roll
    )

    if courses is None:

        raise HTTPException(

            status_code=404,

            detail="Student not found."

        )

    return courses


# ==========================================================

@app.put(
    "/courses/{course_id}",
    response_model=schema.CourseResponse
)
def update_course(
    course_id: int,
    course: schema.CourseUpdate,
    db: Session = Depends(get_db)
):

    updated_course = crud.update_course(

        db=db,

        course_id=course_id,

        course_update=course

    )

    if updated_course is None:

        raise HTTPException(

            status_code=404,

            detail="Course not found."

        )

    return updated_course


# ==========================================================

@app.delete("/courses/{course_id}")
def delete_course(
    course_id: int,
    db: Session = Depends(get_db)
):

    deleted_course = crud.delete_course(

        db,

        course_id

    )

    if deleted_course is None:

        raise HTTPException(

            status_code=404,

            detail="Course not found."

        )

    return {

        "message": "Course deleted successfully."

    }


# ==========================================================
# HEALTH CHECK
# ==========================================================

@app.get("/health")
def health():

    return {

        "status": "healthy",

        "server": "running"

    }