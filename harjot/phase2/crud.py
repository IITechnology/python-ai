from sqlalchemy.orm import Session
from passlib.context import CryptContext

import models
import schema


# ==========================================================
# PASSWORD HASHING
# ==========================================================

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


# ==========================================================
# USER CRUD
# ==========================================================

def get_user_by_roll(
    db: Session,
    roll: int
):
    return (
        db.query(models.User)
        .filter(models.User.roll == roll)
        .first()
    )


def create_user(
    db: Session,
    user: schema.SignupCreate
):
    hashed_password = pwd_context.hash(user.password)

    db_user = models.User(
        roll=user.roll,
        hashed_password=hashed_password
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


# ==========================================================
# STUDENT CRUD
# ==========================================================

def get_student(
    db: Session,
    roll: int
):
    return (
        db.query(models.Student)
        .filter(models.Student.roll == roll)
        .first()
    )


def get_students(
    db: Session
):
    return db.query(models.Student).all()


def create_student(
    db: Session,
    student: schema.StudentCreate
):
    """
    Create profile after signup.

    Roll number must already exist in Users table.
    """

    user = get_user_by_roll(
        db,
        student.roll
    )

    if user is None:
        return None

    existing_student = get_student(
        db,
        student.roll
    )

    if existing_student:
        return existing_student

    db_student = models.Student(
        user_id=user.id,
        roll=student.roll,
        name=student.name,
        email=student.email,
        branch=student.branch,
        semester=student.semester
    )

    db.add(db_student)
    db.commit()
    db.refresh(db_student)

    return db_student


def update_student(
    db: Session,
    roll: int,
    student: schema.StudentUpdate
):
    db_student = get_student(
        db,
        roll
    )

    if db_student is None:
        return None

    if student.email is not None:
        db_student.email = student.email

    if student.branch is not None:
        db_student.branch = student.branch

    if student.semester is not None:
        db_student.semester = student.semester

    db.commit()
    db.refresh(db_student)

    return db_student


def delete_student(
    db: Session,
    roll: int
):
    student = get_student(
        db,
        roll
    )

    if student is None:
        return None

    db.delete(student)
    db.commit()

    return student


# ==========================================================
# COURSE CRUD
# ==========================================================

def add_course(
    db: Session,
    roll: int,
    course: schema.CourseCreate
):
    student = get_student(
        db,
        roll
    )

    if student is None:
        return None

    db_course = models.Course(
        title=course.title,
        student_id=student.id
    )

    db.add(db_course)
    db.commit()
    db.refresh(db_course)

    return db_course


def get_student_courses(
    db: Session,
    roll: int
):
    student = get_student(
        db,
        roll
    )

    if student is None:
        return None

    return student.courses