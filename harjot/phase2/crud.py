# ==========================================================
# IMPORTS
# ==========================================================

from sqlalchemy.orm import Session

import models
import schema


# ==========================================================
# SIGNUP
# ==========================================================

def signup(
    db: Session,
    user: schema.UserSignup
):

    # --------------------------------------
    # Check Roll Number
    # --------------------------------------

    existing_roll = (
        db.query(models.User)
        .filter(models.User.roll == user.roll)
        .first()
    )

    if existing_roll:

        return None

    # --------------------------------------
    # Check Email
    # --------------------------------------

    existing_email = (
        db.query(models.User)
        .filter(models.User.email == user.email)
        .first()
    )

    if existing_email:

        return None

    # --------------------------------------
    # Create User
    # --------------------------------------

    db_user = models.User(

        roll=user.roll,

        name=user.name,

        email=user.email,

        branch=user.branch,

        semester=user.semester,

        password=user.password

    )

    db.add(db_user)

    db.commit()

    db.refresh(db_user)

    return db_user


# ==========================================================
# LOGIN
# ==========================================================

def login(
    db: Session,
    credentials: schema.UserLogin
):

    student = (

        db.query(models.User)

        .filter(

            models.User.roll == credentials.roll

        )

        .first()

    )

    if not student:

        return None

    if student.password != credentials.password:

        return None

    return student


# ==========================================================
# GET STUDENT BY ROLL
# ==========================================================

def get_student(
    db: Session,
    roll: int
):

    return (

        db.query(models.User)

        .filter(

            models.User.roll == roll

        )

        .first()

    )


# ==========================================================
# GET STUDENT BY ID
# ==========================================================

def get_student_by_id(
    db: Session,
    student_id: int
):

    return (

        db.query(models.User)

        .filter(

            models.User.id == student_id

        )

        .first()

    )


# ==========================================================
# GET ALL STUDENTS
# ==========================================================

def get_students(
    db: Session
):

    return (

        db.query(models.User)

        .order_by(models.User.roll)

        .all()

    )
# ==========================================================
# UPDATE STUDENT
# ==========================================================

def update_student(
    db: Session,
    roll: int,
    student_update: schema.StudentUpdate
):

    student = get_student(db, roll)

    if not student:

        return None

    # --------------------------------------
    # Check Duplicate Email
    # --------------------------------------

    if student_update.email:

        existing_email = (

            db.query(models.User)

            .filter(
                models.User.email == student_update.email,
                models.User.roll != roll
            )

            .first()

        )

        if existing_email:

            raise ValueError(
                "Email already exists."
            )

    # --------------------------------------
    # Update Fields
    # --------------------------------------

    update_data = student_update.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():

        setattr(student, key, value)

    db.commit()

    db.refresh(student)

    return student


# ==========================================================
# DELETE STUDENT
# ==========================================================

def delete_student(
    db: Session,
    roll: int
):

    student = get_student(db, roll)

    if not student:

        return None

    db.delete(student)

    db.commit()

    return student


# ==========================================================
# CHECK EMAIL EXISTS
# ==========================================================

def email_exists(
    db: Session,
    email: str
):

    return (

        db.query(models.User)

        .filter(

            models.User.email == email

        )

        .first()

    )


# ==========================================================
# CHECK ROLL EXISTS
# ==========================================================

def roll_exists(
    db: Session,
    roll: int
):

    return (

        db.query(models.User)

        .filter(

            models.User.roll == roll

        )

        .first()

    )
# ==========================================================
# ADD COURSE
# ==========================================================

def add_course(
    db: Session,
    roll: int,
    course: schema.CourseCreate
):

    student = get_student(db, roll)

    if not student:

        return None

    db_course = models.Course(

        title=course.title,

        student_id=student.id

    )

    db.add(db_course)

    db.commit()

    db.refresh(db_course)

    return db_course


# ==========================================================
# GET ALL COURSES OF A STUDENT
# ==========================================================

def get_courses(
    db: Session,
    roll: int
):

    student = get_student(db, roll)

    if not student:

        return None

    return (

        db.query(models.Course)

        .filter(

            models.Course.student_id == student.id

        )

        .all()

    )


# ==========================================================
# GET COURSE BY ID
# ==========================================================

def get_course(
    db: Session,
    course_id: int
):

    return (

        db.query(models.Course)

        .filter(

            models.Course.id == course_id

        )

        .first()

    )


# ==========================================================
# UPDATE COURSE
# ==========================================================

def update_course(
    db: Session,
    course_id: int,
    course_update: schema.CourseUpdate
):

    course = get_course(db, course_id)

    if not course:

        return None

    course.title = course_update.title

    db.commit()

    db.refresh(course)

    return course


# ==========================================================
# DELETE COURSE
# ==========================================================

def delete_course(
    db: Session,
    course_id: int
):

    course = get_course(db, course_id)

    if not course:

        return None

    db.delete(course)

    db.commit()

    return course


# ==========================================================
# TOTAL STUDENTS
# ==========================================================

def total_students(
    db: Session
):

    return (

        db.query(models.User)

        .count()

    )


# ==========================================================
# TOTAL COURSES
# ==========================================================

def total_courses(
    db: Session
):

    return (

        db.query(models.Course)

        .count()

    )