from pydantic import BaseModel,  validator, Extra




class TokenData(BaseModel):
    
    id: int
    admin: bool = False
    
    class Config():
        orm_mode = True
        extra = Extra.forbid

