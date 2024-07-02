from  models.basemodel import BaseModel
from sqlalchemy import Column, String, Integer, Enum
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(BaseModel, Base):
  """
  """
  __tablename__ = "students"
  current_class = Column(String(30), nullable=False)
  house = Column(String(60), nullable=False)
  dicipline = Column(String(35), nullable=False)
  number_of_subjects_taken = Column(Integer, nullable=False, default=9)
  
  
  def __init__(*args, **kwargs):
    """
    """
    super().__init__(*args, **kwargs)