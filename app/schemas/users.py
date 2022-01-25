from typing import Optional, List
from pydantic import BaseModel,  validator, Extra
from app.model import models

import re
class UserBase(BaseModel):
    
    nom: str
    prenom: str
    email: str
    passwd: str
    adresse: str
    ville: str
    cp: int
    role: models.RoleType
    

    @validator('nom','prenom','adresse','ville')
    def valid_str(cls, v):
        if v.strip() == "":
          raise ValueError(f'{v}, est vide')
        return v

    @validator('email')
    def valid_email(cls, v):
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if not re.fullmatch(regex, v):
          raise ValueError(f'{v}, email non conforme')
        return v

    @validator('passwd')
    def valid_passwd(cls, v):
        if len(v.strip())  <  4 :
          raise ValueError(f'{v}, 4 chars minimum')
        return v

    @validator('cp')
    def valid_cp(cls, v):
        if len(str(v)) !=  5 :
            raise ValueError(f'{v}, 5 chars')
        return v
    
    class Config():
        extra = Extra.forbid



class UserCreate(UserBase):
    pass  
        
class User(UserBase):
    id: Optional[int] = None
    class Config():
        orm_mode = True
        extra = Extra.forbid

class PaginatedUsers(BaseModel):
    limit: int
    offset: int
    data: List[User]

 