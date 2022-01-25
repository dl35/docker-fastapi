
import json, os
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from app.schemas import users as susers , activities as sactivities
from app.model import models
from app.crud import manage as crud
from typing import List

from app.model import models



router = APIRouter(
    prefix="/manage",
    tags=["manage"],
    responses={404: {"description": "Not found"}})

    
@router.get("/loadusers")
def loadusers(db: Session = Depends(get_db)):
    
   # get current directory
    current = os.getcwd()
    path =( os.path.join( current  ,"app/tools" ,"users.json"      )  )
    f = open( path )
    data = json.load(f)
    users: List[models.UserTable]=[]
    for d in data:
        userc=susers.User(
         id=d['id'],
         email=d['email'],
         nom=d['nom'],
         prenom=d['prenom'],
         passwd=d['passwd'],  
         adresse=d['adresse'],
         ville=d['ville'],
         cp=d['cp'],
         role=d['role'].upper()
        )
        
        user=models.UserTable(**userc.dict() )
        users.append( user )
        
    return crud.add_all_users(db, users )

@router.get("/loadactivities")
def loadactivities(db: Session = Depends(get_db)):
    # get current directory
    current = os.getcwd()
    path =( os.path.join( current  ,"app/tools" ,"activities.json"      )  )
    f = open( path )
    data = json.load(f)
    activities: List[models.ActivitiesTable]=[]
    for d in data:
        #if d['desc']:

        act=sactivities.ActivitiesCreate(
         id_user=d['id_user'],
         type=d['type'],
         dist=d['dist'],
         desc=d['desc'],
         date=d['date']
        )
        at=models.ActivitiesTable(**act.dict() )

        activities.append( at )
    return crud.add_all_activities(db, activities )