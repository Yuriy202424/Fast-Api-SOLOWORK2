from app import app
from ..schemas import DataRows
from ..db import SESSION, Data


@app.get("/")
def index():
    return{"a":"Dildak"}


@app.post("/adding")
def adding(data: DataRows):
    with SESSION.begin() as session:
        test = Data(**data.model_dump())
        session.add(test)
