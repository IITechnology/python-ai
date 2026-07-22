from sqlalchemy.orm import Session
from passlib.context import CryptContext

import models
import schema


# ======================================================
# PASSWORD HASHING
# ======================================================

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


# ======================================================
# USER CRUD
# ======================================================

def get_user_by_roll(
    db: Session,
    roll: int
):
    return db.query(models.User).filter(
        models.User.roll == roll
    ).first()



def create_user(
    db: Session,
    user: schema.SignupCreate
):

    hashed_password = pwd_context.hash(
        user.password
    )


    db_user = models.User(
        roll=user.roll,
        hashed_password=hashed_password
    )


    db.add(db_user)
    db.commit()
    db.refresh(db_user)


    return db_user



def verify_password(
    plain_password: str,
    hashed_password: str
):
    return pwd_context.verify(
        plain_password,
        hashed_password
    )



# ======================================================
# STUDENT CRUD
# ======================================================

def get_student(
    db: Session,
    roll: int
):
    return db.query(models.Student).filter(
        models.Student.roll == roll
    ).first()



def get_students(
    db: Session,
    skip: int = 0,
    limit: int = 100
):
    return db.query(models.Student)\
        .offset(skip)\
        .limit(limit)\
        .all()



def create_student(
    db: Session,
    student: schema.StudentCreate
):

    db_student = models.Student(
        roll=student.roll,
        name=student.name
    )


    db.add(db_student)
    db.commit()
    db.refresh(db_student)


    return db_student



def delete_student(
    db: Session,
    roll: int
):

    student = db.query(models.Student).filter(
        models.Student.roll == roll
    ).first()


    if student is None:
        return None


    db.delete(student)
    db.commit()


    return student



# ======================================================
# COURSE CRUD
# ======================================================

def add_course(
    db: Session,
    course: schema.CourseCreate,
    roll: int
):

    db_course = models.Course(
        title=course.title,
        student_roll=roll
    )


    db.add(db_course)
    db.commit()
    db.refresh(db_course)


    return db_course