from pymongo import MongoClient

def getConnection():
    client = MongoClient('localhost', 27017)
    db = client.usuarios
    
    return db