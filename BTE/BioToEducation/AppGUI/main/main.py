import flet as ft
from layout import CriarLayout
import sys
import os

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))


if root_dir not in sys.path:
    sys.path.append(root_dir)

# Agora você pode importar o módulo
from dataNAlgoritm.algoritm import mainAlgoritm

    
def main(page: ft.Page) -> None:
        page.title = 'BTE - Biology To Education'
        layout = CriarLayout(page)
        page.add(layout)
        page.window_min_width = 300
        page.window_max_width = 1200

      
if __name__ == "__main__":  
    ft.app(target=main, assets_dir="../assets")
