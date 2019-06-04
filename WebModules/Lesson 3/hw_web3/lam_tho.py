import pymongo 
from bson.objectid import ObjectId
uri = 'mongodb://admin:admin@ds021182.mlab.com:21182/c4e'

client = pymongo.MongoClient(uri)
db = client.c4e
collection = db.gmh

# add posts. 
posts = db.posts
post_data = {
    'title': 'A Late Late Night',
    'author': 'GMH',
    'content': "I'm dying in side, coding this poem."
}
result = posts.insert_one(post_data)
print('One post: {0}'.format(result.inserted_id))

# delete unnecessary posts. 
result = posts.delete_one({"_id" : ObjectId("5cf6c1a2a88d24aa3705b048")})