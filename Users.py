from DBHandler import DBHandler
from sqlalchemy import Column, Integer, String, Date, Text


class Users(DBHandler.Base):
    __tablename__ = 'users'
    username = Column(String(30),primary_key=True)
    email = Column(String(30))
    gender=Column(String(6))
    verification=Column(Integer)
    faceimage = Column(Text)

    def __repr__(self):
        return f"<User(username={self.name},email={self.email},faceimage={self.faceimage} )>"