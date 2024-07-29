from sqlalchemy.orm import Session
from models import Player, Team, PlayerRating, Match
from schemas import PlayerCreate, TeamCreate, PlayerRatingCreate, MatchCreate

# Team CRUD operations
def get_team(db: Session, team_id: int):
    return db.query(Team).filter(Team.id == team_id).first()

def get_teams(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Team).offset(skip).limit(limit).all()

def create_team(db: Session, team: TeamCreate):
    db_team = Team(id=team.id, name=team.name, region=team.region)
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team

# Player CRUD operations
def get_player(db: Session, player_id: int):
    return db.query(Player).filter(Player.id == player_id).first()

def get_players(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Player).offset(skip).limit(limit).all()

def create_player(db: Session, player: PlayerCreate):
    db_player = Player(id=player.id, name=player.name, position=player.position, club_team_id=player.club_team_id, international_team_id=player.international_team_id)
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player

# Match CRUD operations
def get_match(db: Session, match_id: int):
    return db.query(Match).filter(Match.id == match_id).first()

def create_match(db: Session, match: MatchCreate):
    db_match = Match(id=match.id, home_team_id=match.home_team_id, away_team_id=match.away_team_id, date=match.date, home_score=match.home_score, away_score=match.away_score)
    db.add(db_match)
    db.commit()
    db.refresh(db_match)
    return db_match

# PlayerRating CRUD operations
def get_player_rating(db: Session, player_rating_id: int):
    return db.query(PlayerRating).filter(PlayerRating.id == player_rating_id).first()

def get_ratings_by_id(db: Session, player_id:int):
    return db.query(PlayerRating).filter(PlayerRating.playerId == player_id).all()

def get_ratings_by_match(db: Session, match_id:int):
    return db.query(PlayerRating).filter(PlayerRating.matchId == match_id).all()

def create_player_rating(db: Session, player_rating: PlayerRatingCreate):
    db_player_rating = PlayerRating(id=player_rating.id, playerId=player_rating.player_id, matchId=player_rating.match_id, rating=player_rating.rating)
    db.add(db_player_rating)
    db.commit()
    db.refresh(db_player_rating)
    return db_player_rating
