from pydantic import BaseModel,  validator, Extra




class LoginBase(BaseModel):
    
    email: str
    passwd: str


class Login(LoginBase):
    pass
    class Config():
        orm_mode = True
        extra = Extra.forbid
