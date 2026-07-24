from typing import List, Optional

from pydantic import BaseModel, ConfigDict


# ==========================================================
# AUTHENTICATION
# ==========================================================

class SignupCreate(BaseModel):
    roll: int
    password: str


class UserResponse(BaseModel):
    id: int
    roll: int

    model_config = ConfigDict(from_attributes=True)


# ==========================================================
# COURSE
# ==========================================================

class CourseCreate(BaseModel):
    title: str


class CourseResponse(BaseModel):
    id: int
    title: str

    model_config = ConfigDict(from_attributes=True)


# ==========================================================
# CREATE STUDENT PROFILE
# ==========================================================

class StudentCreate(BaseModel):
    roll: int
    name: str
    email: Optional[str] = None
    branch: Optional[str] = None
    semester: Optional[int] = None


# ==========================================================
# UPDATE STUDENT PROFILE
# ==========================================================

class StudentUpdate(BaseModel):
    email: Optional[str] = None
    branch: Optional[str] = None
    semester: Optional[int] = None


# ==========================================================
# STUDENT RESPONSE
# ==========================================================

class StudentResponse(BaseModel):
    id: int
    roll: int
    name: str
    email: Optional[str]
    branch: Optional[str]
    semester: Optional[int]

    courses: List[CourseResponse] = []

    model_config = ConfigDict(from_attributes=True)