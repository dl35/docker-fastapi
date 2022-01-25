from typing import Optional

from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from sqlalchemy.exc import SQLAlchemyError

from app.routers import login, manage, users, activities
import os

from app.model.models import Base
from app.database import  db_engine



Base.metadata.create_all(bind=db_engine)




app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    )
@app.exception_handler(SQLAlchemyError)
async def validation_exception_handler(request: Request, ex: SQLAlchemyError):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        
        content=jsonable_encoder({"detail": ex , "body": ''}),
    )   

@app.exception_handler(Exception)
async def validation_exception_handler(request: Request, ex: Exception):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        
        content=jsonable_encoder({"detail": ex , "body": 'body' }),
    )


app.include_router(login.router)    
app.include_router(manage.router)
app.include_router(users.router)
app.include_router(activities.router)



@app.get("/")
def read_root():
    return {"Hello": "World"}


