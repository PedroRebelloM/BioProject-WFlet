import flet as ft
import assets, funcoes

def CriarLayoutLogin(page: ft.Page):

    
    campoUsuario = ft.TextField(label="Insira seu Email", keyboard_type=ft.KeyboardType.EMAIL)
    campoSenha = ft.TextField(label="Insira sua senha", password=True, can_reveal_password=True)
    area = ft.Text()

    botaoEnviar = ft.ElevatedButton(text="Enviar", on_click=lambda e: funcoes.click(campoUsuario, campoSenha, area, page))

    layout = ft.Container(
        content=ft.Column(
            [
                campoUsuario,
                campoSenha,
                botaoEnviar,
                area
            ]
        )
    )

    page.add(layout)
    return layout