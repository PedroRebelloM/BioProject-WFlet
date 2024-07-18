import bcrypt, os, sys
from database.connections import getConnection

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

if root_dir not in sys.path:
    sys.path.append(root_dir)

def addUsuario(nome, instituicao, cargo, email, senha):
    db = getConnection()
    senhaHash = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()) # encriptando a senha
    db.users.insert_one({'nome': nome, 'instituicao': instituicao, 'cargo': cargo, 'email': email, 'senha': senhaHash})
    
def authUsuario(email, password):
    db = getConnection()
    user = db.users.find_one({'email': email, 'password': password})
    return user