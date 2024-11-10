from pydantic import BaseModel


class DataRows(BaseModel):
    id: int
    number: int
    content: str

