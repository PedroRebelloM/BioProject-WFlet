import flet as ft
import assets, funcoes

def CriarLayoutRegistro(page: ft.Page):    
    campoNome = ft.TextField(label="Insira seu Nome", keyboard_type=ft.KeyboardType.EMAIL)
    campoInstituicao = ft.TextField(label="Insira sua Insituição", keyboard_type=ft.KeyboardType.EMAIL)
    campoCargo = ft.TextField(label="Insira o cargo ocupante na Instituição", keyboard_type=ft.KeyboardType.EMAIL)
    campoUsuario = ft.TextField(label="Insira seu Email", keyboard_type=ft.KeyboardType.EMAIL)
    campoSenha = ft.TextField(label="Insira sua senha", password=True, can_reveal_password=True)
    campoConfirmar = ft.TextField(label="Repita sua senha", password=True, can_reveal_password=True)
    area = ft.Text()
    
    botaoRegistrar = ft.ElevatedButton(text="Registrar", on_click=lambda _: funcoes.Registrar(campoNome, campoInstituicao, campoCargo, campoUsuario, campoSenha, campoConfirmar, area, page))
    botaoRetornar = ft.ElevatedButton(text="Retornar ao Login", on_click=lambda _: funcoes.Retornar(page))

    layout = ft.Container(
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
                area
            ]
        ) 
    ) 

    page.controls.clear()
    page.add(layout)
    page.update()

    