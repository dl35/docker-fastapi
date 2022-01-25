from fastapi import APIRouter,status, Depends, HTTPException
from sqlalchemy.orm import Session


from app.database import get_db
from app.crud import  users as crud
from app.schemas import users as schema
from app.exceptions import exceptions
from  ..dependencies import get_current_user


#https://github.com/ChristopherGS/ultimate-fastapi-tutorial/blob/main/part-10-jwt-auth/app/api/api_v1/endpoints/auth.py
#from app.dependencies import verify_token, verify_admin

# https://blog.balasundar.com/building-a-crud-app-with-fastapi-and-mysql

#https://sanjeevan.co.uk/blog/fastapi-quickstart

#https://christophergs.com/tutorials/ultimate-fastapi-tutorial-pt-7-sqlalchemy-database-setup/

#https://github.com/bitfumes/fastapi-course

router = APIRouter(
    prefix="/users",
    tags=["users"],
    #dependencies=[ Depends(get_current_user)],
    responses={404: {"description": "Not found"}})

    



#uniquement pour ADMIN
# récupérer la liste de users , pagination...
@router.get("/")
def list(db: Session = Depends(get_db), current = Depends(get_current_user) ,  limit: int = 10, offset: int = 0):
       
        if current['admin']==False :
          raise HTTPException(status_code=403, detail="Operation not permitted")
        
        u_list = crud.get_all(db, limit, offset)
        response = {"limit": limit, "offset": offset, "data": u_list}
        return response

#récupérer un user
@router.get("/{user_id}", status_code=status.HTTP_200_OK )
def get(user_id:int,db: Session = Depends(get_db), current = Depends(get_current_user)  ):
        
        if current['admin']==False and user_id != current['id'] :
          raise HTTPException(status_code=403, detail="Operation not permitted")

        try:
          u = crud.get(db, user_id=user_id )
          return u
        except exceptions.UserException as ue:
               raise HTTPException(**ue.__dict__) 

#ajouter un user, uniquement pour ADMIN
@router.post("/", status_code=status.HTTP_201_CREATED) 
def add(user: schema.UserCreate ,db: Session = Depends(get_db) , current = Depends(get_current_user)  ):
        if current['admin']==False :
          raise HTTPException(status_code=403, detail="Operation not permitted")
        try:
           u = crud.add(db, user )
           return u
        except exceptions.UserException as ue:
               raise HTTPException(**ue.__dict__) 
# modifier un user      
@router.put("/{user_id}", status_code=status.HTTP_204_NO_CONTENT) 
def update(user_id:int ,user: schema.UserCreate, db: Session = Depends(get_db) , current = Depends(get_current_user) ):

        if current['admin']==False and user_id != current['id'] :
          raise HTTPException(status_code=403, detail="Operation not permitted")

        try:
           u = crud.update(db, user_id, user ) 
           return u
        except exceptions.UserException as ue:
               raise HTTPException(**ue.__dict__) 


#supprimer un user, uniquement pour ADMIN
@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT) 
def delete(user_id:int,db: Session = Depends(get_db), current = Depends(get_current_user)  ):
        if current['admin']==False :
          raise HTTPException(status_code=403, detail="Operation not permitted")
        try:
          u = crud.delete(db, user_id )
          return u
        except exceptions.UserException as ue:
               raise HTTPException(**ue.__dict__) 
        
        