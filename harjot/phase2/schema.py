from typing import List, Optional

from pydantic import BaseModel, EmailStr


# ==========================================================
# COURSE SCHEMAS
# ==========================================================

class CourseBase(BaseModel):
    title: str


class CourseCreate(CourseBase):
    pass


class CourseUpdate(BaseModel):
    title: str


class CourseResponse(CourseBase):
    id: int

    class Config:
        from_attributes = True


# ==========================================================
# USER SCHEMAS
# ==========================================================

class UserSignup(BaseModel):

    roll: int

    name: str

    email: EmailStr

    branch: str

    semester: int

    password: str


class UserLogin(BaseModel):

    roll: int

    password: str


class StudentUpdate(BaseModel):

    name: Optional[str] = None

    email: Optional[EmailStr] = None

    branch: Optional[str] = None

    semester: Optional[int] = None


# ==========================================================
# RESPONSE SCHEMAS
# ==========================================================

class StudentResponse(BaseModel):

    id: int

    roll: int

    name: str

    email: EmailStr

    branch: str

    semester: int

    courses: List[CourseResponse] = []

    class Config:
        from_attributes = True


class LoginResponse(BaseModel):

    message: str

    student: StudentResponse