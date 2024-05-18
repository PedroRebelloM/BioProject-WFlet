import flet as ft
from flet import View, Page, AppBar, ElevatedButton, Text
from flet import RouteChangeEvent, ViewPopEvent, CrossAxisAlignment, MainAxisAlignment

if __name__ == "__main__":
    
    def main(page: ft.Page) -> None:
        page.title = 'BTE - Biology To Education'
        
        #Logo BTE
        img = ft.Image(
                src = r"C:\Users\Pedro\Desktop\BioProject-WFlet\BTE\BioToEducation\AppGUI\assets\icons\Logo.png",
                width= 200,
                height= 200,
                fit = ft.ImageFit.CONTAIN,
                filter_quality="HIGH",
                
                )
        
        
        iconHome = ft.ElevatedButton(
            "Home", icon = "home", icon_color = "black", on_click = None, bgcolor = "white", color = "black",
            style = ft.ButtonStyle(
                side = {
                    ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLACK),
                }
            ), adaptive = True, width = 140,
        )
        
        iconDna = ft.ElevatedButton(
            "Tradução", icon = "translate", icon_color = "black", on_click = None, bgcolor = "white", color = "black",
            style = ft.ButtonStyle(
                side = {
                    ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLACK),
                    
                } 
            ), adaptive = True, width = 140,

        ) 
        
        iconRna = ft.ElevatedButton(
            "Transcrição", icon = "protein", icon_color = "black", on_click = None, bgcolor = "white", color = "black", 
            style = ft.ButtonStyle(
                side = {
                    ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLACK), 
                        
                }
            ), adaptive = True, width = 140,
        )
        
        iconComparacao = ft.ElevatedButton(
            "Comparação", icon = "percent", icon_color = "black", on_click = None, bgcolor = "white", color = "black",
            style = ft.ButtonStyle(
                side = {
                    ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLACK),
                }
            ), adaptive = True, width = 140,
        )
        
        
        colunaSuperior = ft.Column(
            [
                img
            ],
            alignment = ft.MainAxisAlignment.START,
            horizontal_alignment= ft.CrossAxisAlignment.START,

            
        )
        
        colunaDoMeio = ft.Column(
            [
                iconHome, iconDna, iconRna, iconComparacao
            ],
            alignment= ft.MainAxisAlignment.START,
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
            expand = True,
            spacing = 20,
        

            
        )
        layout = ft.Row(
                [
                    ft.VerticalDivider(),
                    ft.Container(
                        bgcolor= "#A1FF0A",
                        expand=False,
                        width=160,
                        border = ft.border.all(0.5, ft.colors.BLACK),
                        border_radius = ft.border_radius.BorderRadius(20, 0, 20, 0),
                        content = ft.Column(
                            [
                               colunaSuperior, colunaDoMeio
                            ],
                            horizontal_alignment = ft.CrossAxisAlignment.CENTER, 
                            
                          
                        )
                    )                 
                    ,
                    ft.Container(
                        bgcolor= "#FFFFFF",
                        alignment=ft.alignment.center,
                        expand=True,
                        border = ft.border.all(0.5, ft.colors.BLACK),
                        border_radius= ft.border_radius.BorderRadius(0, 20, 0, 20)
                    ),
                    
                ],
                spacing=0,
                expand=True,

            )

        page.add(layout)
        

ft.app(target=main, assets_dir="../assets/icons")