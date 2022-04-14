from sqlalchemy import create_engine, Integer, Boolean, String, \
    Column, DateTime, ForeignKey

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database
from datetime import datetime

engine = create_engine('sqlite:///newspaper.db', echo=True)
if not database_exists(engine.url):
    create_database(engine.url)
engine.connect()

Base = declarative_base()


class Redactions(Base):
    __tablename__ = 'redactions'
    id = Column(Integer(), primary_key=True)
    redactor_id = Column(Integer(), ForeignKey('redactors.id'))
    address = Column(String(255), nullable=False)


class Redactors(Base):
    __tablename__ = 'redactors'
    id = Column(Integer(), primary_key=True)
    first_name = Column(String(255), nullable=False)
    second_name = Column(String(255), nullable=False)


class Employer(Base):
    __tablename__ = 'employer'
    id = Column(Integer(), primary_key=True)
    first_name = Column(String(255), nullable=False)
    second_name = Column(String(255), nullable=False)


class RedactionsEmployers(Base):
    __tablename__ = 'redactions_employers'
    id = Column(Integer(), primary_key=True)
    emploee_id = Column(Integer(), ForeignKey('employer.id'))
    redaction_id = Column(Integer(), ForeignKey('redactions.id'))



class Articles(Base):
    __tablename__ = 'articles'
    id = Column(Integer(), primary_key=True)
    emploee_id = Column(Integer(), ForeignKey('employer.id'))
    status_id = Column(Boolean())

class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer(), primary_key=True)
    first_name = Column(String(255), nullable=False)
    second_name = Column(String(255), nullable=False)

class AuthorArticles(Base):
    __tablename__ = 'author_articles'
    id = Column(Integer(), primary_key=True)
    article_id = Column(Integer(), ForeignKey('articles.id'))
    author_id = Column(Integer(), ForeignKey('author.id'))




if __name__ == '__main__':
    Base.metadata.create_all(engine)
