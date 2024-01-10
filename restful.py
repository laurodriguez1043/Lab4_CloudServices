from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Dict, Optional
from pymongo import MongoClient
from bson import ObjectId

app = FastAPI()

# Connect to MongoDB
client = MongoClient("mongodb+srv://laurod3:copito@cloudservices.mj0umuk.mongodb.net/")
db = client.CloudServices  # Specify your cluster name
collection = db.library  # Specify your database name and collection (item) name


# database to store books
#books_db = {}
#book_uniq_id =1

# model for Book
class Book(BaseModel):
    title: str
    author: str
    publication_year: int
    isbn: int
    pages: Optional[int]
    class Config:
        json_encoders = {ObjectId: str}

# Create a new book
@app.post("/books/")
def create_book(book: Book):
    #global book_uniq_id
    #book_id = book_uniq_id
    #books_db[book_id] = book
    #book_uniq_id += 1
    book_dict = book.dict()
    result = collection.insert_one(book_dict)
    return {"message": "Book created successfully", "book_id": str(result.inserted_id)}

# Get all books
@app.get("/books/")
def get_all_books():
    # books = list(collection.find())
    # return books
    books = list(collection.find({}))  # Fetch all books from MongoDB
    serialized_books = []
    for book in books:
        book["_id"] = str(book["_id"])  # Convert ObjectId to str
        serialized_books.append(Book(**book).dict())
    return serialized_books

# Get a book by ID
@app.get("/books/{book_id}")
def get_book_by_id(book_id: str):
    obj_id = ObjectId(book_id)

    book = collection.find_one({"_id": obj_id})

    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    #if book_id not in books_db:
    #    raise HTTPException(status_code=404, detail="Book not found")

    book["_id"]=str(book["_id"])
    return book

# Update a book by ID
@app.put("/books/{book_id}")
def update_book(book_id: str, book: Book):
    #if book_id not in books_db:
    #    raise HTTPException(status_code=404, detail="Book not found")
    #books_db[book_id] = book
    obj_id = ObjectId(book_id)
    book_dict = book.dict(exclude={"_id"})
    result = collection.update_one({"_id": obj_id}, {"$set": book_dict})
    #book["_id"]=str(book["_id"])
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book updated successfully"}

# Delete a book by ID
@app.delete("/books/{book_id}")
def delete_book(book_id: str):
    #if book_id not in books_db:
    #    raise HTTPException(status_code=404, detail="Book not found")
    #del books_db[book_id]
    obj_id = ObjectId(book_id)
    result = collection.delete_one({"_id": obj_id})
    
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted successfully"}