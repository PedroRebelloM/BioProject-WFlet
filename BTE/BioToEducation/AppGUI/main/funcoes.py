import flet as ft
import os 
import sys 
import layout
from flet import Page, Text
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))


if root_dir not in sys.path:
    sys.path.append(root_dir)
    
from dataNAlgoritm.algoritm import mainAlgoritm

linhasPQ = []
def botaoA(linha: ft.Column):
    texto = mainAlgoritm.returnSequencia()
    # Quebra de texto 
    pontoDeQuebra = 180
    while len(texto) >= pontoDeQuebra:
        linhasPQ.append(texto[:pontoDeQuebra])
        texto = texto[pontoDeQuebra:]
        
    linhasPQ.append(texto)
    textoFormatado = '\n'.join(textoFormatado)
    novoTexto = ft.Text(value=textoFormatado, color = "black", size = 12, weight = "normal")
    linha.controls.clear()
    linha.controls.append(novoTexto)
    linha.update()
    return linha
    
def botaoB(linha: ft.Column):
    texto = mainAlgoritm.returnSequencia2()
    novoTexto = ft.Text(value=texto, color = "black", size = 12, weight = "normal")
    linha.controls.clear()
    linha.controls.append(novoTexto)
    linha.update()
    return linha

    



