from pymongo import MongoClient

def getConnection():
    client = MongoClient("mongodb+srv://pedro:OE90K8aVEjdtxNI0@cluster0.83zii.mongodb.net/")
    db = client['usuarios']
    
    return db