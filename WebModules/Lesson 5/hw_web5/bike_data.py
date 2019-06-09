uri = 'mongodb://c4e:12345678Abc@ds231307.mlab.com:31307/c4e'
# python -m pip install pymongo dnspython

import pymongo
from bson.objectid import ObjectId

client = pymongo.MongoClient(uri)
db = client.c4e
collection = db.gmh

def insert_bike(model, fee, image, year):
    bike_data = {
        'model': model, 
        'fee': fee,
        'image': image,
        'year': year
    }
    collection.insert_one(bike_data)

print(list(collection.find({})))

# def get_all():
#     collection = db.gmh
#     return list(collection.find())