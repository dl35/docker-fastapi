from fastapi import APIRouter,status, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import  OAuth2PasswordRequestForm

from app.database import get_db

from app.crud import  login as crud
from app.schemas import users as schema

from app.schemas import token as schema_token

from app.exceptions import exceptions
from app.auth import auth_jwt



router = APIRouter(
    prefix="/login",
    tags=["login"],
    responses={404: {"description": "Not found"}})


@router.post("/", status_code=status.HTTP_200_OK) 
def login( form_data: OAuth2PasswordRequestForm = Depends() ,db: Session = Depends(get_db)):
       try:
  
           user=form_data.username
           pwd=form_data.password

           user = "clementine.austen@gmail.com"
           pwd = "75pa"
           
           obj = crud.get(db, user , pwd )
       except exceptions.UserException as ue:
             raise HTTPException(**ue.__dict__)   
       st = schema_token.TokenData(id=obj.id)
       if obj.role == "ADMIN":
           st.admin= True
       access_token =  auth_jwt.create_access_token( st  )      
       return {"access_token": access_token, "token_type": "bearer"}
       


@router.post("/signin", status_code=status.HTTP_200_OK) 
def signin( user: schema.UserCreate ,db: Session = Depends(get_db)):
       try:
           obj = crud.add(db, user )
       except exceptions.UserException as ue:
             raise HTTPException(**ue.__dict__)   
       
       return {"succes": 'true' }