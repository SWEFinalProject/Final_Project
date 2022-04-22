"""This file includes models for Postgresql DB"""
# pylint: disable=E0401, R0903

from flask_login import UserMixin
from database import db

chat_table = db.Table(
    # Table combining many to many relationship with reviews table
    "chat_table",
    db.Column("ct_id", db.Integer, db.ForeignKey("ct.id"), primary_key=True),
    db.Column("user_id", db.String(30), db.ForeignKey("user.gsu_id"), primary_key=True),
    db.Column(
        "chatroom_id", db.Integer, db.ForeignKey("chatroom.id"), primary_key=True
    ),
)


class Users(UserMixin, db.Model):
    """Defines each user of program, child of one-to-many relationship with chatrooms"""

    __tablename__ = "user"
    __table_args__ = {"extend_existing": True}
    id = db.Column(db.Integer, unique=True)
    gsu_id = db.Column(db.String(30), unique=True, primary_key=True, nullable=False)
    f_name = db.Column(db.String(30), unique=False, nullable=False)
    l_name = db.Column(db.String(50), unique=False, nullable=False)
    level = db.Column(db.String(20), unique=False, nullable=False)
    primary_major = db.Column(
        db.String(30), unique=False, nullable=False, default="undecided"
    )
    alt_email = db.Column(db.String(120), unique=False, nullable=True)
    phone = db.Column(db.String(20), unique=False, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    chatroom_id = db.Column(db.String(30), db.ForeignKey("user.gsu_id"))
    """chat_table = db.relationship(
        "Ct",
        secondary="chat_table",
        lazy="subquery",
        backref=db.backref("users", lazy=True),
    )"""

    def __repr__(self):
        return f"{self.gsu_id}"


class Restaurant(db.Model):
    __tablename__ = "restaurant"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    address = db.Column(db.String(80), unique=False, nullable=False)
    rating = db.Column(db.Float, default=0)
    price = db.Column(db.Integer)
    # image = db.Column(db.String(500), unique=True, nullable=False)

    def __repr__(self):
        return f"{self.name}"


class Chatroom(db.Model):
    """Model for chatrooms, parent of one-to-many relationship for users"""

    __tablename__ = "chatroom"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    # members = db.relationship("Users", backref="chatrooms", lazy=True)
    chat_table = db.relationship(
        "Ct",
        secondary="chat_table",
        lazy="subquery",
        backref=db.backref("chatrooms", lazy=True),
    )

    def __repr__(self):
        return f"{self.name}"


class Ct(db.Model):
    # __tablename__ = 'Ct'
    # __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)