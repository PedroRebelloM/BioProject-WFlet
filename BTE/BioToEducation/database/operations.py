import bcrypt, os, sys
from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, ID
from database.connections import getConnection
from uuid import uuid4

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

if root_dir not in sys.path:
    sys.path.append(root_dir)

schema = Schema(user_id=ID(stored = True), file_path = ID(stored = True), content = TEXT)

if not os.path.exists("indexdir"):
    os.mkdir("indexdir")
    
indice = create_in("indexdir", schema)

def addUsuario(nome, instituicao, cargo, email, senha):
    db = getConnection()
    senhaHash = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()) # encriptando a senha
    db.users.insert_one({"nome": nome, "instituicao": instituicao, "cargo": cargo, "email": email, "senha": senhaHash})
    
def authUsuario(email, password):
    db = getConnection()
    user = db.users.find_one({"email": email})
    if user:
        senha_hash = user.get("senha", None)
        if senha_hash and bcrypt.checkpw(password.encode("utf-8"), senha_hash):
            return user
    return None

def salvarArquivoNoBancoEPesquisar(user_id, file_path, file_data):
    db = getConnection()
    db.files.insert_one({
        "user_id": user_id,
        "file_path": file_path,
        "file_data": file_data
    })
    
    with open(file_path, 'r', encoding = 'utf-8') as opd:
        conteudo = opd.read()
        
    construtor = indice.writer()
    construtor.add_document(user_id=str(user_id), file_path = file_path, content = conteudo)
    construtor.commit()

def listarArquivosNoBanco(user_id):
    db = getConnection()
    arquivos = db.files.find({"user_id": user_id})
    return arquivos
    
