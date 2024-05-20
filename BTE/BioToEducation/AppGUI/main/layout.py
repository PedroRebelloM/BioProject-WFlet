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
        containerA = ft.ElevatedButton(
            "Texto 1",  bgcolor = "white", color = "black", 
            style = ft.ButtonStyle(
                side = {
                    ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLACK), 
                        
                }
            ), adaptive = True, width = 400,
        )
        
        #  container texto B
        containerB = ft.ElevatedButton(
           "Texto 2",  bgcolor = "white", color = "black", 
            style = ft.ButtonStyle(
                side = {
                    ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLACK), 
                        
                }
            ), adaptive = True, width = 400, 
        )
            
      
        
        # Texto Sequenciamento 
        sequenciamento = ft.Text("Sequenciamento", size = 20, weight = ft.FontWeight.W_600, italic = True, color = "black", )
        
        containerTextoSequenciamento = ft.Container(
            content = sequenciamento, 
            margin = ft.margin.only(left = 25)
        )
        
        # Container abaixo do texto Sequenciamento
        containerSequenciamento = ft.Container(
            width = 1000,
            height = 380, 
            bgcolor = "#B5E995",
            border = ft.border.all(1, "black"), 
            border_radius = ft.border_radius.all(20),
            margin = ft.margin.only(left = 20),
            alignment=ft.alignment.center, 
           
        )
        
        containerBotaoAtualizar = ft.Container(
          ft.ElevatedButton(
                "Atualizar Genes", on_click = None, bgcolor = "white", color = "black",
                adaptive = True, width = 200, height = 30,
                style = ft.ButtonStyle(
                    side = {
                        ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLACK),
                    }
                ),
            ), 
        )
        
        containerDoisGenes = ft.Container(
            margin = ft.margin.only(top = 15),
            content = ft.Row(
                [
                ft.Column (
                    [
                    ft.Text("Meus Genes", color = "black", size = 14, weight = ft.FontWeight.W_600, italic = True ),
                    containerA, containerB, containerBotaoAtualizar   
                ],  
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=10,
                    
                ),
            ],
                alignment=ft.MainAxisAlignment.START,
                
               
        
            ), width = 1200 * (3/4),
               alignment = ft.alignment.center,
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
                    horizontal_alignment = ft.CrossAxisAlignment.START, 
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
                                containerMeusGenes,  containerTextoSequenciamento, containerSequenciamento
                            ]
                        )
                    ),
                    
                ],
                spacing=0,
                expand=True,

            )
        
        return layoutAll