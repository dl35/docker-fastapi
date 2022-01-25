from typing import List
from sqlalchemy.orm import Session
from app.model.models import ActivitiesTable
from app.schemas import activities as schema
from . import users as crud
from app.exceptions import exceptions



def get(db: Session, act_id:int):
    
    
    u = db.query(ActivitiesTable).filter( ActivitiesTable.id == act_id).first()
    if u is None:
        raise exceptions.ActivitiesNotFoundError
    return u    
    
def add(db: Session, act: schema.ActivitiesCreate):
    try:
      crud.get(db,user_id=act.id_user)
    except exceptions.UserException: 
        raise 
  
    db_act = ActivitiesTable( **act.dict() )
    db.add( db_act )
    db.commit()
    db.refresh(db_act)
    return db_act

def update(db: Session, act_id:int, activities: schema.ActivitiesCreate):
    a = get(db, act_id = act_id)
    if a :
        a.date = activities.date
        a.dist = activities.dist
        a.type = activities.type
        a.desc = activities.desc
               

        db.commit()
        db.refresh(a)
       
    else :
        raise exceptions.ActivitiesNotFoundError
    return a

def delete(db: Session, act_id:int):
    try:
     u = get(db, act_id = act_id)
    except exceptions.ActivitiesException: 
        raise 
         
    db.delete(u)
    db.commit()
    
    return


def get_all_id(db: Session, id_user:int, limit: int, offset: int) -> List[ActivitiesTable]:
    try:
        u = db.query(ActivitiesTable).filter( ActivitiesTable.id_user == id_user ).order_by( ActivitiesTable.date.desc()).offset(offset).limit(limit).all()
        if u is None:
            raise exceptions.ActivitiesNotFoundError
    except Exception as e:
        raise e    
    return u 

def get_all(db: Session, limit: int, offset: int) -> List[ActivitiesTable]:
    return db.query(ActivitiesTable).offset(offset).limit(limit).all()
