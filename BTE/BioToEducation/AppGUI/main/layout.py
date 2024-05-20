import flet as ft


def CriarLayout(page: ft.page):

    
    #Cores
        corOpacaGenes = ft.colors.with_opacity(0.35, "C9E995"),
    
    #Logo BTE
        img = ft.Image(
            src = r"C:\Users\Pedro\Desktop\BioProject-WFlet\BTE\BioToEducation\AppGUI\assets\Logo.png",
            width= 200,
            height= 200,
            fit = ft.ImageFit.CONTAIN,
            filter_quality="HIGH",
                
        )
        
        # Sequencia dos ícones
        iconHome = ft.ElevatedButton(
            "Home", icon = "home", icon_color = "black", on_click = None, bgcolor = "white", color = "black",
            style = ft.ButtonStyle(
                side = {
                    ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLACK),
                }
            ), adaptive = True, width = 160,
        )
        
        iconDna = ft.ElevatedButton(
            "Tradução", icon = "translate", icon_color = "black", on_click = None, bgcolor = "white", color = "black",
            style = ft.ButtonStyle(
                side = {
                    ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLACK),
                    
                } 
            ), adaptive = True, width = 160,

        ) 
        
        iconRna = ft.ElevatedButton(
            "Transcrição", icon = "CELL_TOWER", icon_color = "black", on_click = None, bgcolor = "white", color = "black", 
            style = ft.ButtonStyle(
                side = {
                    ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLACK), 
                        
                }
            ), adaptive = True, width = 160,
        )
        
        iconComparacao = ft.ElevatedButton(
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
                iconHome, iconDna, iconRna, iconComparacao, 
        
            ],
            alignment= ft.MainAxisAlignment.START,
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
            expand = True,
            spacing = 20,
        
        )
        
         # container texto A
        containerA = ft.Container(
            width = 400,
            height = 45, 
            bgcolor = "white",
            border = ft.border.all(1, "black"), 
            border_radius = ft.border_radius.all(20), 
          
        )
        
        #  container texto B
        containerB = ft.Container(
            width = 400,
            height = 45, 
            bgcolor = "white",
            border = ft.border.all(1, "black"), 
            border_radius = ft.border_radius.all(20),
          
        )
        
        containerDoisGenes = ft.Container(
            content = ft.Column(
                [
                    ft.Text("Meus Genes", color = "black", size = 14,),
                    containerA, containerB               
                ],  alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20,
                    
            ),
            width = 1200 * (3/4), 
            
        )
        
        #Container dos Meus Genes
        containerMeusGenes = ft.Container(
            bgcolor = "#59C9E995",
            width = 1200,
            height = 200,
            padding = 20,
            border = ft.border.only(bottom=ft.border.BorderSide(1, "black")),
            border_radius = ft.border_radius.BorderRadius(0, 0, 0, 0),
            content = ft.Column(
                [
                    containerDoisGenes,
                ], alignment= ft.MainAxisAlignment.START,
                    horizontal_alignment = ft.CrossAxisAlignment.CENTER, 
            )
        )
        
        # Aplicando layout todo
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
                        border_radius= ft.border_radius.BorderRadius(0, 20, 0, 20),
                        content = ft.Column(
                            [
                                containerMeusGenes
                            ],
                        )
                    ),
                    
                ],
                spacing=0,
                expand=True,

            )
        
        return layoutAll