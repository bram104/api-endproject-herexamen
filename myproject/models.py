from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from database import Base


class usernames(Base):
    __tablename__ = "usernames"

    leagueId = Column(Integer, primary_key=True, index=True)
    in_game_name = Column(String, unique=True, index=True)
    email = Column(String, default=True)
    player_region = Column(String, unique=True)
    birthday = Column(String, index=True)
    password = Column(String, index=True)



class gamemodes(Base):
    __tablename__ = "gamemodes"

    gamemodeId = Column(Integer, primary_key=True, index=True)
    summoners_rift = Column(Boolean, index=True)
    aram = Column(Boolean)
    teamfight_tactics = Column(Boolean)
    arena = Column(Boolean)



class champions(Base):
    __tablename__ = "champions"

    championId = Column(Integer, primary_key=True, index=True)
    champion_name = Column(String, index=True)
    champion_skins = Column(String)
    release_date = Column(Integer)
    price = Column(Integer)
    champion_region = Column(String)
    difficulty = Column(Integer)








