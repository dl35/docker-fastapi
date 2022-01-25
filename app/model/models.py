from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Enum, DateTime
from app.database import Base
import enum


class Type(str, enum.Enum):
    BIKE = "BIKE"
    SWIM = "SWIM"
    RUN = "RUN"


class RoleType(str, enum.Enum):
    ADMIN = "ADMIN"
    USER = "USER"
    

class UserTable(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    nom = Column( String(255), nullable=False)
    prenom = Column( String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True, index=True)
    passwd = Column( String(255), nullable=False)
    adresse = Column( String(255), nullable=False)
    ville = Column( String(255), nullable=False)
    cp = Column(Integer, nullable=False)
    role = Column(Enum(RoleType))
    

    

class ActivitiesTable(Base):
    __tablename__ = "activities"
    
    id = Column(Integer, primary_key=True, index=True)
    type = Column(Enum(Type))
    dist = Column(Integer, nullable=False)
    date = Column(DateTime, nullable=False)
    desc = Column(String(255) , nullable=True , default= 'NULL' ) 
    id_user = Column(Integer)
 
    

    
  
    
    
    
    
    
    
    
       
     
      