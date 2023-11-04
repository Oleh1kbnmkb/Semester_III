from __future__ import annotations
from typing import List, Optional
from sqlalchemy import ForeignKey, String, Date, Time, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base
from flask_login import UserMixin

class User(Base, UserMixin):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    nickname: Mapped[Optional[str]] = mapped_column()
    email: Mapped[Optional[str]] = mapped_column()
    password: Mapped[Optional[str]] = mapped_column()


    def __str__(self) -> str:
        return f"User: {self.nickname}"

    def __repr__(self) -> str:
        return self.nickname.capitalize()