from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Annotated
import models
from database import engine,SessionLocal
from sqlalchemy.orm import Session
#Creating an instance of FastApi
app = FastAPI()

#this creates all the tables in postgres
models.Base.metadata.create_all(bind=engine)

#creating structure of choices for the quiz application
class ChoiceBase(BaseModel):
    choice_text: str
    is_correct:bool

#creating structure of questions for the quiz
#the choices field will have the value which is are the instances of choiceBase
class QuestionBase(BaseModel):
    question_text:str
    choices: List[ChoiceBase]    

#making a connection with the database

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()    
#dependency injection
db_dependency = Annotated[Session,Depends(get_db)]