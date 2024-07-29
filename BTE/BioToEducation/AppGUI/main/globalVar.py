import sys, os
import arquivos

caminhoDoArquivo = r"C:\Users\Pedro\Desktop\BioProject-WFlet\BTE\BioToEducation\dataNAlgoritm\data\tumorNecrosis\ncbi_dataset\data\tumorNecrosis.fna"
caminhoSegundoArquivo = r"C:\Users\Pedro\Desktop\BioProject-WFlet\BTE\BioToEducation\dataNAlgoritm\data\tumorProtein\ncbi_dataset\data\tumorProtein.fna"

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

