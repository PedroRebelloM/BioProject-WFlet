import sys, os
import arquivos


baseDir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

caminhoDoArquivo = os.path.join(baseDir, 'dataNAlgoritm', 'data', 'tumorNecrosis', 'ncbi_dataset', 'data', 'tumorNecrosis.fna')

caminhoSegundoArquivo = os.path.join(baseDir, 'dataNAlgoritm', 'data', 'tumorProtein', 'ncbi_dataset', 'data', 'tumorProtein.fna')
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

