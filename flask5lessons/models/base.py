from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


engine = create_engine("sqlite:///app.db", echo=True)


class Base(DeclarativeBase):
  ...


def create_db():
  Base.metadata.create_all(engine)


def drop_db():
  Base.metadata.drop_all(engine)

