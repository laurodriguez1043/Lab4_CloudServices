from pymongo import MongoClient

connection_string = "mongodb+srv://laurod3:copito@cloudservices.mj0umuk.mongodb.net/"

try:
    # Try to connect to MongoDB
    client = MongoClient(connection_string)

    # Check if the connection is successful
    if client.server_info():
        print("MongoDB connection successful!")
    else:
        print("MongoDB connection failed.")
except Exception as e:
    print(f"Error: {e}")