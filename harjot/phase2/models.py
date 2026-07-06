from sqlalchemy import Column, Integer, String, Float #ORM Db
from database import Base

class StudentModel(Base):
    __tablename__="students"
    rollnumber=Column(Integer, primary_key=True, index=True) #keyward argument, key: primary
    name=Column(String, nullable=False)
    marks=Column(Float, nullable=True)

    def __repr__(self):  #repr is a representation, which automatically to call inbuilt method and always use string format. it always return a valu and its ia string
        return f"<Student (roll={self.rollnumber},name='{self.name}')>"/n