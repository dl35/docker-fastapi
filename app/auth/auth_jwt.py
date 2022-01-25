
from typing import Dict
from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from decouple import config
from app.schemas import token as schema


JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")
JWT_TOKEN_EXPIRE_MINUTES = config("expire")


def create_access_token( data: schema.TokenData , expires_delta: Optional[timedelta] = None):
    
    to_encode = data.__dict__
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm=JWT_ALGORITHM)
    
    return encoded_jwt
