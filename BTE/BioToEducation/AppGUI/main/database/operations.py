from connections import getConnection
import bcrypt

def addUsuario(nome, instituicao, cargo, email, senha):
    db = getConnection()
    senhaHash = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()) # encriptando a senha
    db.users.insert_one({'nome': nome, 'instituicao': instituicao, 'cargo': cargo, 'email': email, 'senha': senhaHash})
    
def authUsuario(email, password):
    db = getConnection()
    user = db.users.find_one({'email': email, 'password': password})
    return user