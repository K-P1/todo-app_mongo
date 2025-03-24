import os
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

load_dotenv()

MONGO_DB_CONNECTION_URI = os.environ.get('MONGO_DB_CONNECTION_URI')

class Database:
    def __init__(self):
        self.client = MongoClient(MONGO_DB_CONNECTION_URI, server_api=ServerApi('1'))
        self.db = self.client["todoapp"]
        self.user_collection = self.db["users"]
        self.todo_collection = self.db["todo"]
        
        # Test connection
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(f"Failed to connect to MongoDB: {e}")
            raise

db = Database()