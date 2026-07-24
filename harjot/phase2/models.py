from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


# ==========================================================
# USER
# ==========================================================

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    roll = Column(Integer, unique=True, nullable=False, index=True)

    hashed_password = Column(String, nullable=False)

    student = relationship(
        "Student",
        back_populates="user",
        uselist=False,
        cascade="all, delete"
    )


# ==========================================================
# STUDENT
# ==========================================================

class Student(Base):

    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        unique=True,
        nullable=False
    )

    roll = Column(
        Integer,
        unique=True,
        nullable=False,
        index=True
    )

    name = Column(String, nullable=False)

    email = Column(String, nullable=True)

    branch = Column(String, nullable=True)

    semester = Column(Integer, nullable=True)

    user = relationship(
        "User",
        back_populates="student"
    )

    courses = relationship(
        "Course",
        back_populates="student",
        cascade="all, delete-orphan"
    )


# ==========================================================
# COURSE
# ==========================================================

class Course(Base):

    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)

    student_id = Column(
        Integer,
        ForeignKey("students.id"),
        nullable=False
    )

    student = relationship(
        "Student",
        back_populates="courses"
    )