import flet as ft
from login import CriarLayoutLogin
import sys
import os

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

if root_dir not in sys.path:
    sys.path.append(root_dir)

# Agora você pode importar o módulo
from dataNAlgoritm.algoritm import mainAlgoritm
    
def main(page: ft.Page) -> None:
    page.title = 'BTE - Biology To Education'
        
    page.window.width = 800
    page.window.height = 600
    CriarLayoutLogin(page)
    page.update()
      
if __name__ == "__main__":  
    ft.app(target=main, assets_dir="../assets")
