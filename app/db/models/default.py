from sqlalchemy.orm import Mapped
from .. import Base



class Data(Base):
    __tablename__ = "datas"
    
    number : Mapped[int]
    password : Mapped[str]
     


class Content(Base):
    __tablename__ = "contents"

    content : Mapped[int]