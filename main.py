from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Annotated

#Creating an instance of FastApi
app = FastAPI()

#creating structure of choices for the quiz application
class ChoiceBase(BaseModel):
    choice_text: str
    is_correct:bool

#creating structure of questions for the quiz
#the choices field will have the value which is are the instances of choiseBase
class QuestionBase(BaseModel):
    question_text:str
    choices: List[ChoiceBase]    