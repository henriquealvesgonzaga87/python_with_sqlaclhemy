from sqlalchemy.orm import declarative_base, relationship, Session
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, inspect, select, func, Float

Base = declarative_base()


class Client(Base):
    __tablename__ = "client_account"
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(String)
    tax_number = Column(String, unique=True)
    address = Column(String, unique=True)

    account = relationship("Account", back_populates="client", cascade="all, delete-orphan")

    def __repr__(self):
        return f"ID: {self.id} - Name: {self.name}"


class Account(Base):
    __tablename__ = "bank_account"
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    agency_number = Column(Integer, unique=True)
    account_number = Column(Integer, autoincrement=True, unique=True)
    id_client = Column(Integer, ForeignKey("client_account.id"), unique=True, nullable=False)
    bank_balance = Column(Float, unique=True)

    client = relationship("Client", back_populates="account")

    def __repr__(self):
        return f"id: {self.id} - agency: {self.agency_number} - account number: {self.account_number}"


engine = create_engine("sqlite://")

Base.metadata.create_all(engine)

inspect_engine = inspect(engine)

with Session(engine) as session:

    client1 = Client(
        name="Client01",
        tax_number="01010101",
        address="client01@mail.com",
        account=[Account(
            agency_number="01",
            account_number="0001",
            bank_balance="10"
        )]
    )

    session.add_all([client1])

    session.commit()
