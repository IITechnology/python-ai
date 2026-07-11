from sqlalchemy import Column, Integer, String, ForeignKey, Float # type: ignore #ORM Db
from database import Base
from sqlalchemy.orm import relationship

class Student(Base):
    __tablename__="students"
    roll=Column(Integer, primary_key=True, index=True) #keyward argument, key: primary
    name=Column(String, nullable=False)
    courses=relationship("Course", back_populates="student")

class Course(Base):
    __tablename__="courses"
    id=Column(Integer, primary_key=True, index=True) #keyward argument, key: primary
    title=Column(String, index=True)
    student_roll=Column(Integer, ForeignKey("students.roll"))
    student=relationship("Student", back_populates="courses")

