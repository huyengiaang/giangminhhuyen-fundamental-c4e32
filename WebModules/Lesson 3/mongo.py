uri = 'mongodb://c4e:12345678Abc@ds231307.mlab.com:31307/c4e'
# python -m pip install pymongo dnspython

import pymongo

client = pymongo.MongoClient(uri)
db = client.c4e
collection = db.gmh
# collection.insert_one({'name':'gmh'})/

def get_all():
    collection = db.gmh
    return list(collection.find())

def insert_food(name, price):
    collection.insert_one({'name':name, 'price': price})

 

def insert_user(name: str, age: int):
    """[summary]
    
    Arguments:
        name {str} -- [description]
        age {int} -- [description]
    """
    collection = db.gmh
    collection.insert_one({'name':'gmh'})


# add 1 user into the collection 
# collection.insert_one({'name': 'gmh', 'age': 19})

# # list all users
# print(list(collection.find({})))

# # find all users named 'gmh'
# print(list(collection.find({'name':'gmh'})))

# # find one user named 'hoa'
# print(collection.find_one({'name': 'hoa'}))

# # update age of usernames
# collection.update_one({'name': 'gmh'}, {'$set':{'age': 40}})

# # ngoai ra con co cac lenh: update, update_many, replace_one

# # delete user named 'gmh'
# collection.delete_one({'name':'gmh'})


