import flet as ft
import assets, funcoes


def CriarLayoutLogin(page: ft.Page):

    img = ft.Image(
        src=assets.logoBteSCirculo,
        width=500,
        fit=ft.ImageFit.CONTAIN,
        filter_quality="HIGH",
    )

    campoUsuario = ft.TextField(
        label="Usuário:",
        hint_text="Insira seu email",
        color=ft.colors.BLACK,
        fill_color="#D9D9D9",
        border=ft.InputBorder.UNDERLINE,
        filled=True,
        border_color=ft.colors.GREEN,
        focused_border_color=ft.colors.GREEN,
        keyboard_type=ft.KeyboardType.EMAIL,
        width=250,
        hint_style=ft.TextStyle(
            color="#2B2929",
            size=12,
            weight=ft.text.FontWeight.BOLD,
        ),
        label_style=ft.TextStyle(
            color=ft.colors.BLACK,
        ),
    )

    campoSenha = ft.TextField(
        label="Senha:",
        hint_text="Insira sua Senha",
        color=ft.colors.BLACK,
        fill_color="#D9D9D9",
        border=ft.InputBorder.UNDERLINE,
        filled=True,
        border_color=ft.colors.GREEN,
        focused_border_color=ft.colors.GREEN,
        password=True,
        can_reveal_password=True,
        width=250,
        hint_style=ft.TextStyle(
            color="#2B2929",
            size=12,
            weight=ft.text.FontWeight.BOLD,
        ),
        label_style=ft.TextStyle(
            color=ft.colors.BLACK,
        ),
    )

    area = ft.Text()

    botaoEntrar = ft.ElevatedButton(
        text="Entrar",
        on_click=lambda _: funcoes.Entrar(campoUsuario, campoSenha, area, page),
        bgcolor="#83C852",
        color=ft.colors.BLACK,
        style=ft.ButtonStyle(
            side={
                ft.ControlState.DEFAULT: ft.BorderSide(1, ft.colors.BLACK),
            }
        ),
    )

    botaoRegistrar = ft.TextButton(
        text="Não possui conta? Crie aqui",
        on_click=lambda _: funcoes.BotaoPgRegistrar(page),
        style=ft.ButtonStyle(color={ft.ControlState.DEFAULT: ft.colors.BLACK}),
    )

    botaoRecuperarSenha = ft.TextButton(
        text="Esqueceu sua senha? Clique aqui",
        on_click=lambda _: None,
        style=ft.ButtonStyle(color={ft.ControlState.DEFAULT: ft.colors.BLACK}),
    )

    # Container com a imagem e fundo verde à esquerda
    imagem = ft.Container(
        content=img,
        bgcolor="#7CC649",
        border_radius=ft.border_radius.BorderRadius(20, 0, 20, 0),
        width=300,
        height=500,
        alignment=ft.alignment.center,
        padding=ft.Padding(20, 0, 20, 0),  # Ajuste o padding conforme necessário
    )

    # Container com os campos e botões à direita
    coluna = ft.Container(
        content=ft.Column(
            [
                campoUsuario,
                campoSenha,
                botaoEntrar,
                botaoRegistrar,
                botaoRecuperarSenha,
            ],
            alignment=ft.MainAxisAlignment.CENTER,  # Centraliza os campos e botões
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,  # Ajuste o espaçamento entre os elementos
        ),
        bgcolor=ft.colors.WHITE,
        width=350,
        height=500,
        border_radius=ft.border_radius.BorderRadius(0, 20, 0, 20),
        padding=ft.Padding(40, 40, 40, 40),  # Ajuste o padding conforme necessário
    )

    # Layout final combinando imagem e coluna
    layout = ft.Container(
        content=ft.Row(
            [imagem, coluna],
            spacing=0,
        ),
        alignment=ft.alignment.center,
    )

    page.window.full_screen = False
    page.window.maximized = False
    page.window.movable = True
    page.window.focused = True
    page.window.resizable = False
    page.controls.clear()
    page.add(layout)
    page.update()
