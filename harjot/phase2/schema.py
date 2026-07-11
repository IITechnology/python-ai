from pydantic import BaseModel
from typing import List,Optional
 
class StudentCreate(BaseModel):
    roll: int
    name: str

class CourseCreate(BaseModel):
    title: str

class CourseResponse(CourseCreate):
    id: int
    student_roll: int
    class Config:
        orm_mode=True

class StudentResponse(StudentCreate):
    courses: List[CourseResponse]=[]
    class Config:
        orm_mode=True
