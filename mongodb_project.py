import pprint
import pymongo as pym

db_connection = pym.MongoClient(
    "mongodb+srv://pymongo:pymongo@cluster0.nhajgus.mongodb.net/?retryWrites=true&w=majority")

db = db_connection.test
collection = db.test_collection
