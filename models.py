from sqlalchemy import Boolean, Column, ForeignKey, Integer, String 
from database import Base

#creaing tables that is to be displayed in the database

class Questions(Base):
    __tablename__ = 'questions'
    #id of each question will be an integer and it will be set as the primary key to uniquely identify the row
    id = Column(Integer,primary_key=True,index=True)
    question_text = Column(String, index=True)