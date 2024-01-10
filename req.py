import requests

book_data = {
    "title": "Book",
    "author": "SKL",
    "publication_year": 2023,
    "isbn": 1234,
    "pages": 50
}

book_data_2 = {
    "title": "Genial",
    "author": "KSL",
    "publication_year": 2024,
    "isbn": 9783210,
    "pages": 400
}
# URLs for the POST requests
post_url = "http://localhost:8000/books/"

# Send POST request for the first book
response_1 = requests.post(post_url, json=book_data)
if response_1.status_code == 200:
    print("First book added successfully")
else:
    print("Failed to add the first book")

# Send POST request for the second book
response_2 = requests.post(post_url, json=book_data_2)
if response_2.status_code == 200:
    print("Second book added successfully")
else:
    print("Failed to add the second book")