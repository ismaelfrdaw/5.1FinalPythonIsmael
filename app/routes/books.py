from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database.database import get_db
from app.models import models
from app.schemas import schemas

router = APIRouter(
    prefix="/books",
    tags=["books"]
)

@router.get("/", response_model=List[schemas.BookResponse])
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve a list of books with pagination.
    """
    books = db.query(models.Book).offset(skip).limit(limit).all()
    return books

@router.get("/{book_id}", response_model=schemas.BookResponse)
def read_book(book_id: int, db: Session = Depends(get_db)):
    """
    Get a specific book by ID.
    """
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.post("/", response_model=schemas.BookResponse, status_code=201)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    """
    Create a new book record. Validates that the author exists.
    """
    # Check if author exists
    author = db.query(models.Author).filter(models.Author.id == book.author_id).first()
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")

    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@router.put("/{book_id}", response_model=schemas.BookResponse)
def update_book(book_id: int, book: schemas.BookCreate, db: Session = Depends(get_db)):
    """
    Update an existing book's details. Validates that the author exists.
    """
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    
    # Check if author exists
    author = db.query(models.Author).filter(models.Author.id == book.author_id).first()
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")

    for key, value in book.dict().items():
        setattr(db_book, key, value)
    
    db.commit()
    db.refresh(db_book)
    return db_book

@router.delete("/{book_id}", status_code=204)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    """
    Delete a book record from the database.
    """
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    
    db.delete(db_book)
    db.commit()
    return
