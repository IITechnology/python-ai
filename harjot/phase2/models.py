from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


# ==========================================================
# USER MODEL
# ==========================================================

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    roll = Column(Integer, unique=True, nullable=False, index=True)

    name = Column(String, nullable=False)

    email = Column(String, unique=True, nullable=False)

    branch = Column(String, nullable=False)

    semester = Column(Integer, nullable=False)

    password = Column(String, nullable=False)

    courses = relationship(
        "Course",
        back_populates="student",
        cascade="all, delete-orphan"
    )


# ==========================================================
# COURSE MODEL
# ==========================================================

class Course(Base):

    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)

    student_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    student = relationship(
        "User",
        back_populates="courses"
    )