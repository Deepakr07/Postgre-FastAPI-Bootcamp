from sqlalchemy import Boolean, Column, ForeignKey, Integer, String 
from database import Base

#creaing tables that is to be displayed in the database

#questions table
class Questions(Base):
    __tablename__ = 'questions'
    #id of each question will be an integer and it will be set as the primary key to uniquely identify the row
    id = Column(Integer,primary_key=True,index=True)
    question_text = Column(String, index=True)

#choices table
#here the question id is a foreign key which is referring to the primary key of the question table
class Choices(Base):

    __tablename__ = 'choices'

    id = Column(String,primary_key=True,index=True)
    choice_text = Column(String,index=True)
    is_correct = Column(Boolean,default=False)
    question_id = Column(Integer,ForeignKey("questions.id"))