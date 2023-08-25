from pydantic import BaseModel


class usernameBase(BaseModel):
    in_game_name: str
    email: str
    player_region: str
    birthday: str



class username(usernameBase):
    leagueId: int

    class Config:
        orm_mode = True


class usernameCreate(usernameBase):
    password: str | None = "Invalid"


class gamemodeBase(BaseModel):
    summoners_rift: bool
    aram: bool
    teamfight_tactics: bool
    arena: bool


class gamemode(gamemodeBase):
    gamemodeId: int

    class Config:
        orm_mode = True


class gamemodeCreate(gamemodeBase):
    pass


class championBase(BaseModel):
    championId: int
    champion_name: str
    champion_skins: str
    release_date: int
    price: int
    champion_region: str
    difficulty: int


class champion(championBase):

    class Config:
        orm_mode = True


class championCreate(championBase):
    pass

