from pydantic import BaseModel



class DataRows(BaseModel):
    number: int
    password: str



class ContentFiller(BaseModel):
    content: str
