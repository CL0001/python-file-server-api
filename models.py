from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class File(Base):
    __tablename__ = "files"

    id = Column(String, primary_key=True)
    file_name = Column(String)
    file_size = Column(Integer)
    file_path = Column(String)
    created_at = Column(DateTime)
    created_by = Column(String)