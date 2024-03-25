# build a schema using pydantic
from pydantic import BaseModel

class Book(BaseModel):
    title: str
    text: str
    date: datetime
    classification: str 
    signature: str
    resolution: str
    pdf_path: str

    class Config:
        orm_mode = True


        