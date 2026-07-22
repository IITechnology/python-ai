from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


# ======================================================
# USER (Authentication)
# ======================================================

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    roll = Column(Integer, unique=True, index=True, nullable=False)

    hashed_password = Column(String, nullable=False)



# ======================================================
# STUDENT (Profile)
# ======================================================

class Student(Base):

    __tablename__ = "students"

    roll = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    courses = relationship(
        "Course",
        back_populates="student",
        cascade="all, delete",
        lazy="joined"
    )



# ======================================================
# COURSE
# ======================================================

class Course(Base):

    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, index=True, nullable=False)

    student_roll = Column(
        Integer,
        ForeignKey("students.roll", ondelete="CASCADE")
    )

    student = relationship(
        "Student",
        back_populates="courses"
    )