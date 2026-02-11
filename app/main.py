from fastapi import FastAPI
from app.database.database import engine, Base
from app.routes import authors, books

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Library API - Ismael Franco Ruiz 2º DAW",
    description="API for managing authors and books. Created by Ismael Franco Ruiz 2º DAW",
    version="1.0.0"
)

app.include_router(authors.router)
app.include_router(books.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Library API - Ismael Franco Ruiz 2º DAW"}
