import sqlalchemy
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid
import datetime

Base = declaractive_base()

class Basemodel:
  """
  """
  id = Column(String(60), primary_key=True)
  first_name = Column(String(128), nullable=False)
  last_name = Column(String(128), nullable=False)
  created_at = Column(DateTime, default=datetime.utcnow)
  updated_at = Column(Datetime, default=datetime.utcnow)
  email = Column(String(60), unique=true, nullable=False)
  password = Column(String(60), nullable=False)
  password2 = Column(String(60), nullable=False)
  age = Column(Integer, nullable=False)
  sex = Column(String(6), nullable=False)
  nin = Column(Integer, nullable=False)
  lga = Column(String(128), nullable=False)
  state_of_origin = Column(String(128), nullable=false)
  
  def __init__(self, *args, **kwargs):
    """
    """
    #self.id = str(uuid.uuid4())