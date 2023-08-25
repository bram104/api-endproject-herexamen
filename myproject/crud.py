from sqlalchemy.orm import Session
from passlib.hash import argon2

import models
import schemas
import auth


def get_user_by_birthday(db: Session, birthday: int):
    return db.query(models.usernames).filter(models.usernames.birthday == birthday).first()

def get_user_by_ign(db: Session, in_game_name: str):
    return db.query(models.usernames).filter(models.usernames.in_game_name == in_game_name).first()

def get_all_usernames(db: Session):
    return db.query(models.usernames).all()

def get_username_by_email(db: Session, email: str):
    return db.query(models.usernames).filter(models.usernames.email == email).first()

def get_username_by_Id(db: Session, leagueId: int):
    return db.query(models.usernames).filter(models.usernames.leagueId == leagueId).first()

def get_gamemode_by_Id(db: Session, gamemodeId: int):
    return db.query(models.gamemodes).filter(models.gamemodes.gamemodeId == gamemodeId).first()

def get_champion_by_Id(db: Session, championId: int):
    return db.query(models.champions).filter(models.champions.championId == championId).first()

def get_all_champions(db: Session):
    return db.query(models.champions).all()


def create_usernames(db: Session, username: schemas.usernameCreate):
    hashed_password = auth.get_password_hash(username.password)
    db_usernames = models.usernames(in_game_name=username.in_game_name, email=username.email, player_region=username.player_region,
                               password=hashed_password, birthday=username.birthday)
    db.add(db_usernames)
    db.commit()
    db.refresh(db_usernames)
    return db_usernames


def update_usernames(db: Session, leagueId: int, username: schemas.usernameCreate):
    db_username = db.query(models.usernames).filter(models.usernames.leagueId == leagueId).first()
    db_username.in_game_name = username.in_game_name
    db_username.email = username.email
    db_username.player_region = username.player_region
    db_username.birthday = username.birthday
    db_username.password = username.password
    db.commit()
    db.refresh(db_username)
    return db_username


def delete_username(db: Session, leagueId: int):
    print(leagueId)
    db_delete = db.query(models.usernames).filter(models.usernames.leagueId == leagueId).first()
    db.delete(db_delete)
    db.commit()
    return None


def delete_champion(db: Session, championId: int):
    print(championId)
    db_delete = db.query(models.champions).filter(models.champions.championId == championId).first()
    db.delete(db_delete)
    db.commit()
    return None


def create_champion(db: Session, champion: schemas.championCreate):
    champions_list = get_all_champions(db)
    db_champion = models.champions(championId=len(champions_list) +1, champion_name=champion.champion_name, champion_skins=champion.champion_skins,
                                release_date=champion.release_date, price=champion.price, champion_region=champion.champion_region,
                                difficulty=champion.difficulty)
    db.add(db_champion)
    db.commit()
    db.refresh(db_champion)
    return db_champion
