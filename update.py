import requests

# Book ID to be updated
book_id_to_update = '659e9807ba2d5e052e0c5428'  # Replace with the ID of the book you want to update
update_url = f"http://localhost:8000/books/659e9807ba2d5e052e0c5428"

# Updated book data
updated_book_data = {
    
    "title": "New Book 1",
    "author": "SKL",
    "publication_year": 2023,
    "isbn": "1234",
    "pages": 70
}

response = requests.put(update_url, json=updated_book_data)

if response.status_code == 200:
    print(f"Book with ID {book_id_to_update} updated successfully")
elif response.status_code == 404:
    print(f"Book with ID {book_id_to_update} not found")
else:
    print(f"Failed to update book with ID {book_id_to_update}. Status code: {response.status_code}")
