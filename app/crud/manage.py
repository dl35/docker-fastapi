from typing import List
from sqlalchemy.orm import Session
from app.model.models import UserTable,ActivitiesTable
from app.schemas import users as susers ,activities as sactivities


def add_all_users(db: Session, users: List[susers.User] ):
    num_of_deleted_rows = db.query(UserTable).delete()
    db.add_all( users )
    db.commit()
    return db.query(UserTable).count()


def add_user(db: Session, user: susers.UserCreate ):
    db_user = UserTable( **user.dict() )
    db.add( db_user )
    db.commit()
    return db.query(UserTable).count()



def add_all_activities(db: Session, acts: List[sactivities.Activities ] ):
    num_of_deleted_rows = db.query(ActivitiesTable).delete()
    #print( num_of_deleted_rows )
    db.add_all( acts )
    db.commit()
    return db.query(ActivitiesTable).count()


def add_activities(db: Session, act: sactivities.ActivitiesCreate ):
    db_act = ActivitiesTable( **act.dict() )
    db.add( db_act )
    db.commit()
    return db.query(ActivitiesTable).count()