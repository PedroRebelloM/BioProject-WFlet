import flet as ft
import os, sys, re, bcrypt
import home, traducao, transcricao, comparacao, login, registrar, arquivos, bancoDeDados, pesquisar
import globalVar
from database import operations

dirPai = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if dirPai not in sys.path:
    sys.path.append(dirPai)

dirClasses = os.path.abspath(os.path.join(dirPai, 'classes'))
if dirClasses not in sys.path:
    sys.path.append(dirClasses)

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
if root_dir not in sys.path:
    sys.path.append(root_dir)

from database.operations import authUsuario, addUsuario
from AppGUI.classes.session import session
from dataNAlgoritm.algoritm import mainAlgoritm

linhasPQ = []
def BotaoPrimeiroGene(linha: ft.Column):
    linha.controls.clear()
    mainAlgoritm.atualizarResultados()
    texto = mainAlgoritm.returnSequencia()
    novoTexto = ft.Text(value=texto, color = "black", size = 12, weight = ft.FontWeight.BOLD, text_align= ft.TextAlign.JUSTIFY)
    linha.controls.append(novoTexto)
    linha.update()
    return linha
    
def BotaoSegundoGene(linha: ft.Column):
    linha.controls.clear()
    mainAlgoritm.atualizarResultados()
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
    
def BancoDeDados(page: ft.Page):
    page.controls.clear()
    page.add(bancoDeDados.CriarLayoutBancoDeDados(page))
    page.update()
    
def Pesquisar(page: ft.Page):
    page.controls.clear()
    page.add(pesquisar.CriarLayoutPesquisar(page))
    page.update()    

def PgArquivos(page: ft.Page):
    page.controls.clear()
    page.add(arquivos.CriarLayoutArquivos(page))
    page.update()
    
    
def BotaoATranscricao(linha: ft.Column):
    linha.controls.clear()
    mainAlgoritm.atualizarResultados()
    texto = mainAlgoritm.returnRna1()
    novoTexto = ft.Text(value=texto, color = "black", size = 12, weight = ft.FontWeight.BOLD, text_align= ft.TextAlign.JUSTIFY)
    linha.controls.append(novoTexto)
    linha.update()
    return linha

def BotaoBTranscricao(linha: ft.Column):
    linha.controls.clear()
    mainAlgoritm.atualizarResultados()
    texto = mainAlgoritm.returnRna2()
    novoTexto = ft.Text(value=texto, color = "black", size = 12, weight = ft.FontWeight.BOLD, text_align= ft.TextAlign.JUSTIFY)
    linha.controls.append(novoTexto)
    linha.update()
    return linha

def BotaoATraducao(linha: ft.Column):
    linha.controls.clear()
    mainAlgoritm.atualizarResultados()
    texto = mainAlgoritm.returnProteinasA()
    novoTexto = ft.Text(value=texto, color = "black", size = 12, weight = ft.FontWeight.BOLD, text_align= ft.TextAlign.JUSTIFY)
    linha.controls.append(novoTexto)
    linha.update()
    return linha

def BotaoBTraducao(linha: ft.Column):
    linha.controls.clear()
    mainAlgoritm.atualizarResultados()
    texto = mainAlgoritm.returnProteinasB()
    novoTexto = ft.Text(value=texto, color = "black", size = 12, weight = ft.FontWeight.BOLD, text_align= ft.TextAlign.JUSTIFY)
    linha.controls.append(novoTexto)
    linha.update()
    return linha

def BotaoDnaComparacao(linha: ft.Column, textoComparador: ft.Column):
    linha.controls.clear()
    textoComparador.controls.clear()
    mainAlgoritm.atualizarResultados()
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
    mainAlgoritm.atualizarResultados()  
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
    
def EscolherArquivo(e: ft.FilePickerResultEvent, qddArquivos, page: ft.Page):
        print("Função chamada")
        print(f"{qddArquivos}")
        caminhos = []
        
        if e.files:
            arquivos = e.files[0].path 
            if qddArquivos == 1:
                globalVar.setCaminhoArquivo(arquivos)
                mensagem = f"Primeiro arquivo selecionado: {globalVar.getCaminhoArquivo()}"
                print(globalVar.getCaminhoArquivo())
            elif qddArquivos == 2:
                globalVar.setCaminhoSegundoArquivo(arquivos)
                mensagem = f"Segundo arquivo selecionado: {globalVar.getCaminhoSegundoArquivo()}"
                print(globalVar.getCaminhoSegundoArquivo())
            else:
                print("Nenhum arquivo selecionado")   
            
            snack_bar = ft.SnackBar(
                content= ft.Text(mensagem),
                duration=2000
            )
            page.snack_bar = snack_bar
            page.snack_bar.open = True
            page.update()
        else: 
            print("Nnehum arquivo selecionado")
            
