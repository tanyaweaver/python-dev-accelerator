# -*- coding: utf-8 -*-
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    Unicode,
    ForeignKey,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgres://cewing:@localhost:5432/psycotest")

Base = declarative_base()


class Author(Base):
    __tablename__ = 'author'
    authorid = Column(Integer, primary_key=True)
    name = Column(Unicode(255))

    books = relationship('Book', back_populates="author")

    def __repr__(self):
        return '<Author: {}>'.format(self.name)


class Book(Base):
    __tablename__ = 'book'
    bookid = Column(Integer, primary_key=True)
    title = Column(Unicode(255))
    authorid = Column(Integer, ForeignKey('author.authorid'))

    author = relationship("Author", back_populates="books")

    def __repr__(self):
        return '<Book: {0} - by {1}>'.format(self.title, self.author.name)


# creating a session and binding the Base metadata:

Base.metadata.create_all(bind=engine)


SessionFactory = sessionmaker(bind=engine)
session = SessionFactory()

# interact with the session to read, create, update data:
session.query(Author).all()

new_author = Author(name="Ursula K. LeGuinn")
session.add(new_author)
