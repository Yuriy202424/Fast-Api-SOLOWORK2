from fastapi import HTTPException
from sqlalchemy import select
from app import app
from ..schemas import DataRows, ContentFiller
from ..db import SESSION, Data, Content


@app.get("/")
def index():
    return{"a":"Dildak"}


@app.post("/adding/{number}/{password}")
def adding(number : int, password : str):
    with SESSION.begin() as session:
        test = Data(number = number, password = password)
        pw = password
        session.add(test)


@app.post("/authentification/{content}")
def content(content : str):
    with SESSION.begin() as session:
        num = session.scalar(select(Data.number))
        if num == None:
            raise HTTPException(status_code=400, detail="You are not registered! You cant use this function")
        else:
            test = Content(content = content)
            session.add(test)
            return(test)
        