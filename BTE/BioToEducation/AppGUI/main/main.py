import sys
import os
import flet as ft

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

if root_dir not in sys.path:
    sys.path.append(root_dir)

from login import CriarLayoutLogin

def main(page: ft.Page) -> None:
    page.title = 'BTE - Biology To Education'

    page.window.width = 800
    page.window.height = 600
    CriarLayoutLogin(page)
    page.update(page)

if __name__ == "__main__":
    ft.app(target=main, assets_dir="../assets")