from pymongo import MongoClient 
from bson import ObjectId

def connect(base):
    con = MongoClient()
    return con[base]

# user = {'_id':3, "nome":"maria antonieta"}
# db.usuario.insert(user)

# busca = db.usuario.find()
# busca['nome']
# print(busca['nome'])    
# busca = [x for x in busca]
# print(busca['nome'])
