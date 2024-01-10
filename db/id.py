from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb+srv://laurod3:copito@cloudservices.mj0umuk.mongodb.net/")
db = client["CloudServices"]
collection = db["library"]

# Retrieve all documents from the collection
books = collection.find()

# Extract _id and title fields
id_title_list = [{"_id": str(book["_id"]), "title": book.get("title", "")} for book in books]

# Print the list of _id and title fields
print("List of _id and title fields:")
for item in id_title_list:
    print(f"ID: {item['_id']}, Title: {item['title']}")
