# app/routes.py

from fastapi import APIRouter, Depends, HTTPException
from schemas import Team, Player, PlayerRating, Match
from sqlalchemy.orm import Session
from database import get_db
from crud import get_teams, get_players, get_player_rating, get_ratings_by_id, get_ratings_by_match

router = APIRouter()
@router.get("/teams", response_model=list[Team])
def read_teams(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    teams = get_teams(db, skip=skip, limit=limit)
    return teams

@router.get("/players", response_model=list[Player])
def read_players(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    players = get_players(db, skip=skip, limit=limit)
    return players

@router.get("/player_ratings/{player_id}", response_model=list[PlayerRating])
def read_player_ratings(player_id: int, db: Session = Depends(get_db)):
    player_ratings = get_ratings_by_id(db, player_id)
    return player_ratings