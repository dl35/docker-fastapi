from sqlalchemy.orm import Session
from app.model.models import UserTable
from app.schemas import login as schema
from app.exceptions import exceptions



def get(db: Session, u :str , pwd :str ):
    u = db.query(UserTable).filter( UserTable.email == u , UserTable.passwd == pwd ).first()
    if u is None:
        raise exceptions.UserUnauthorizedError
    return u