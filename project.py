from sqlalchemy.orm import declarative_base, relationship, Session
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, inspect, select, func, Float

Base = declarative_base()


class Client(Base):
    __tablename__ = "client_account"
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(String)
    tax_number = Column(String, unique=True)
    address = Column(String, unique=True)

    def __repr__(self):
        return f"ID: {self.id} - Name: {self.name}"


class Account(Base):
    __tablename__ = "bank_account"
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    agency_number = Column(String, unique=True)
    account_number = Column(Integer, autoincrement=True, unique=True)
    id_client = Column(Integer, ForeignKey("client_account.id"), unique=True, nullable=False)
    bank_balance = Column(Float, unique=True)

    def __repr__(self):
        return f"id: {self.id} - agency: {self.agency_number} - account number: {self.account_number}"
