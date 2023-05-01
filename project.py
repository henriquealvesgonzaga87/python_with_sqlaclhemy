from sqlalchemy.orm import declarative_base, relationship, Session
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, inspect, select, func

Base = declarative_base()


class Client(Base):
    __tablename__ = "client_account"
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(String)
    tax_number = Column(String, unique=True)
    address = Column(String, unique=True)

    def __repr__(self):
        return f"ID: {self.id} - Name: {self.name}"
