import flet as ft
import os 
import sys 
import layout, traducao, transcricao, comparacao
import clipboard as cp

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
    page.add(layout.CriarLayout(page))
    page.update()
    
def Traducao(page: ft.Page):
    page.controls.clear()
    page.add(traducao.CriarLayoutTraducao(page))
    page.update()

def Transcricao(page: ft.Page):
    page.controls.clear()
    page.add(transcricao.CriarLayoutTranscricao(page))
    
def Comparacao(page: ft.Page):
    page.controls.clear()
    page.add(comparacao.CriarLayoutComparação(page))
    
def Copiar(linha: ft.Column):
    cp.copy(linha)
    
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
    linha.update()
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
    return linha, textoComparador