from flask_pymongo import MongoClient
from config import DBConfig

db = MongoClient(DBConfig.MONGO_URI).get_database('airbncDB')
