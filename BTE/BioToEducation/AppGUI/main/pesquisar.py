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

def CriarLayoutPesquisar(page: ft.Page): 
                
    arquivo1 = ft.FilePicker(on_result = lambda e: funcoes.EscolherArquivoBancoDeDados(e, 1, page))
    
    page.overlay.append(arquivo1)
    
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
    
    botaoPgArquivo = ft.ElevatedButton(
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
            botaoHome, botaoRna, botaoDna, botaoComparacao, botaoPgArquivo, botaoActionBd, botaoPesquisar, botaoLogout
        ],
        alignment= ft.MainAxisAlignment.START,
        horizontal_alignment = ft.CrossAxisAlignment.CENTER,
        expand = True,
        spacing = 20,
    )
        
    #Texto Sequenciamento 
    texto = ft.Text("Retorno do Banco de Dados:", size = 20, weight = ft.FontWeight.W_600, italic = True, color = "black")
    
    containerTextoBD = ft.Container(
        content = texto, 
        margin = ft.margin.only(left = 25)
    )
    
    linha = ft.Column(
        [
            ft.Text("", color = 'black', width= 900)
        ], scroll = ft.ScrollMode.ALWAYS,
    ) 
    
    #Container abaixo do texto Resultados
    global containerBD  # Adicione uma referência global ao contêiner
    containerBD = ft.Container(
        width = 1000,
        height = 500, 
        margin = ft.margin.only(left = 20),
        alignment=ft.alignment.top_left, 
        content = linha,
        data = '',
        padding = 25,
    )
    
    # Botao do Gene A    
    # botaoSelected = ft.SegmentedButton(
    #     on_change = None,
    #     selected = {"1"},
    #     allow_multiple_selection = True,
    #     allow_empty_selection = True,
    #     show_selected_icon = False,
    #     width = 200,
    #     style= ft.ButtonStyle(
    #         bgcolor={
    #             ft.MaterialState.SELECTED: ft.colors.LIGHT_GREEN_ACCENT,
    #             ft.MaterialState.DEFAULT: ft.colors.WHITE,
    #         },      
    #         side = {ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLACK),},
    #         elevation = {"pressed": 0, "": 1},
    #     ),
    #     segments = [
    #         ft.Segment(
    #             value = "1",
    #             label = ft.Text("DNA", size = 12, color = ft.colors.BLACK, text_align = ft.TextAlign.CENTER, weight = ft.FontWeight.BOLD),
    #         ),
    #         ft.Segment(
    #             value = "2",
    #             label = ft.Text("NOME", size = 12, color = ft.colors.BLACK, text_align = ft.TextAlign.CENTER, weight = ft.FontWeight.BOLD),
    #         ),
    #         ft.Segment(
    #             value = "3",
    #             label = ft.Text("RNA", size = 12, color = ft.colors.BLACK, text_align = ft.TextAlign.CENTER, weight = ft.FontWeight.BOLD),
    #         )
    #     ]
    # )
    
    bancoSelected = ft.Dropdown(
    options=[
        ft.dropdown.Option("Genoma"),
        ft.dropdown.Option("PubMed"),
        ft.dropdown.Option("Protein"),
        ft.dropdown.Option("Gene")
    ],
    value="Genoma",  # Valor padrão
    width=160,
    on_change=lambda e: print(f"Banco selecionado no dropdown: {bancoSelected.value}"),  # Adiciona um print para verificar
    text_style = ft.TextStyle(
        color = ft.colors.BLACK, 
        size = 14,  
        weight = ft.FontWeight.BOLD  
    ),
    
)
    
    campoTexto = ft.TextField(
        hint_text = "Pesquise por RNA, DNA ou Nome",
        color = ft.colors.BLACK,
        content_padding = 5,
        focused_border_color = ft.colors.BLACK26,
        hint_style=ft.TextStyle(
            color=ft.colors.BLACK26,
            italic=True,
        ),
        bgcolor = ft.colors.WHITE,
        text_size = 12,
        width = 200,
    )
    
    # Botão para atualizar os genes
    botaoEscolherArquivo1 = ft.Container(
        ft.ElevatedButton(
            "Escolher arquivo para busca interna", on_click = lambda _: None, bgcolor = "white", color = "black", 
            adaptive = True, width = 350, height = 30,
            style = ft.ButtonStyle(
                side = {
                    ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLACK),
                }
            ),
        ),                      
    )
    
    botaoEscolherArquivoNCBI = ft.Container(
        ft.ElevatedButton(
            "Buscar no NCBI", on_click = lambda _: funcoes.buscarNoNCBI(page, bancoSelected.value, campoTexto, containerBD), bgcolor = "white", color = "black", 
            adaptive = True, width = 350, height = 30,
            style = ft.ButtonStyle(
                side = {
                    ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLACK),
                }
            ),
        ),   
    )
    
    containerPesquisa = ft.Container(
        content=ft.Column(
        [
            ft.Text("Informações", color="black", size=20, weight=ft.FontWeight.W_600, text_align="CENTER"),
            ft.Row(
                [
                    ft.Container(
                        content = ft.Column(
                            [
                                campoTexto, bancoSelected
                            ]
                        ),
                        alignment=ft.alignment.center,
                        margin = ft.margin.only(left = 30),
                    ),
                    ft.Container(
                        content = ft.Column(
                            [
                               botaoEscolherArquivo1, botaoEscolherArquivoNCBI
                            ],
                        ),
                        alignment=ft.alignment.center,
                        margin = ft.margin.only(left = 30),
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                width = 800,
            ),
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.START,
    ),
    )
    
    #Container dos Meus Genes
    containerMor = ft.Container(
        bgcolor = "#59C9E995",
        width = 1200,
        height = 180,
        border = ft.border.only(bottom = ft.border.BorderSide(1, "black")),
        padding = ft.padding.only(left = 20),
        border_radius = ft.border_radius.BorderRadius(0, 0, 0, 0),
        content = ft.Column(
            [
                containerPesquisa,
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
                    border_radius = ft.border_radius.BorderRadius(20, 0, 20, 0),
                    content = ft.Column(
                        [
                            colunaSuperior, colunaDoMeio,
                        ],
                        horizontal_alignment = ft.CrossAxisAlignment.CENTER, 
                    )
                ),
                ft.Container(
                    bgcolor= "#FFFFFF",
                    alignment=ft.alignment.center,
                    expand=True,
                    border = ft.border.all(0.5, ft.colors.BLACK),
                    border_radius= ft.border_radius.BorderRadius(0, 20, 0, 20),
                    content = ft.Column(
                        [
                            containerMor, containerTextoBD, containerBD
                        ]
                    )
                ),
            ],
            spacing=0,
            expand=True,
    )
    
    page.update()   
    return layoutAll
