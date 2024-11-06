#inorder to connect to the database and perform database operations such as CRUD
from sqlalchemy import create_engine

#The sessionmaker function in SQLAlchemy is a factory for creating session objects, which are used to interact with the database.
from sqlalchemy.orm import sessionmaker

#used for creating a base class for defining ORM models in sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE = 'postgresql://postgres:deepak@localhost:5432/QuizApplication'

#used to create a new sqlalchemy engine instance to connect to the database 
engine = create_engine(URL_DATABASE)

#sessionmaker function is used to create a new session instance

#Session in SQLAlchemy is used to manage the operations for interacting with the database

#autocommit=False - changes made in the session will not be commited to the database until explicitly called with session.commit()

#autoflush = False - disables automatic flushing of changes to the database before queries are executed

#binds the session to the engine created earlier, ensuring that the session is connected to the correct database
SessionLocal = sessionmaker(autocommit=False, autoflush=False,  bind=engine)