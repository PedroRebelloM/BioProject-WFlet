import flet as ft
import assets, funcoes


def CriarLayoutRegistro(page: ft.Page):
    img = ft.Image(
        src=assets.logoBteSCirculo,
        width=400,
        fit=ft.ImageFit.CONTAIN,
        filter_quality="HIGH",
    )

    campoNome = ft.TextField(
        label="Insira seu Nome",
        keyboard_type=ft.KeyboardType.EMAIL,
        color=ft.colors.BLACK,
        fill_color="#D9D9D9",
        border=ft.InputBorder.UNDERLINE,
        filled=True,
        border_color=ft.colors.GREEN,
        focused_border_color=ft.colors.GREEN,
        width=250,
        height=50,
        cursor_color=ft.colors.TRANSPARENT,
        hint_style=ft.TextStyle(
            color="#2B2929",
            size=12,
            weight=ft.text.FontWeight.BOLD,
        ),
        label_style=ft.TextStyle(
            color=ft.colors.BLACK,
        ),
    )

    campoInstituicao = ft.TextField(
        label="Insira sua Instituição",
        color=ft.colors.BLACK,
        fill_color="#D9D9D9",
        border=ft.InputBorder.UNDERLINE,
        filled=True,
        border_color=ft.colors.GREEN,
        focused_border_color=ft.colors.GREEN,
        width=250,
        height=50,
        cursor_color=ft.colors.TRANSPARENT,
        hint_style=ft.TextStyle(
            color="#2B2929",
            size=12,
            weight=ft.text.FontWeight.BOLD,
        ),
        label_style=ft.TextStyle(
            color=ft.colors.BLACK,
        ),
    )

    campoCargo = ft.TextField(
        label="Insira o cargo ocupante na Instituição",
        color=ft.colors.BLACK,
        fill_color="#D9D9D9",
        border=ft.InputBorder.UNDERLINE,
        filled=True,
        border_color=ft.colors.GREEN,
        focused_border_color=ft.colors.GREEN,
        width=250,
        height=50,
        cursor_color=ft.colors.TRANSPARENT,
        hint_style=ft.TextStyle(
            color="#2B2929",
            size=12,
            weight=ft.text.FontWeight.BOLD,
        ),
        label_style=ft.TextStyle(
            color=ft.colors.BLACK,
        ),
    )

    campoUsuario = ft.TextField(
        label="Insira seu Email",
        color=ft.colors.BLACK,
        fill_color="#D9D9D9",
        border=ft.InputBorder.UNDERLINE,
        filled=True,
        border_color=ft.colors.GREEN,
        focused_border_color=ft.colors.GREEN,
        width=250,
        height=50,
        cursor_color=ft.colors.TRANSPARENT,
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
        label="Insira sua senha",
        password=True,
        can_reveal_password=True,
        color=ft.colors.BLACK,
        fill_color="#D9D9D9",
        border=ft.InputBorder.UNDERLINE,
        filled=True,
        border_color=ft.colors.GREEN,
        focused_border_color=ft.colors.GREEN,
        width=250,
        height=50,
        cursor_color=ft.colors.TRANSPARENT,
        hint_style=ft.TextStyle(
            color="#2B2929",
            size=12,
            weight=ft.text.FontWeight.BOLD,
        ),
        label_style=ft.TextStyle(
            color=ft.colors.BLACK,
        ),
    )

    campoConfirmar = ft.TextField(
        label="Repita sua senha",
        password=True,
        can_reveal_password=True,
        color=ft.colors.BLACK,
        fill_color="#D9D9D9",
        border=ft.InputBorder.UNDERLINE,
        filled=True,
        border_color=ft.colors.GREEN,
        focused_border_color=ft.colors.GREEN,
        width=250,
        height=50,
        cursor_color=ft.colors.TRANSPARENT,
        hint_style=ft.TextStyle(
            color="#2B2929",
            size=12,
            weight=ft.text.FontWeight.BOLD,
        ),
        label_style=ft.TextStyle(
            color=ft.colors.BLACK,
        ),
    )

    area = ft.Text(color=ft.colors.BLACK)

    botaoRegistrar = ft.ElevatedButton(
        text="Registrar",
        on_click=lambda _: funcoes.Registrar(
            campoNome,
            campoInstituicao,
            campoCargo,
            campoUsuario,
            campoSenha,
            campoConfirmar,
            area,
            page,
        ),
        bgcolor="#83C852",
        color=ft.colors.BLACK,
        style=ft.ButtonStyle(
            side={
                ft.ControlState.DEFAULT: ft.BorderSide(1, ft.colors.BLACK),
            }
        ),
        height=50,
    )

    botaoRetornar = ft.ElevatedButton(
        text="Retornar ao Login",
        on_click=lambda _: funcoes.Retornar(page),
        bgcolor="#83C852",
        color=ft.colors.BLACK,
        style=ft.ButtonStyle(
            side={
                ft.ControlState.DEFAULT: ft.BorderSide(1, ft.colors.BLACK),
            }
        ),
        height=50,
    )

    coluna = ft.Container(
        content=ft.Column(
            [
                campoNome,
                campoInstituicao,
                campoCargo,
                campoUsuario,
                campoSenha,
                campoConfirmar,
                botaoRegistrar,
                botaoRetornar,
                area,  # Adicionando a área ao layout
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15,
        ),
        bgcolor=ft.colors.WHITE,
        width=350,
        height=540,
        border_radius=ft.border_radius.BorderRadius(0, 20, 0, 20),
        padding=ft.Padding(30, 30, 30, 30),
    )

    imagem = ft.Container(
        content=img,
        bgcolor="#7CC649",
        border_radius=ft.border_radius.BorderRadius(20, 0, 20, 0),
        width=250,
        height=540,
        alignment=ft.alignment.center,
        padding=ft.Padding(20, 50, 20, 50),
    )

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
