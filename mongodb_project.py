import pprint
import pymongo as pym

db_connection = pym.MongoClient(
    "mongodb+srv://pymongo:pymongo@cluster0.nhajgus.mongodb.net/?retryWrites=true&w=majority")

db = db_connection.test
collection = db.test_collection

data = [
    {
        "name": "jhon headhammer",
        "tax_number": "010101",
        "address": "headhammer@mail.com",
        "account": {
            "agency_number": "01",
            "account_number": "0001",
            "bank_balance": "1000.00"
        }
    },
    {
        "name": "sasha buttcracker",
        "tax_number": "020202",
        "address": "buttcracker@mail.com",
        "account": {
            "agency_number": "01",
            "account_number": "0002",
            "bank_balance": "2000.00"
        }
    }]

inserting_data = db.posts
result = inserting_data.insert_many(data)

for post in inserting_data.find():
    pprint.pprint(post)
