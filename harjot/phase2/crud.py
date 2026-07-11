from sqlalchemy.orm import Session
import models, schema

def get_student(db:Session,roll:int):
    return db.query(models.Student).filter(models.Student.roll==roll).first()

def get_students(db:Session,skip:int=0,limit:int=10):
    #return db.query(models.Student).offset(skip).limit(limit).all()
    return db.query(models.Student).all()


def create_students(db:Session,student:schema.StudentCreate):
    db_student=models.Student(roll=student.roll,name=student.name)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student