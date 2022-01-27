from typing import Optional, List
from pydantic import BaseModel,  validator, Extra, root_validator
from app.model import models
from datetime import datetime

class ActivitiesBase(BaseModel):
    
    date: datetime
    type: models.Type
    dist: int
    desc: Optional[str] = None
    id_user:int


    '''@validator('date')
    def valid_date(cls, v):
        print (v)
        t = str(v)
        try:
          datetime.strptime( t ,'%Y-%m-%d %H:%M:%S'  )
          return v
        except:  
            raise ValueError(f'{v}, format date incoorect ')'''

    #@root_validator
    def valid_dist(cls, values):
        v = values.get('dist')
        type = values.get('type')
        date = values.get('date')
        print( v ,type , date )

        if type == models.Type.RUN and ( v < 1000 or v > 100000 ) :
          raise ValueError(f'{type}, dist comprise  entre 1 et 100 kms')
        
        if type == models.Type.SWIM and ( v < 500 or v > 20000 ) :
          raise ValueError(f'{type}, dist comprise entre 500 m et 50 kms')

        if type == models.Type.BIKE and ( v < 5000 or v > 200000 ) :
          raise ValueError(f'{type}, dist comprise entre 5 et 200 kms')

        return values

    class Config():
        extra = Extra.forbid    

class ActivitiesCreate(ActivitiesBase):
    pass  
        
class Activities(ActivitiesBase):
    id: Optional[int] = None
    class Config():
        orm_mode = True
        extra = Extra.forbid


class PaginatedActivities(BaseModel):
    limit: int
    offset: int
    data: List[Activities]

 