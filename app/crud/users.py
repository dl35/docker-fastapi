from typing import List
from sqlalchemy.orm import Session
from app.model.models import UserTable
from app.schemas import users as schema
from app.exceptions import exceptions



def get_by_email(db: Session, email:str):
    u = db.query(UserTable).filter( email == UserTable.email ).first()
       
    return u  

def get(db: Session, user_id:int):
    u = db.query(UserTable).filter( UserTable.id == user_id).first()
    if u is None:
        raise exceptions.UserNotFoundError
    return u    
    
def add(db: Session, user: schema.UserCreate):
    u = get_by_email(db, email=user.email)
    if u :
        raise exceptions.UserExistError
    db_user = UserTable( **user.dict() )
    db.add( db_user )
    db.commit()
    db.refresh(db_user)
    return db_user

def update(db: Session, user_id:int, user: schema.UserCreate):
    u = get(db, user_id = user_id)
    if u :
              
        u.nom = user.nom
        u.prenom = user.prenom
        u.email = user.email
        u.passwd = user.passwd
        u.adresse = user.adresse
        u.ville = user.ville
        u.cp = user.cp
        u.role = user.role
               
        try:
            db.commit()
            db.refresh(u)
        except:
            db.rollback()
            raise exceptions.UserExistError

    else :
        raise exceptions.UserNotFoundError
    return u

def delete(db: Session, user_id:int):
    u = get(db, user_id = user_id)
    if u :        
        db.delete(u)
        db.commit()
    else:
        raise exceptions.UserNotFoundError
    return




def get_all(db: Session, limit: int, offset: int) -> List[UserTable]:
    return db.query(UserTable).offset(offset).limit(limit).all()
