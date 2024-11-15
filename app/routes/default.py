from fastapi import HTTPException
from sqlalchemy import select
from app import app
from ..schemas import DataRows, ContentFiller
from ..db import SESSION, Data, Content


@app.get("/")
def index():
    return{"a":"Dildak"}


@app.post("/authentification/{user}/{password}")
def authentification(user : str, password : str):
    with SESSION.begin() as session:
        test = Data(user = user, password = password)
        session.add(test)


@app.post("/content/{content}")
def create_content(key: int, content : str):
    with SESSION.begin() as session:
        us = session.scalar(select(Data.user))
        if us == None:
            raise HTTPException(status_code=400, detail="You are not registered! You cant use this function")
        else:
            if len(str(key)) == 3:
                test = Content(key = key, content = content)
                session.add(test)
                return(test)
            else:
                raise HTTPException(status_code=400, detail="Key must be integer and only 3 digits")
        

@app.get("/get_content/{pincode}")
def get_content(pincode: int):
    with SESSION.begin() as session:
        if len(str(pincode)) == 3:
            content = session.scalar(select(Content).where(Content.key == pincode))
            if content:
                return {"id" : content.key, "content" : content.content}
            else:
                raise HTTPException(status_code=400, detail="Key is not found") 
        else:
            raise HTTPException(status_code=400, detail="Key must be integer and only 3 digits")
        

@app.post("/update/{pincode}/{content}")
def upd_content(pincode: int, content: str):
    with SESSION.begin() as session:
        if len(str(pincode)) == 3:
                upd = session.query(Content).filter(Content.key == pincode).first()
                if upd:
                    upd.content = content
                    session.commit
                    return {"message" : "Succesfully updated!!!"}
                else:
                    return {"message" : "Pincode(Key) not found!"}
        else:
            raise HTTPException(status_code=400, detail="Key must be integer and only 3 digits")
        

@app.delete("/delete/{pincode}")
def delete_content(pincode: int):
    with SESSION.begin() as session:
        if len(str(pincode)) == 3:
            del_content = session.scalar(select(Content).where(Content.key == pincode))
            if del_content:
                session.delete(del_content)
                return {"message" : "deleted!"}
            else:
                raise HTTPException(status_code=400, detail="Key is not found")
        else:
            raise HTTPException(status_code=400, detail="Key must be integer and only 3 digits")
        