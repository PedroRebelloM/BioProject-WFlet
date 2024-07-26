import flet as ft

class EscolherArquivo:
    def __init__(self, page):
        self.page = page
        self.caminhoDoArquivo = ''
        self.caminhoSegundoArquivo = ''
    
    def SelecionarArquivos(self, e):
        # Implementação para escolher arquivos
        file_picker = ft.FilePicker()
        file_picker.on_result = self.on_result
        self.page.dialogs.open(file_picker)

    def Resultado(self, e):
        if e.files:
            # Supondo que estamos pegando o primeiro arquivo
            self.caminhoDoArquivo = e.files[0].path
            # Se há um segundo arquivo
            if len(e.files) > 1:
                self.caminhoSegundoArquivo = e.files[1].path
            else:
                self.caminhoSegundoArquivo = ''
            print(f"Caminho do primeiro arquivo: {self.caminhoDoArquivo}")
            print(f"Caminho do segundo arquivo: {self.caminhoSegundoArquivo}")
            # Feche o dialogo após a seleção
            self.page.dialogs.close()