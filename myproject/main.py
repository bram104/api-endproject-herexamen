from fastapi import Depends, FastAPI, HTTPException, Path
from sqlalchemy.orm import Session

import os
import crud
import models
import schemas
import auth
from database import SessionLocal, engine

print("We are in the main.......")
if not os.path.exists('.\sqlitedb'):
    print("Making folder.......")
    os.makedirs('.\sqlitedb')

print("Creating tables.......")
models.Base.metadata.create_all(bind=engine)
print("Tables created.......")

app = FastAPI()

# Dependency
def get_database():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/post/username/", response_model=schemas.username)
def create_username(username: schemas.usernameCreate, db: Session = Depends(get_database)):
    get_user_by_ign = crud.get_user_by_ign(db, in_game_name=username.in_game_name)
    get_user_by_email = crud.get_username_by_email(db, email=username.email)
    if get_user_by_email:
        raise HTTPException(status_code=400, detail="Email already registered")
    elif get_user_by_ign:
        raise HTTPException(status_code=400, detail="User already exist")
    return crud.create_usernames(db=db, username=username)


@app.put("/username/put/{leagueId}", response_model=schemas.username)
async def update_usernames(username: schemas.usernameCreate, db: Session = Depends(get_database),
    leagueId: int = Path(ge=0, le=30)):
    return crud.update_usernames(db=db, username=username, leagueId=leagueId)


@app.post("/post/champion/", response_model=schemas.champion)
def create_champion(champion: schemas.championCreate, db: Session = Depends(get_database)):
    return crud.create_champion(db, champion=champion)


@app.delete("/delete/champion/{championId}", response_model=schemas.champion)
async def delete_champion(championId: int = Path(ge=0, le=30), db: Session = Depends(get_database)):
    deleted_champion = crud.get_champion_by_Id(db, championId=championId)
    if deleted_champion is None:
        raise HTTPException(status_code=404, detail="Champion not found")
    crud.delete_champion(db=db, championId=championId)
    return deleted_champion

@app.get("/usernames/all/", response_model=list[schemas.username])
def read_users(db: Session = Depends(get_database)):
    return crud.get_all_usernames(db=db)


@app.get("/username/{leagueId}", response_model=schemas.username)
def read_user(leagueId: int, db: Session = Depends(get_database)):
    username_by_id = crud.get_username_by_Id(db, leagueId=leagueId)
    if username_by_id is None:
        raise HTTPException(status_code=404, detail="User not found")
    return username_by_id


@app.get("/gamemode/{gamemodeId}", response_model=schemas.gamemode)
def get_gamemode(gamemodeId: int,db: Session = Depends(get_database)):
    gamemodeId = crud.get_gamemode_by_Id(db=db, gamemodeId=gamemodeId)
    return gamemodeId