def EscolherArquivoBancoDeDados(e: ft.FilePickerResultEvent, qddArquivos, page: ft.Page):
    if not session.isLogged():
        mensagem = "Usuário não está logado!"
        snack_bar = ft.SnackBar(content=ft.Text(mensagem), duration=2000)
        page.snack_bar = snack_bar
        page.snack_bar.open = True
        page.update()
        return

    user = session.getUser()
    if e.files:
        arquivos = e.files[0].path  # 'file_path': Caminho do arquivo selecionado
        globalVar.setCaminhoArquivo(arquivos)
        mensagem = f"Arquivo selecionado: {globalVar.getCaminhoArquivo()}"
        print(globalVar.getCaminhoArquivo())

        # Ler o conteúdo do arquivo em modo binário
        with open(arquivos, 'rb') as file:
            file_data = file.read()  # 'file_data': Dados binários do arquivo
        
        # Salvar o arquivo no banco de dados
        operations.salvarArquivoNoBancoEPesquisar(user['_id'], arquivos, file_data)
        
        snack_bar = ft.SnackBar(
            content=ft.Text(mensagem),
            duration=2000
        )
        page.snack_bar = snack_bar
        page.snack_bar.open = True
        page.update()
    else:
        print("Nenhum arquivo selecionado")

def atualizarListaArquivos(linha: ft.Column, user_id):
    db = operations.getConnection()
    arquivos = db.files.find({"user_id": user_id}) #Requisição de acordo com o Id do usuário no banco de dados
    
    linha.controls.clear()
    
    linhasDeBotoes = []
    botoes = []
    
    for arquivo in arquivos:
        file_path = arquivo["file_path"]
        file_name = os.path.basename(file_path)  # Obter o nome do arquivo
        botao = ft.ElevatedButton(
            text = f"Baixar {file_name}",
            on_click = lambda e, p = file_path: downloadArquivo(p, linha),
            style = ft.ButtonStyle(
                shape = {ft.ControlState.DEFAULT: ft.RoundedRectangleBorder(radius = 5)},
                bgcolor = {ft.ControlState.DEFAULT: ft.colors.WHITE},
                elevation = {"pressed": 0, "": 1},
                 animation_duration = 500,
                side = {ft.ControlState.DEFAULT: ft.BorderSide(1, ft.colors.BLACK)},
                color = {ft.ControlState.DEFAULT: ft.colors.BLACK}
            ),
            width = 300
        )
        botoes.append(botao)  # Adicionar cada botão individualmente
        
        if len(botoes) == 3:
            linhaBotoes = ft.Row( # Linha para os trios
                controls = botoes,
                alignment = ft.MainAxisAlignment.START,
                spacing = 10
            )   
            
            linhasDeBotoes.append(linhaBotoes)
            botoes = []
            
            
    if botoes:
        linhaBotoes = ft.Row( # Linha para os trios
            controls = botoes,
            alignment = ft.MainAxisAlignment.START,
            spacing = 10
        )  
        
        linhasDeBotoes.append(linhaBotoes)
    
    linha.controls.extend(linhasDeBotoes) # Adicionando as linhas ao controle de linha (extend por ser mais de um objeto)
    linha.page.update() # Atualizar a página para refletir as alterações

def downloadArquivo(file_path, container: ft.Container):
    db = operations.getConnection()
    arquivo = db.files.find_one({"file_path": file_path})
    
    if arquivo:
        file_data = arquivo.get("file_data", None)
        
        if file_data is None:
            print(f"Erro: Dados do arquivo para {file_path} estão ausentes.")
            return
        
        # Definir o caminho de salvamento
        savePath = os.path.join(os.path.expanduser("~"), "Downloads", os.path.basename(file_path))
        
        try:
            with open(savePath, 'wb') as file:
                file.write(file_data)
            print(f"Arquivo {savePath} baixado com sucesso.")
            snack_bar = ft.SnackBar(
                content=ft.Text(f"Arquivo baixado com sucesso no local: {savePath}"),
                duration=2000
            )
        except Exception as e:
            print(f"Erro ao salvar o arquivo {savePath}: {e}")
            snack_bar = ft.SnackBar(
                content = ft.Text(f"Erro ao baixar {file_path}: {e}"),
                duration=2000
            )
        
        if container.page:
            container.page.snack_bar = snack_bar
            container.page.snack_bar.open = True
            container.page.update()
    else:
        print(f"Arquivo {file_path} não encontrado no banco de dados.")
        snack_bar = ft.SnackBar(
            content = ft.Text(f"Arquivo {file_path} não encontrado no banco de dados."),
            duration = 2000
        )
        if container.page:
            container.page.snack_bar = snack_bar
            container.page.snack_bar.open = True
            container.page.update()