import flet as ft
import layout

def CriarLayoutTranscricao(page: ft.Page):
    def carregarContainers():
        layout.CriarLayout.layoutAll.controls.remove(layout.CriarLayout.containerMeusGenes)
        layout.CriarLayout.layoutAll.controls.remove(layout.CriarLayout.containerTextoSequenciamento)
        layout.CriarLayout.layoutAll.controls.remove(layout.CriarLayout.containerSequenciamento)
        layout.CriarLayout.controls.remove(layout.CriarLayout.sequenciamento)