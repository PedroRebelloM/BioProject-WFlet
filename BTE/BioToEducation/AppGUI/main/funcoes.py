import flet as ft
import os 
import sys 
import layout
import main 
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))


if root_dir not in sys.path:
    sys.path.append(root_dir)
    
from dataNAlgoritm.algoritm import mainAlgoritm



def atualizarContainer(container, page):
    sequenciamentoClick = mainAlgoritm.seQ
    layout.containerSequenciamento.context = ft.Text(sequenciamentoClick)
    page.update()



