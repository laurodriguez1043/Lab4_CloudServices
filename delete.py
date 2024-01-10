import requests


book_delete = '659e9807ba2d5e052e0c5428'
delete_url = f"http://localhost:8000/books/659e9807ba2d5e052e0c5428"

response = requests.delete(delete_url)


if response.status_code == 200:
    print(f"Book with ID {book_delete} deleted successfully")
elif response.status_code == 404:
    print(f"Book with ID {book_delete} not found")
else:
    print(f"Failed to delete book with ID {book_delete}. Status code: {response.status_code}")