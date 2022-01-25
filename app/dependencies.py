
from fastapi import Header,status, Depends, HTTPException
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from fastapi.responses import JSONResponse
import json
from app.crud import  users as crud
from app.schemas import token as schema
from app import exceptions
from app.database import get_db
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext

from decouple import config



JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")
JWT_TOKEN_EXPIRE_MINUTES = config("expire")


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")





async def get_current_user(token: str = Depends(oauth2_scheme) , db: Session = Depends(get_db) ):
   
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        id: str = payload.get("id")
        admin: str = payload.get("admin")
        if id is None or admin is None :
            raise credentials_exception
        u = crud.get(db,id)
        role = "USER"
        if admin:
            role = "ADMIN"
        if( u.id !=id or u.role != role ):
            raise credentials_exception
        obj = dict()   
        obj['id']=u.id
        obj['admin']=admin
        
    except JWTError:
        raise credentials_exception
    return obj


      