import flet as ft
import assets, funcoes, fix


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

    # Logo BTE
    img = ft.Image(
        src=assets.logoBTE,
        width=200,
        height=200,
        fit=ft.ImageFit.CONTAIN,
        filter_quality="HIGH",
    )

    # Sequencia dos ícones
    botaoHome = ft.ElevatedButton(
        "Home",
        icon="home",
        icon_color="black",
        on_click=lambda _: funcoes.Home(page),
        bgcolor="white",
        color="black",
        style=ft.ButtonStyle(
            side={
                ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLACK),
            }
        ),
        adaptive=True,
        width=160,
    )

    botaoRna = ft.ElevatedButton(
        "Transcrição",
        icon="CELL_TOWER",
        icon_color="black",
        on_click=lambda _: funcoes.Transcricao(page),
        bgcolor="white",
        color="black",
        style=ft.ButtonStyle(
            side={
                ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLACK),
            }
        ),
        adaptive=True,
        width=160,
    )

    botaoDna = ft.ElevatedButton(
        "Tradução",
        icon="translate",
        icon_color="black",
        on_click=lambda _: funcoes.Traducao(page),
        bgcolor="white",
        color="black",
        style=ft.ButtonStyle(
            side={
                ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLACK),
            }
        ),
        adaptive=True,
        width=160,
    )

    botaoComparacao = ft.ElevatedButton(
        "Comparação",
        icon="percent",
        icon_color="black",
        on_click=lambda _: funcoes.Comparacao(page),
        bgcolor="white",
        color="black",
        style=ft.ButtonStyle(
            side={
                ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLACK),
            }
        ),
        adaptive=True,
        width=160,
    )

    botaoEscolhaArquivo = ft.ElevatedButton(
        "Arquivos",
        icon="ATTACH_FILE",
        icon_color="black",
        on_click=lambda _: funcoes.PgArquivos(page),
        bgcolor="white",
        color="black",
        style=ft.ButtonStyle(
            side={
                ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLACK),
            }
        ),
        adaptive=True,
        width=160,
    )

    botaoActionBd = ft.ElevatedButton(
        "Database",
        icon="CLOUD_UPLOAD",
        icon_color="black",
        on_click=lambda _: funcoes.BancoDeDados(page),
        bgcolor="white",
        color="black",
        style=ft.ButtonStyle(
            side={
                ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLACK),
            }
        ),
        adaptive=True,
        width=160,
    )

    botaoPesquisar = ft.ElevatedButton(
        "Pesquisar",
        icon="SCREEN_SEARCH_DESKTOP_OUTLINED",
        icon_color="black",
        on_click=lambda _: funcoes.Pesquisar(page),
        bgcolor="white",
        color="black",
        style=ft.ButtonStyle(
            side={
                ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLACK),
            }
        ),
        adaptive=True,
        width=160,
    )

    botaoLogout = ft.ElevatedButton(
        "Logout",
        icon="logout",
        icon_color="black",
        on_click=lambda _: funcoes.Retornar(page),
        bgcolor="white",
        color="black",
        style=ft.ButtonStyle(
            side={ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLACK)}
        ),
        adaptive=True,
        width=160,
    )

    # Divisao dos icones e logo
    colunaSuperior = ft.Column(
        [img],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.START,
    )

    colunaDoMeio = ft.Column(
        [
            botaoHome,
            botaoRna,
            botaoDna,
            botaoComparacao,
            botaoEscolhaArquivo,
            botaoActionBd,
            botaoPesquisar,
            botaoLogout,
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,
        spacing=20,
    )

    textoSeq = ft.Text(
        "Sequenciamento Transcrito:",
        size=20,
        weight=ft.FontWeight.W_600,
        italic=True,
        color="black",
    )

    containerTextoSequenciamento = ft.Container(
        content=textoSeq, margin=ft.margin.only(left=25)
    )

    linha = ft.Column(
        [ft.Text("", color="black", width=900)],
        scroll=ft.ScrollMode.ALWAYS,
    )

    containerSequenciamento = ft.Container(
        width=1000,
        height=420,
        bgcolor="#B5E995",
        border=ft.border.all(1, "black"),
        border_radius=ft.border_radius.all(20),
        margin=ft.margin.only(left=20),
        alignment=ft.alignment.top_left,
        content=linha,
        data="",
        padding=25,
    )

    # Botao do Gene A
    botaoPrimeiroGene = ft.ElevatedButton(
        text=fix.nomeGene1,
        bgcolor="white",
        color="black",
        style=ft.ButtonStyle(
            side={
                ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLACK),
            }
        ),
        adaptive=True,
        width=400,
        height=30,
        on_click=lambda _: funcoes.BotaoATranscricao(linha),
    )

    # Botao do Gene B
    botaoSegundoGene = ft.ElevatedButton(
        text=fix.nomeGene2,
        bgcolor="white",
        color="black",
        style=ft.ButtonStyle(
            side={
                ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLACK),
            }
        ),
        adaptive=True,
        width=400,
        height=30,
        on_click=lambda _: funcoes.BotaoBTranscricao(linha),
    )

    # Botão para atualizar os genes
    BotaoCopiarA = ft.Container(
        ft.ElevatedButton(
            f"Copiar transcrição {fix.nomeGene1}",
            on_click=lambda _: funcoes.CopiarTranscricaoA(linha, page),
            bgcolor="white",
            color="black",
            adaptive=True,
            height=30,
            style=ft.ButtonStyle(
                side={
                    ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLACK),
                }
            ),
        ),
    )

    BotaoCopiarB = ft.Container(
        ft.ElevatedButton(
            f"Copiar transcrição {fix.nomeGene2}",
            on_click=lambda _: funcoes.CopiarTranscricaoB(linha, page),
            bgcolor="white",
            color="black",
            adaptive=True,
            height=30,
            style=ft.ButtonStyle(
                side={
                    ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLACK),
                }
            ),
        ),
    )

    containerDoisGenes = ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "Meus Genes",
                    color="black",
                    size=20,
                    weight=ft.FontWeight.W_600,
                    text_align="CENTER",
                ),
                ft.Row(
                    [
                        ft.Column(
                            [botaoPrimeiroGene, botaoSegundoGene],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=5,
                        ),
                        ft.Container(
                            content=ft.Column(
                                [BotaoCopiarA, BotaoCopiarB],
                            ),
                            alignment=ft.alignment.center,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    width=800,
                ),
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.START,
        ),
    )

    containerMeusGenes = ft.Container(
        bgcolor="#59C9E995",
        width=1400,
        height=150,
        padding=ft.padding.only(left=20),
        border=ft.border.only(bottom=ft.border.BorderSide(1, "black")),
        border_radius=ft.border_radius.BorderRadius(0, 0, 0, 0),
        content=ft.Column(
            [
                containerDoisGenes,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.START,
        ),
    )

    layoutAll = ft.Row(
        [
            ft.VerticalDivider(),
            ft.Container(
                bgcolor="#A1FF0A",
                expand=False,
                width=180,
                border=ft.border.all(0.5, ft.colors.BLACK),
                border_radius=ft.border_radius.BorderRadius(20, 0, 20, 0),
                content=ft.Column(
                    [
                        colunaSuperior,
                        colunaDoMeio,
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ),
            ft.Container(
                bgcolor="#FFFFFF",
                alignment=ft.alignment.center,
                expand=True,
                border=ft.border.all(0.5, ft.colors.BLACK),
                border_radius=ft.border_radius.BorderRadius(0, 20, 0, 20),
                content=ft.Column(
                    [
                        containerMeusGenes,
                        containerTextoSequenciamento,
                        containerSequenciamento,
                    ]
                ),
            ),
        ],
        spacing=0,
        expand=True,
    )

    page.add(layoutAll)
    page.update()
