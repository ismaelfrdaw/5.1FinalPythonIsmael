from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database.database import get_db
from app.models import models
from app.schemas import schemas

router = APIRouter(
    prefix="/authors",
    tags=["authors"]
)

@router.get("/", response_model=List[schemas.AuthorResponse])
def read_authors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve a list of authors with pagination.
    """
    authors = db.query(models.Author).offset(skip).limit(limit).all()
    return authors

@router.get("/{author_id}", response_model=schemas.AuthorWithBooks)
def read_author(author_id: int, db: Session = Depends(get_db)):
    """
    Get a specific author by ID, including their list of books.
    """
    author = db.query(models.Author).filter(models.Author.id == author_id).first()
    if author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return author

@router.post("/", response_model=schemas.AuthorResponse, status_code=201)
def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    """
    Create a new author record in the database.
    """
    db_author = models.Author(**author.dict())
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

@router.put("/{author_id}", response_model=schemas.AuthorResponse)
def update_author(author_id: int, author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    """
    Update an existing author's details.
    """
    db_author = db.query(models.Author).filter(models.Author.id == author_id).first()
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    
    for key, value in author.dict().items():
        setattr(db_author, key, value)
    
    db.commit()
    db.refresh(db_author)
    return db_author

@router.delete("/{author_id}", status_code=204)
def delete_author(author_id: int, db: Session = Depends(get_db)):
    """
    Delete an author record from the database.
    """
    db_author = db.query(models.Author).filter(models.Author.id == author_id).first()
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    
    db.delete(db_author)
    db.commit()
    return
