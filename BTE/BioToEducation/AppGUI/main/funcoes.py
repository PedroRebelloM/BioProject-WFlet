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
    novoTexto = ft.Text(value=texto, color = "black", size = 12, weight = "normal")
    linha.controls.clear()
    linha.controls.append(novoTexto)
    linha.update()
    return linha
    
def botaoB(linha: ft.Column):
    texto = mainAlgoritm.returnSequencia2()
    novoTexto = ft.Text(value=texto, color = "black", size = 12, weight = "normal", text_align= ft.TextAlign.JUSTIFY)
    linha.controls.clear()
    linha.controls.append(novoTexto)
    linha.update()
    return linha




