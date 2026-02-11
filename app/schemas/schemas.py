from pydantic import BaseModel
from typing import List, Optional
from datetime import date

# Author Schemas
class AuthorBase(BaseModel):
    name: str
    bio: Optional[str] = None
    birth_date: Optional[date] = None
    nationality: Optional[str] = None

class AuthorCreate(AuthorBase):
    pass

class AuthorResponse(AuthorBase):
    id: int
    
    class Config:
        orm_mode = True

# Book Schemas
class BookBase(BaseModel):
    title: str
    description: Optional[str] = None
    publish_year: int
    pages: int
    author_id: int

class BookCreate(BookBase):
    pass

class BookResponse(BookBase):
    id: int
    
    class Config:
        orm_mode = True

# Extended Author Schema with Books
class AuthorWithBooks(AuthorResponse):
    books: List[BookResponse] = []
