import flet as ft
from flet import View, Page, AppBar, ElevatedButton, Text
from flet import RouteChangeEvent, ViewPopEvent, CrossAxisAlignment, MainAxisAlignment
from layout import CriarLayout
    
def main(page: ft.Page) -> None:
        page.title = 'BTE - Biology To Education'
        layout = CriarLayout(page)
        page.add(layout)
        page.window_min_width = 300
        page.window_max_width = 1200
      
if __name__ == "__main__":  
    ft.app(target=main, assets_dir="../assets")
