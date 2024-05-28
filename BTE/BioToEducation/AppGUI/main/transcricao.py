import flet as ft
import assets, layout, funcoes

def CriarLayoutTranscricao(page: ft.Page):
     
    page.theme = ft.Theme(
    scrollbar_theme=ft.ScrollbarTheme(
        track_color={
            ft.MaterialState.HOVERED: ft.colors.TRANSPARENT,
            ft.MaterialState.DEFAULT: ft.colors.TRANSPARENT,
        },
        track_visibility=False,
        track_border_color=ft.colors.TRANSPARENT,
        thumb_visibility=True,
        thumb_color={
            ft.MaterialState.HOVERED: ft.colors.BLACK12,
            ft.MaterialState.DEFAULT: ft.colors.BLACK12,
        },
        thickness=10,
        radius=5,
        
        )
    )   
    
    #Logo BTE
    img = ft.Image(
        src = assets.logoBTE,
        width= 200,
        height= 200,
        fit = ft.ImageFit.CONTAIN,
        filter_quality="HIGH",
            
    )
    
    # Sequencia dos ícones
    botaoHome = ft.ElevatedButton(
        "Home", icon = "home", icon_color = "black", on_click = lambda _: funcoes.Home(page), bgcolor = "white", color = "black",
        style = ft.ButtonStyle(
            side = {
                ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLACK),
            }
        ), adaptive = True, width = 160, 
    )
    
    botaoDna = ft.ElevatedButton(
        "Transcrição", icon = "CELL_TOWER", icon_color = "black", on_click = lambda _: funcoes.Traducao(page), bgcolor = "white", color = "black",
        style = ft.ButtonStyle(
            side = {
                ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLACK),
                
            } 
        ), adaptive = True, width = 160,

    ) 
    
    botaoRna = ft.ElevatedButton(
        "Tradução", icon = "translate", icon_color = "black", on_click = None, bgcolor = "white", color = "black", 
        style = ft.ButtonStyle(
            side = {
                ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLACK), 
                    
            }
        ), adaptive = True, width = 160,
    )
    
    botaoComparacao = ft.ElevatedButton(
        "Comparação", icon = "percent", icon_color = "black", on_click = None, bgcolor = "white", color = "black",
        style = ft.ButtonStyle(
            side = {
                ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLACK),
            }
        ), adaptive = True, width = 160
    )

    # Divisao dos icones e logo
    colunaSuperior = ft.Column(
        [
            img
        ],
        alignment = ft.MainAxisAlignment.START,
        horizontal_alignment= ft.CrossAxisAlignment.START,

        
    )
    
    colunaDoMeio = ft.Column(
        [
            botaoHome, botaoDna, botaoRna, botaoComparacao, 
    
        ],
        alignment= ft.MainAxisAlignment.START,
        horizontal_alignment = ft.CrossAxisAlignment.CENTER,
        expand = True,
        spacing = 20,
    )
    
    layoutAll = ft.Row(
            [
                ft.VerticalDivider(),
                ft.Container(
                    bgcolor= "#A1FF0A",
                    expand=False,
                    width=180,
                    border = ft.border.all(0.5, ft.colors.BLACK),
                    border_radius = ft.border_radius.BorderRadius(20, 0, 20, 0),
                    content = ft.Column(
                        [
                            colunaSuperior, colunaDoMeio, 
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
                    border_radius= ft.border_radius.BorderRadius(0, 20, 0, 20),
                    content = ft.Column(
                        [
                            
                        ]
                    )
                ),
                
            ],
            spacing=0,
            expand=True,

            )
    
    page.add(layoutAll)
    page.update()