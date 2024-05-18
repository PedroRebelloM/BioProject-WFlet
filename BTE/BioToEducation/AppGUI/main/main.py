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
        
        iconHome = ft.IconButton(
                icon = ft.icons.HOME, on_click=None, data=0,
                icon_color = "black",
                icon_size = 40,
                tooltip = "Home"
                
        )
        
        
        colunaSuperior = ft.Column(
            [
                img
            ],
            alignment = ft.MainAxisAlignment.START,
            horizontal_alignment= ft.CrossAxisAlignment.START
            
        )
        
        colunaDoMeio = ft.Column(
            [
                iconHome
            ],
            alignment= ft.MainAxisAlignment.CENTER,
            horizontal_alignment = ft.CrossAxisAlignment.CENTER
            
        )
        layout = ft.Row(
                [
                    ft.VerticalDivider(),
                    ft.Container(
                        bgcolor= "#A1FF0A",
                        expand=False,
                        width=140,
                        border = ft.border.all(0.5, ft.colors.BLACK),
                        border_radius = ft.border_radius.BorderRadius(20, 0, 20, 0),
                        content = ft.Column(
                            [
                               colunaSuperior, colunaDoMeio
                            ],
                            horizontal_alignment = ft.CrossAxisAlignment.CENTER
                          
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

        page.add(layout, iconHome)
        

ft.app(target=main, assets_dir="../assets/icons")