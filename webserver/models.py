import os
import dotenv

from sqlalchemy import create_engine, Column, ForeignKey, Integer, String, Sequence, Float
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


dotenv.load_dotenv()

SQLITE_URL = os.getenv("SQLITE_URL")


engine = create_engine(
    url=SQLITE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


Database = declarative_base()


class Customer(Database):
    __tablename__ = "customers"

    id = Column(Integer, Sequence("customer_id"), primary_key=True, index=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)


class Reseller(Database):
    __tablename__ = "resellers"

    id = Column(Integer, Sequence("customer_id"), primary_key=True, index=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)

    relationship("Product", back_populates="owner")


class Product(Database):
    __tablename__ = "products"

    id = Column(Integer, Sequence("customer_id"), primary_key=True, index=True)
    price = Column(Float, nullable=False)
    reseller_id = Column(Integer, ForeignKey("resellers.id"))
