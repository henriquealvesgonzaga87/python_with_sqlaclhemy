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
        name="client",
        tax_number="01010101",
        address="client01@mail.com",
        account=[Account(
            agency_number="01",
            account_number="0001",
            bank_balance="10"
        )]
    )

    client2 = Client(
        name="client02",
        tax_number="02020202",
        address="client02@mail.com",
        account=[Account(
            agency_number="02",
            account_number="0002",
            bank_balance="20"
        )]
    )

    session.add_all([client1, client2])

    session.commit()

statment_client = select(Client).where(Client.name.in_(['client', 'client02']))
print("Showing registered clients")
for client in session.scalars(statment_client):
    print(client)
print()

statment_account = select(Account).where(Account.id_client.in_([1, 2]))
print("Showing registered accounts")
for account in session.scalars(statment_account):
    print(account)
print()

sorted_statement = select(Client).order_by(Client.id.desc())
print("Showing the results in a sorted way")
for result in session.scalars(sorted_statement):
    print(result)
print()

join_statement = select(Client.name, Client.tax_number, Account.agency_number, Account.account_number,
                        Account.bank_balance).join_from(Client, Account)
for result in session.scalars(join_statement):
    print(result)
print()

connection = engine.connect()
results = connection.execute(join_statement).fetchall()
print("executing the statment from the connection")
for result in results:
    print(result)
print()

count_statement = select(func.count('*')).select_from(Client)
print("Showing the instances from Client")
for result in session.scalars(count_statement):
    print(result)
