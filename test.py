
import pymongo

client = pymongo.MongoClient("mongodb+srv://root:Root1234@root.y6a5m.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d= { 'name': 'nizam',
     'email': 'nizam.malik@gmsil.com',
     'surname': 'malik'



}

db1 = client['mongotest']
coll= db1['test']
coll.insert_one(d)
