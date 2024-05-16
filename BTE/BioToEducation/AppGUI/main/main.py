import flet as ft
from flet import View, Page, AppBar, ElevatedButton, Text
from flet import RouteChangeEvent, ViewPopEvent, CrossAxisAlignment, MainAxisAlignment

def main(page: ft.Page) -> None:
    page.title = 'BTE - Biology To Education'
    
    page.add(
        ft.Row(
            [
                 ft.VerticalDivider(),
                ft.Container(
                    bgcolor= "#A1FF0A",
                    alignment=ft.alignment.center,
                    expand=False,
                    width=140
                ),
                ft.Container(
                    bgcolor= "#FFFFFF",
                    alignment=ft.alignment.center,
                    expand=True,
                ),
                
            ],
            spacing=0,
            expand=True,
        )
    )
ft.app(target=main)