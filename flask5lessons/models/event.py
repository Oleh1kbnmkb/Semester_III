from __future__ import annotations
from typing import List, Optional
from sqlalchemy import ForeignKey, String, Date, Time, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base
from .user import User


class Event(Base):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(primary_key=True,)
    date = Column("date", Date)
    time = Column("time", Time, nullable=True,)
    header: Mapped[str] = mapped_column(String(80))
    describe: Mapped[str] = mapped_column(String(240), nullable=True,)
    #user: Mapped[User] = relationship(back_populates="events")


    def __str__(self) -> str:
        return f"Event: {self.header}"

    def __repr__(self) -> str:
        return self.header.capitalize()
