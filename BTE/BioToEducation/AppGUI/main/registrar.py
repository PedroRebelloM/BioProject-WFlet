import flet as ft
import assets, funcoes

def CriarLayoutRegistro(page: ft.Page):    
    campoUsuario = ft.TextField(label="Insira seu Email", keyboard_type=ft.KeyboardType.EMAIL)
    campoSenha = ft.TextField(label="Insira sua senha", password=True, can_reveal_password=True)
    campoConfirmar = ft.TextField(label="Repita sua senha", password=True, can_reveal_password=True)
    area = ft.Text()
    
    botaoRegistrar = ft.ElevatedButton(text="Registrar", on_click=lambda _: funcoes.Registrar(campoUsuario, campoSenha, campoConfirmar, area, page))
    botaoRetornar = ft.ElevatedButton(text="Retornar ao Login", on_click=lambda _: funcoes.Retornar(page))

    layout = ft.Container(
        content=ft.Column(
            [
                campoUsuario,
                campoSenha,
                campoConfirmar,
                botaoRegistrar,
                botaoRetornar,
                area
            ]
        )
    )

    page.add(layout)
    return layout