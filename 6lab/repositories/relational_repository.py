from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)

class Ad(Base):
    __tablename__ = 'ads'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))
    date_id = Column(Integer, ForeignKey('dates.id'))
    user = relationship("User")
    category = relationship("Category")
    date = relationship("Date")

class Date(Base):
    __tablename__ = 'dates'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    ad_id = Column(Integer, ForeignKey('ads.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    content = Column(String)
    ad = relationship("Ad")
    user = relationship("User")

class RelationalRepository:
    def __init__(self, database_url='sqlite:///ads_service.db'):
        self.engine = create_engine(database_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def add_user(self, user: User):
        session = self.Session()
        session.add(user)
        session.commit()
        session.close()

    def get_user(self, user_id: int) -> User:
        session = self.Session()
        user = session.query(User).filter_by(id=user_id).first()
        session.close()
        return user

    def add_ad(self, ad: Ad):
        session = self.Session()
        session.add(ad)
        session.commit()
        session.close()

    def get_ad(self, ad_id: int) -> Ad:
        session = self.Session()
        ad = session.query(Ad).filter_by(id=ad_id).first()
        session.close()
        return ad

    def add_date(self, date: Date):
        session = self.Session()
        session.add(date)
        session.commit()
        session.close()

    def get_date(self, date_id: int) -> Date:
        session = self.Session()
        date = session.query(Date).filter_by(id=date_id).first()
        session.close()
        return date

    def add_category(self, category: Category):
        session = self.Session()
        session.add(category)
        session.commit()
        session.close()

    def get_category(self, category_id: int) -> Category:
        session = self.Session()
        category = session.query(Category).filter_by(id=category_id).first()
        session.close()
        return category

    def add_question(self, question: Question):
        session = self.Session()
        session.add(question)
        session.commit()
        session.close()

    def get_question(self, question_id: int) -> Question:
        session = self.Session()
        question = session.query(Question).filter_by(id=question_id).first()
        session.close()
        return question
