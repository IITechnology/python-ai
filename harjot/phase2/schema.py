from pydantic import BaseModel,Field
from typing import List


# ======================================================
# AUTHENTICATION
# ======================================================

class SignupCreate(BaseModel):
    roll: int
    password: str


class UserResponse(BaseModel):
    id: int
    roll: int

    class Config:
        from_attributes = True



# ======================================================
# STUDENT
# ======================================================

class StudentCreate(BaseModel):
    roll: int
    name: str


class CourseResponse(BaseModel):
    id: int
    title: str
    student_roll: int

    class Config:
        from_attributes = True

class StudentResponse(BaseModel):
    roll: int
    name: str
    courses: list[CourseResponse] = []

    class Config:
        from_attributes = True


# ======================================================
# COURSE
# ======================================================

class CourseCreate(BaseModel):
    title: str




# ======================================================
# STUDENT WITH COURSES (for dashboard)
# ======================================================

class StudentWithCourses(BaseModel):
    roll: int
    name: str
    courses: List[CourseResponse] = Field(default_factory=list)

    class Config:
        from_attributes = True