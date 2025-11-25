from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    firstname: Mapped[str] = mapped_column(String(120), nullable=False)
    lastname: Mapped[str] = mapped_column(String(120), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "firstname": self.firstname,
            "lastname": self.lastname,
            # do not serialize the password, its a security breach
        }
    
class Comment(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    commenttext: Mapped[str] = mapped_column(String(120), nullable=False)
    author_id: Mapped[str] = mapped_column(ForeignKey('user.id'), nullable=False)
    post_id: Mapped[str] = mapped_column(String(120), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "commenttext": self.commenttext,
            "post_id": self.post_id,
            # do not serialize the password, its a security breach
        }