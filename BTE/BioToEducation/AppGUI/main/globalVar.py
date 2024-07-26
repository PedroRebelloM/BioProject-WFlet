import sys, os
import arquivos

caminhoDoArquivo = ""
caminhoSegundoArquivo = ""

def setCaminhoArquivo(caminho):
    global caminhoDoArquivo
    caminhoDoArquivo = caminho
    
def setCaminhoSegundoArquivo(caminho):
    global caminhoSegundoArquivo
    caminhoSegundoArquivo = caminho
    
def getCaminhoArquivo():
    return caminhoDoArquivo

def getCaminhoSegundoArquivo():
    return caminhoSegundoArquivo
