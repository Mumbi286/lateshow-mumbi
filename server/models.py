from flask_sqlalchemy import SQLAlchemy


class Episode(db.Model):
    __tablename__ = 'episodes'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)

    appearances = db.relationship('Appearance', back_populates='episode', cascade='all, delete-orphan')
    guests = db.relationship('Guest', secondary='appearances', back_populates='episodes')

class Guest(db.Model):
    __tablename__ = 'guests'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    appearances = db.relationship('Appearance', back_populates='guest', cascade='all, delete-orphan')
    episodes = db.relationship('Episode', secondary='appearances', back_populates='guests')

class Appearance(db.Model):
    __tablename__ = 'appearances'
    id = db.Column(db.Integer, primary_key=True)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable=False)
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'), nullable=False)

    episode = db.relationship('Episode', back_populates='appearances')
    guest = db.relationship('Guest', back_populates='appearances')
