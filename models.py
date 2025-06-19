from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import bcrypt
from datetime import datetime
import json

# Create SQLite database
engine = create_engine('sqlite:///users.db')
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    receipts = relationship('Receipt', back_populates='user')
    budgets = relationship('Budget', back_populates='user')
    
    def set_password(self, password):
        salt = bcrypt.gensalt()
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')
    
    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))

class Receipt(Base):
    __tablename__ = 'receipts'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    date = Column(DateTime, nullable=False)
    vendor = Column(String, nullable=False)
    total = Column(Float, nullable=False)
    items = Column(Text, nullable=False)  # Store as JSON string
    categories = Column(Text, nullable=True)  # Store as JSON string
    created_at = Column(DateTime, default=datetime.utcnow)
    user = relationship('User', back_populates='receipts')

class Budget(Base):
    __tablename__ = 'budgets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    category = Column(String, nullable=False)
    month = Column(String, nullable=False)  # e.g., '2024-06'
    amount = Column(Float, nullable=False)
    user = relationship('User', back_populates='budgets')

# Create tables
Base.metadata.create_all(engine)

# Create session factory
Session = sessionmaker(bind=engine) 