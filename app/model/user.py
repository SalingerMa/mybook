# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, Boolean, Float
from werkzeug.security import generate_password_hash

from app.model.base import Base


class User(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=True)
    _password = Column('password', String(128), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    is_author = Column(Boolean, default=False)


    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

