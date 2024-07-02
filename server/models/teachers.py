from model.basemodel import BaseModel, Base
from sqlalchemy import Column, String, Integer, Enum


class Teacher(BaseModel, Base):
  """
  """
  __tablename__ = "teachers"
  decipline = Column(String(35), nullable=False)
  subject = Column(String(35), nullable=False)
  number_of_classes = Column(Integer, nullable=False)
  number_of_students = Column(Integer, nullable=False, default=30)
  employment_type = Column(Enum("permanent staff", "corp member", "IT student", "contractor"), nullable=False)
  
  def __init__(self, *args, **kwargs):
    """
    """
    super().__init__(*args, **kwargs)