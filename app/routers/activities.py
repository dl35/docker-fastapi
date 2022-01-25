from fastapi import APIRouter,status, Depends, HTTPException
from sqlalchemy.orm import Session


from app.database import get_db
from app.crud import  activities as crud
from app.schemas import activities as schema
from app.exceptions import exceptions
from  ..dependencies import get_current_user
#from app.dependencies import verify_token, verify_admin

# https://blog.balasundar.com/building-a-crud-app-with-fastapi-and-mysql

#https://sanjeevan.co.uk/blog/fastapi-quickstart

#https://christophergs.com/tutorials/ultimate-fastapi-tutorial-pt-7-sqlalchemy-database-setup/

#https://github.com/bitfumes/fastapi-course

router = APIRouter(
    prefix="/activities",
    tags=["activities"],
    dependencies=[Depends(get_current_user)],
    responses={404: {"description": "Not found"}})

    

@router.get("/")
def list(db: Session = Depends(get_db),  current = Depends(get_current_user) , limit: int = 10, offset: int = 0 ) :

        if current['admin']==False :
            id_user= current['id']    
            u_list = crud.get_all_id(db, id_user ,limit, offset)
        else:
              u_list = crud.get_all(db, limit, offset)
        response = {"limit": limit, "offset": offset, "data": u_list}
        return response

@router.get("/{act_id}", status_code=status.HTTP_200_OK )

def get(act_id:int,db: Session = Depends(get_db),  current = Depends(get_current_user) ):
             
        try:
          u = crud.get(db, act_id=act_id )
          if current['admin']==False and u.id_user != current['id'] :
                raise HTTPException(status_code=403, detail="Operation not permitted")
          return u
        except exceptions.ActivitiesException as ue:
               raise HTTPException(**ue.__dict__) 


@router.post("/", status_code=status.HTTP_201_CREATED) 
def add(activities: schema.ActivitiesCreate ,db: Session = Depends(get_db) ):
       
       current = get_current_user()

       if current['admin']==False  and (activities.id_user != current['id'] ):
          raise HTTPException(status_code=403, detail="Operation not permitted")


       try:
           u = crud.add(db, activities )
           return u
       except exceptions.UserException as ue:
               raise HTTPException(**ue.__dict__)   
       except exceptions.ActivitiesException as ue:
               raise HTTPException(**ue.__dict__) 
      
@router.put("/{act_id}", status_code=status.HTTP_204_NO_CONTENT) 
def update(act_id:int ,activities: schema.ActivitiesCreate, db: Session = Depends(get_db) , current = Depends(get_current_user)):
       
        if current['admin']==False  and (activities.id_user != current['id'] ):
          raise HTTPException(status_code=403, detail="Operation not permitted")  

        try:
           u = crud.update(db, act_id, activities ) 
           return u
        except exceptions.UserException as ue:
               raise HTTPException(**ue.__dict__)    

        except exceptions.ActivitiesException as ue:
               raise HTTPException(**ue.__dict__) 

@router.delete("/{act_id}", status_code=status.HTTP_204_NO_CONTENT) 
async def delete(act_id:int,db: Session = Depends(get_db) ,  current = Depends(get_current_user)):
       
       try:
        obj = crud.get(db,act_id)
        print( obj, current)
        if obj is None  or (obj.id_user != current['id'] ) :
              print( obj, current)
              raise HTTPException(status_code=403, detail="Operation not permitted")
       
        u = crud.delete(db, act_id )
        return u
       except exceptions.ActivitiesException as ue:
               raise HTTPException(**ue.__dict__) 
        
        