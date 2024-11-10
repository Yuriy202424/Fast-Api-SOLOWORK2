from sqlalchemy.orm import sessionmaker, Mapped, mapped_column, DeclarativeBase
from sqlalchemy import create_engine


# ENGINE с большой буквы в первую очередь не помоту что это константа а потому что общепринятый синтаксис(и хорошая практика)
ENGINE = create_engine('sqlite:///my_db.db', echo=True)
SESSION = sessionmaker(bind=ENGINE)


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)


def up():
    Base.metadata.create_all(ENGINE)

def drop():
    Base.metadata.create_all(ENGINE)

def migrate():
    up()
    drop()
    
from .models import Data
migrate()