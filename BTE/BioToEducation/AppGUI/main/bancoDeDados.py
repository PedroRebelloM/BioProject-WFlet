import flet as ft
import assets, globalVar
import sys, os
import funcoes
import fix

dirPai = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if dirPai not in sys.path:
    sys.path.append(dirPai)
    
from dataNAlgoritm.algoritm import mainAlgoritm

# Pasta Raiz e imagens
if assets.root_dir not in sys.path:
    sys.path.append(assets.root_dir)
    
from AppGUI.classes.session import session

def CriarLayoutBancoDeDados(page: ft.Page): 
                
    arquivoEnviado = ft.FilePicker(on_result = lambda e: funcoes.EscolherArquivoBancoDeDados(e, 1, page))
    
    page.overlay.append(arquivoEnviado)
    
    #Tema aplicativo 
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
    
    botaoRna = ft.ElevatedButton(
        "Transcrição", icon = "CELL_TOWER", icon_color = "black", on_click = lambda _: funcoes.Transcricao(page), bgcolor = "white", color = "black",
        style = ft.ButtonStyle(
            side = {
                ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLACK),
                
            } 
        ), adaptive = True, width = 160, 

    ) 
    
    botaoDna = ft.ElevatedButton(
        "Tradução", icon = "translate", icon_color = "black", on_click = lambda _: funcoes.Traducao(page), bgcolor = "white", color = "black", 
        style = ft.ButtonStyle(
            side = {
                ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLACK), 
                    
            }
        ), adaptive = True, width = 160,
    )
    
    botaoComparacao = ft.ElevatedButton(
        "Comparação", icon = "percent", icon_color = "black", on_click = lambda _: funcoes.Comparacao(page), bgcolor = "white", color = "black",
        style = ft.ButtonStyle(
            side = {
                ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLACK),
            }
        ), adaptive = True, width = 160
    )
    
    botaoEscolhaArquivo = ft.ElevatedButton(
        "Arquivos", icon = "ATTACH_FILE", icon_color = "black", on_click = lambda _: funcoes.PgArquivos(page), bgcolor = "white", color = "black",
        style = ft.ButtonStyle(
            side = {
                ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLACK),
            }
        ), adaptive = True, width = 160
    )
    
    botaoActionBd = ft.ElevatedButton(
        "Database", icon = "CLOUD_UPLOAD", icon_color = "black", on_click = lambda _: funcoes.BancoDeDados(page), bgcolor = "white", color = "black",
        style = ft.ButtonStyle(
            side = {
                ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLACK),
            }
        ), adaptive = True, width = 160
    )
    
    botaoPesquisar = ft.ElevatedButton(
        "Pesquisar", icon = "SCREEN_SEARCH_DESKTOP_OUTLINED", icon_color = "black", on_click = lambda _: funcoes.Pesquisar(page), bgcolor = "white", color = "black",
        style = ft.ButtonStyle(
            side = {
                ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLACK),
            }
        ), adaptive = True, width = 160
    )
    
    botaoLogout = ft.ElevatedButton("Logout", icon = "logout", icon_color = "black", on_click = lambda _: funcoes.Retornar(page), bgcolor = "white", color = "black",
        style = ft.ButtonStyle(
            side = {
                ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLACK)
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
            botaoHome, botaoRna, botaoDna, botaoComparacao, botaoEscolhaArquivo, botaoActionBd, botaoPesquisar, botaoLogout
        ],
        alignment= ft.MainAxisAlignment.START,
        horizontal_alignment = ft.CrossAxisAlignment.CENTER,
        expand = True,
        spacing = 20,
    
    )
        
    # Texto Sequenciamento 
    texto = ft.Text("Envios para o banco de dados:", size = 20, weight = ft.FontWeight.W_600, italic = True, color = "black",  )
    
    containerTextoBD = ft.Container(
        content = texto, 
        margin = ft.margin.only(left = 25)
    )
    
    linha = ft.Column(
        [
            ft.Text("", color = 'black', width= 900)
        ], scroll = ft.ScrollMode.ALWAYS,
    ) 
    
    # Container abaixo do texto Banco de Dados
    containerBD = ft.Container(
        width = 1000,
        height = 420, 
        bgcolor = "#B5E995",
        border = ft.border.all(1, "black"), 
        border_radius = ft.border_radius.all(10),
        margin = ft.margin.only(left = 20),
        alignment=ft.alignment.top_left, 
        content = linha,
        data = '',
        padding = 25,
        
    )
    
    botaoAtualizar = ft.ElevatedButton(
        text = "Atualizar Lista",
        on_click = lambda _: funcoes.atualizarListaArquivos(linha, session.getUser()['_id']),
        bgcolor = "white",
        color = "black",
        width = 300,
        height = 30,
        style = ft.ButtonStyle(
           side =  {ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLACK)}
        )
    )

    
    #Botao do Gene A
    botaoPrimeiroGene = ft.ElevatedButton(
        text = fix.nomeGene1,  bgcolor = "white", color = "black", 
        style = ft.ButtonStyle(
            side = {
                ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLACK), 
                    
            }
        ), adaptive = True, width = 400, height = 30, on_click=lambda _: funcoes.BotaoPrimeiroGene(linha) 
    )
    
    #Botao do Gene B
    botaoSegundoGene = ft.ElevatedButton(
        text = fix.nomeGene2,  bgcolor = "white", color = "black", 
        style = ft.ButtonStyle(
            side = {
                ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLACK), 
                    
            }
        ), adaptive = True, width = 400, height = 30, on_click=lambda _: funcoes.BotaoSegundoGene(linha)
    )
        
    
    # Botão para atualizar os genes
    botaoEscolherArquivo1 = ft.Container(
        ft.ElevatedButton(
            "Escolher arquivo", on_click = lambda _: arquivoEnviado.pick_files(), bgcolor = "white", color = "black", 
            adaptive = True, width = 300, height = 30,
            style = ft.ButtonStyle(
                side = {
                    ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLACK),
                }
            ),
        ),           
            
    )
    
    containerDoisGenes = ft.Container(
        content=ft.Column(
        [
            ft.Text("Informações", color="black", size=20, weight=ft.FontWeight.W_600, text_align="CENTER"),
            ft.Row(
                [
                    ft.Column(
                        [
                            botaoPrimeiroGene, botaoSegundoGene
                            ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=5,
                    ),
                    ft.Container(
                        content = ft.Column(
                            [
                               botaoEscolherArquivo1, botaoAtualizar
                            ],
                        ),
                        alignment=ft.alignment.center,
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                width = 800
            
            ),
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.START,
    ),
            
    )
    
    #Container dos Meus Genes
    containerMeusGenes = ft.Container(
        bgcolor = "#59C9E995",
        width = 1400,
        height = 150,
        border = ft.border.only(bottom = ft.border.BorderSide(1, "black")),
        padding = ft.padding.only(left = 20),
        border_radius = ft.border_radius.BorderRadius(0, 0, 0, 0),
        content = ft.Column(
            [
                containerDoisGenes,
            ], alignment= ft.MainAxisAlignment.CENTER,
                horizontal_alignment = ft.CrossAxisAlignment.START, 
        )
    )
    
    # Aplicando layout todo
    layoutAll = ft.Row(
            [
                ft.VerticalDivider(),
                ft.Container(
                    bgcolor= "#A1FF0A",
                    expand= False,
                    width= 180,
                    border = ft.border.all(0.5, ft.colors.BLACK),
                    border_radius = ft.border_radius.BorderRadius(20    , 0, 20, 0),
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
                            containerMeusGenes, containerTextoBD, containerBD
                        ]
                    )
                ),
                
            ],
            spacing=0,
            expand=True,

            )
    
    page.update()   
    return layoutAll