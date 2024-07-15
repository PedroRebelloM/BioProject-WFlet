from connections import getConnection

def addUsuario(email, password):
    db = getConnection()
    db.users.insert_one({'email': email, 'password': password})
    
def authUsuario(email, password):
    db = getConnection()
    user = db.users.find_one({'email': email, 'password': password})
    return user