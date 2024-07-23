import flet as ft
import os, sys, re, bcrypt
import home, traducao, transcricao, comparacao, login, registrar
from session import session

dirPai = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if dirPai not in sys.path:
    sys.path.append(dirPai)

from database.operations import authUsuario, addUsuario

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

if root_dir not in sys.path:
    sys.path.append(root_dir)
    
from dataNAlgoritm.algoritm import mainAlgoritm

linhasPQ = []
def BotaoA(linha: ft.Column):
    linha.controls.clear()
    texto = mainAlgoritm.returnSequencia()
    novoTexto = ft.Text(value=texto, color = "black", size = 12, weight = ft.FontWeight.BOLD, text_align= ft.TextAlign.JUSTIFY)
    linha.controls.append(novoTexto)
    linha.update()
    return linha
    
def BotaoB(linha: ft.Column):
    linha.controls.clear()
    texto = mainAlgoritm.returnSequencia2()
    novoTexto = ft.Text(value=texto, color = "black", size = 12, weight = ft.FontWeight.BOLD, text_align= ft.TextAlign.JUSTIFY)
    linha.controls.append(novoTexto)
    linha.update()
    return linha

def Home(page: ft.Page):
    page.controls.clear()
    page.add(home.CriarLayout(page))
    page.update()
    
def Traducao(page: ft.Page):
    page.controls.clear()
    page.add(traducao.CriarLayoutTraducao(page))
    page.update()

def Transcricao(page: ft.Page):
    page.controls.clear()
    page.add(transcricao.CriarLayoutTranscricao(page))
    page.update()
    
def Comparacao(page: ft.Page):
    page.controls.clear()
    page.add(comparacao.CriarLayoutComparação(page))
    page.update()
    
def BotaoPgRegistrar(page: ft.Page):
    page.controls.clear()
    page.add(registrar.CriarLayoutRegistro(page))
    page.update()
    
def Retornar(page: ft.Page):
    page.controls.clear()
    page.add(login.CriarLayoutLogin(page))
    page.update()
    print("Pg adicionada")  # Log temporário para depuração
    
def BotaoATranscricao(linha: ft.Column):
    linha.controls.clear()
    texto = mainAlgoritm.returnRna1()
    novoTexto = ft.Text(value=texto, color = "black", size = 12, weight = ft.FontWeight.BOLD, text_align= ft.TextAlign.JUSTIFY)
    linha.controls.append(novoTexto)
    linha.update()
    return linha

def BotaoBTranscricao(linha: ft.Column):
    linha.controls.clear()
    texto = mainAlgoritm.returnRna2()
    novoTexto = ft.Text(value=texto, color = "black", size = 12, weight = ft.FontWeight.BOLD, text_align= ft.TextAlign.JUSTIFY)
    linha.controls.append(novoTexto)
    linha.update()
    return linha

def BotaoATraducao(linha: ft.Column):
    linha.controls.clear()
    texto = mainAlgoritm.returnProteinasA()
    novoTexto = ft.Text(value=texto, color = "black", size = 12, weight = ft.FontWeight.BOLD, text_align= ft.TextAlign.JUSTIFY)
    linha.controls.append(novoTexto)
    linha.update()
    return linha

def BotaoBTraducao(linha: ft.Column):
    linha.controls.clear()
    texto = mainAlgoritm.returnProteinasB()
    novoTexto = ft.Text(value=texto, color = "black", size = 12, weight = ft.FontWeight.BOLD, text_align= ft.TextAlign.JUSTIFY)
    linha.controls.append(novoTexto)
    linha.update()
    return linha

def BotaoDnaComparacao(linha: ft.Column, textoComparador: ft.Column):
    linha.controls.clear()
    textoComparador.controls.clear()
    textoComp = mainAlgoritm.returnPorcentagemDna()
    texto = mainAlgoritm.returnAlinhamentoDna()
    novoTexto = ft.Text(value=texto, color = "black", size = 12, weight = ft.FontWeight.BOLD, text_align= ft.TextAlign.JUSTIFY)        
    novoTextoComp = ft.Text(value=textoComp, color = "black", size = 12, weight = ft.FontWeight.BOLD, text_align= ft.TextAlign.JUSTIFY)
    linha.controls.append(novoTexto)
    textoComparador.controls.append(novoTextoComp)
    linha.update(),
    textoComparador.update()
    return linha, textoComparador

def BotaoRnaComparacao(linha: ft.Column, textoComparador: ft.Column):
    linha.controls.clear()
    textoComparador.controls.clear()
    textoComp = mainAlgoritm.returnPorcentagemRna()
    texto = mainAlgoritm.returnAlinhamentoRna()
    novoTexto = ft.Text(value=texto, color = "black", size = 12, weight = ft.FontWeight.BOLD, text_align= ft.TextAlign.JUSTIFY)        
    novoTextoComp = ft.Text(value=textoComp, color = "black", size = 12, weight = ft.FontWeight.BOLD, text_align= ft.TextAlign.JUSTIFY)       
    linha.controls.append(novoTexto)
    textoComparador.controls.append(novoTextoComp)
    linha.update()
    textoComparador.update()
    return linha, textoComparador

def verificarEmail(email: str) -> bool:
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$' # verifica email com o modulo regex:
    return re.match(regex, email) is not None # r'aceita lums e letras + @ com nums e letras + . com letras e nums'
 
def Entrar(campoUsuario: ft.TextField, campoSenha: ft.TextField, area: ft.Text, page: ft.Page):
    email = campoUsuario.value
    senha = campoSenha.value
    
    user = authUsuario(email, senha)
    if user: 
        session.Login(user)
        area.value = "Login Bem-Sucedido"
        page.update()
        Home(page)
    else: 
        area.value = "Faça o seu registro ou verifique seu usuário e/ou senha!"
    
    page.update()
    
def Registrar(campoNome: ft.TextField, campoInstituicao: ft.TextField, campoCargo: ft.TextField, campoUsuario: ft.TextField, campoSenha: ft.TextField, campoConfirmacao: ft.TextField, area: ft.Text, page: ft.Page):
    
    nome = campoNome.value
    instituicao = campoInstituicao.value
    cargo = campoCargo.value
    email = campoUsuario.value
    senha = campoSenha.value
    
    
    if senha != campoConfirmacao.value:
        area.value = "As senhas não conferem"
    elif not verificarEmail(email):
        area.value = "Email inválido"
    else: 
        addUsuario(nome, instituicao, cargo, email, senha)
        area.value = "Usuário criado!"
        
    page.update()


def Logout(page: ft.Page):
    session.logout()
    Retornar(page)

    
