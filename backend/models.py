from sqlalchemy import Column, Integer, String, ForeignKey, Float, Date, Boolean
from sqlalchemy.orm import relationship
from database import Base

class Team(Base):
    __tablename__ = 'teams'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)


class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)


class PlayerRating(Base):
    __tablename__ = 'player_ratings'

    id = Column(Integer, primary_key=True, index=True)
    playerId = Column(Integer, ForeignKey('players.id'))
    matchId = Column(Integer, ForeignKey('matches.id'))
    rating = Column(Float)

class Match(Base):
    __tablename__ = 'matches'

    id = Column(Integer, primary_key=True, index=True)
    homeScore = Column(Integer)
    awayScore = Column(Integer)
    date = Column(Date)
    homeId = Column(Integer, ForeignKey('teams.id'))
    awayId = Column(Integer, ForeignKey('teams.id'))

    home = relationship("Team", foreign_keys=[homeId])
    away = relationship("Team", foreign_keys=[awayId])
