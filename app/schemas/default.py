from pydantic import BaseModel



class DataRows(BaseModel):
    user: str
    password: str



class ContentFiller(BaseModel):
    key: int
    content: str
