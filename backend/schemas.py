from pydantic import BaseModel
from typing import List
from datetime import date

# Team Schemas
class TeamBase(BaseModel):
    name: str

class TeamCreate(TeamBase):
    id: int

class Team(TeamBase):
    id: int

    class Config:
        orm_mode = True

# Player Schemas
class PlayerBase(BaseModel):
    name: str

class PlayerCreate(PlayerBase):
    id: int

class Player(PlayerBase):
    id: int

    class Config:
        orm_mode = True

# PlayerRating Schemas
class PlayerRatingBase(BaseModel):
    player_id: int
    match_id: int
    rating: float

class PlayerRatingCreate(PlayerRatingBase):
    id: int

class PlayerRating(PlayerRatingBase):
    id: int

    class Config:
        orm_mode = True

# match Schemas
class MatchBase(BaseModel):
    home_team_id: int
    away_team_id: int
    date: date
    home_score: int
    away_score: int

class MatchCreate(MatchBase):
    id: int

class Match(MatchBase):
    id: int
    home_team: Team
    away_team: Team

    class Config:
        orm_mode = True