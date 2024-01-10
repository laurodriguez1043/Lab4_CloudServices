from pymongo import MongoClient
from faker import Faker

# Connect to MongoDB
client = MongoClient("mongodb+srv://laurod3:<3kz8IG3cgoCR68aU@cloudservices.mj0umuk.mongodb.net/")
db = client.CloudServices  # Specify your cluster name
collection = db.library  # Specify your database name and collection (item) name

# Create Faker instance for generating fake book data
fake = Faker()

# Insert 50 books into the database
for _ in range(50):
    new_book_data = {
        "title": fake.text(max_nb_chars=50),
        "author": fake.name(),
        "publication_year": fake.year(),
        "isbn": fake.unique.random_number(digits=10),
        "pages": fake.random_int(min=50, max=500)
    }

    # Insert the book into the collection
    collection.insert_one(new_book_data)

print("Books inserted successfully.")
