import pymongo
import datetime

#mongo db client connection with connection string
client = pymongo.MongoClient("mongodb://shashi1991:Udk84gSBErE2198I@cluster0-shard-00-00-qqnja.mongodb.net:27017,cluster0-shard-00-01-qqnja.mongodb.net:27017,cluster0-shard-00-02-qqnja.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin")
#db obj
db = client.Tweepy
#collection obj
collection = db.Tweepy_data

new_posts = [{"author": "Mike","text": "Another post!","tags": ["bulk", "insert"],"date": datetime.datetime(2009, 11, 12, 11, 14)},{"author": "Eliot","title": "MongoDB is fun","text": "and pretty easy too!"}]

##inserting data in Tweepy[db]-->Tweepy_data[collection]
#result = collection.insert(new_posts)

#retrive all data from db
cursor = collection.find()

for entry in (cursor):
    print(entry)

cursor_author = collection.find({'author':'Mike'})

for entry_author in cursor_author:
    print(entry_author)
