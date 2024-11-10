from sqlalchemy.orm import Mapped
from .. import Base


class Data(Base):
    __tablename__ = "datas"
    
    number : Mapped[int]
    content : Mapped[str]
     