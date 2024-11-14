from sqlalchemy.orm import Mapped
from .. import Base



class Data(Base):
    __tablename__ = "datas"
    
    user : Mapped[str]
    password : Mapped[str]
     


class Content(Base):
    __tablename__ = "contents"

    key: Mapped[int]
    content : Mapped[str]