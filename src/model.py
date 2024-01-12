from sqlalchemy import Integer, Column, DateTime, String, Enum, ForeignKey
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class DatabaseMessage(Base):
    __tablename__ = 'messages'

    id = Column('id', Integer, autoincrement=True, primary_key=True)
    phone_number = Column('phone_number', String(40))
    message = Column('message', String(255))
