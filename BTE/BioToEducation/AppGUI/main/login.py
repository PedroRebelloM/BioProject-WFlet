import flet as ft
import assets, funcoes

def CriarLayoutLogin(page: ft.Page):
    campoUsuario = ft.TextField(label="Insira seu Email", keyboard_type=ft.KeyboardType.EMAIL)
    campoSenha = ft.TextField(label="Insira sua senha", password=True, can_reveal_password=True)
    area = ft.Text()

    botaoEntrar = ft.ElevatedButton(text="Entrar", on_click = lambda _: funcoes.Entrar(campoUsuario, campoSenha, area, page))
    botaoRegistrar = ft.ElevatedButton(text="Registrar", on_click = lambda _: funcoes.BotaoPgRegistrar(page))

    layout = ft.Container(
        content=ft.Column(
            [
                campoUsuario,
                campoSenha,
                botaoEntrar,
                botaoRegistrar,
                area
            ]
        )
    )

    page.add(layout)
    return layout
    