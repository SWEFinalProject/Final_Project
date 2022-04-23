"""This file includes models for Postgresql DB"""
# pylint: disable=E0401, R0903

from database import db


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
    chatroom_id = db.Column(db.String(30), db.ForeignKey("chatroom.id"))

    def __repr__(self):
        return f"{self.gsu_id}"
