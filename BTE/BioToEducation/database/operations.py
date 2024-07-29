import bcrypt, os, sys
from database.connections import getConnection
from uuid import uuid4

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

if root_dir not in sys.path:
    sys.path.append(root_dir)

def addUsuario(nome, instituicao, cargo, email, senha):
    db = getConnection()
    senhaHash = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()) # encriptando a senha
    db.users.insert_one({'nome': nome, 'instituicao': instituicao, 'cargo': cargo, 'email': email, 'senha': senhaHash})
    
def authUsuario(email, password):
    db = getConnection()
    user = db.users.find_one({'email': email})
    if user:
        senha_hash = user.get('senha', None)
        if senha_hash and bcrypt.checkpw(password.encode('utf-8'), senha_hash):
            return user
    return None

def salvarArquivoNoBanco(user_id, file_path, file_data):
    db = getConnection()
    db.files.insert_one({
        'user_id': user_id,
        'file_path': file_path,
        'file_data': file_data
    })