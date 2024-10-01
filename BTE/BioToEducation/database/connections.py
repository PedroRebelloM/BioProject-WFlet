from pymongo import MongoClient

def getConnection():
    client = MongoClient("mongodb+srv://pedro:HwlnkSfcpTEaEvdd@cluster0.83zii.mongodb.net/")
    db = client['usuarios']
    
    return db