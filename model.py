from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()  

class DocumentMetadados(Base):
    __tablename__ = 'document_metadados'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    text = Column(String)
    date = Column(DateTime(timezone=True), server_default=func.now())
    classification = Column(String)
    signature = Column(String)
    resolution = Column(String)
    pdf_path = Column(String)