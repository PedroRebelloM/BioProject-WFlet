from Bio import SeqIO
import globalVar
from AppGUI.main.fix import nomeGene1, nomeGene2

print(nomeGene1)
resultados = {}

def leitura(caminhoDoArquivo):
    #realizando leitura do arquivo fna
    nucleotideo = []
    with open(caminhoDoArquivo, 'r') as dna:
        for sequencia in SeqIO.parse(dna, 'fasta'):
            nucleotideo.append(str(sequencia.seq))
            seQ = str(sequencia.seq)
    return nucleotideo, seQ
        
def transcricao(sequencia):
    transcricaoSeq = []
    contador = 0
    
    for nucleotideo in ''.join(sequencia):  # Unifica todas as sequências e itera diretamente sobre elas
        if nucleotideo == 'T':
            transcricaoSeq.append('A')
        elif nucleotideo == 'A':
            transcricaoSeq.append('U')
        elif nucleotideo == 'G':
            transcricaoSeq.append('C')
        elif nucleotideo == 'C':
            transcricaoSeq.append('G')
        contador += 1  # Contador agora é incrementado aqui, não precisa ser incrementado em cada condição

    genoma = ''.join(transcricaoSeq)  # Cocatena os nucleotídeos em uma única string.
    return genoma, contador


# Método responsável pela tradução
def traducao(rnaMensageiro):
    # Dicionário para mapear códons a aminoácidos
    dicionarioDeCodon = {
        'AUG': 'Met',
        'AUC': 'Ile', 'AUU': 'Ile', 'AUA': 'Ile',
        'UCG': 'Ser', 'UCA': 'Ser', 'UCC': 'Ser', 'UCU': 'Ser',
        'AGU': 'Ser', 'AGC': 'Ser',
        'UUU': 'Phe', 'UUC': 'Phe',
        'UUA': 'Leu', 'UUG': 'Leu',
        'GUU': 'Val', 'GUC': 'Val', 'GUA': 'Val', 'GUG': 'Val',
        'CUU': 'Leu', 'CUC': 'Leu', 'CUA': 'Leu', 'CUG': 'Leu',
        'CCU': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro', 'CCG': 'Pro',
        'ACU': 'Thr', 'ACC': 'Thr', 'ACA': 'Thr', 'ACG': 'Thr',
        'GCU': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala', 'GCG': 'Ala',
        'UAU': 'Tyr', 'UAC': 'Tyr',
        'CAU': 'His', 'CAC': 'His',
        'CAA': 'Gln', 'CAG': 'Gln',
        'AAU': 'Asn', 'AAC': 'Asn',
        'AAA': 'Lys', 'AAG': 'Lys',
        'GAU': 'Asp', 'GAC': 'Asp',
        'GAA': 'Glu', 'GAG': 'Glu',
        'UGU': 'Cys', 'UGC': 'Cys',
        'UGG': 'Trp',
        'CGU': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg', 'CGG': 'Arg',
        'AGA': 'Arg', 'AGG': 'Arg',
        'GGU': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly', 'GGG': 'Gly',
        'UAA': 'Parada', 'UAG': 'Parada', 'UGA': 'Parada'
    }
    
    sinteseProteica = []
    proteinasConcatenadas = []
    
    for x in range(0, len(rnaMensageiro), 3):  # Iterador para dividir as bases de 3 em 3, formando os códons
        codon = rnaMensageiro[x:x + 3]  # Pega o códon formado
        if codon in dicionarioDeCodon:
            sinteseProteica.append(dicionarioDeCodon[codon])
        
        # Concatena as strings retornadas pela sinteseProteica  
        proteinasConcatenadas.append(' - '.join(sinteseProteica))
        sinteseProteica = []

    sobra = len(rnaMensageiro) % 3  # Verifica se sobram bases nitrogenadas
    if sobra == 1:
        proteinasConcatenadas.append(rnaMensageiro[-1])
    elif sobra == 2:
        proteinasConcatenadas.append(rnaMensageiro[-2:])
    
    proteinas = ' - '.join(proteinasConcatenadas)
    
    return proteinas

 
def compararDna(nucleotideo, nucleotideoDois):
    
    # Determina a maior sequência e sua correspondente
    if len(nucleotideo) > len(nucleotideoDois):
        maiorDna = nucleotideo
        nomeMaiorDna = nomeGene1
        menorDna = nucleotideoDois
        nomeMenorDna = nomeGene2
    elif len(nucleotideo) < len(nucleotideoDois):
        maiorDna = nucleotideoDois
        nomeMaiorDna = nomeGene2
        menorDna = nucleotideo
        nomeMenorDna = nomeGene1
    else: 
        nomeMaiorDna = "Possuem o mesmo tamanho"
        nomeMenorDna = "Possuem o mesmo"

    # Inicializa uma string para armazenar o resultado do alinhamento
    resultadoAlinhadoDna = ''
    contador = 0
    # Percorre cada posição na sequência mais longa
    for i in range(len(maiorDna)):
        # Verifica se a posição está dentro do comprimento da outra sequência
        if i < len(menorDna):
            # Verifica se os nucleotídeos correspondentes são iguais
            if maiorDna[i] == menorDna[i]:
                resultadoAlinhadoDna += maiorDna[i]
                contador += 1
            else:
                resultadoAlinhadoDna += '-'  # Se são iguais, adiciona o nucleotídeo à sequência alinhada
        else:
            resultadoAlinhadoDna += '-'  # Adiciona um traço à sequência alinhada para as posições além do comprimento da outra sequência
            
        tamanhoMaior = len(maiorDna)
        tamanhoMenor = len(menorDna)
        porcentagemMaiorDna = round(contador * 100 / tamanhoMaior, 2)
        porcentagemMenorDna = round(contador * 100 / tamanhoMenor, 2)
        
    
    resultado = f"Porcentagem de semelhança:\n\nMaior DNA: {nomeMaiorDna}\nMenor DNA: {nomeMenorDna}\n\nPorcentagem em relação ao {nomeMaiorDna}: {porcentagemMaiorDna}%\n\nPorcentagem em relação ao {nomeMenorDna}: {porcentagemMenorDna}%"
    return resultadoAlinhadoDna, resultado

    
def compararRna(rnaMensageiroString, rnaMensageiroString2):
    
    # Determina a maior sequência e sua correspondente
    if len(rnaMensageiroString) > len(rnaMensageiroString2):
        maiorRna = rnaMensageiroString
        nomeMaiorRna = nomeGene1
        menorRna = rnaMensageiroString2
        nomeMenorRna = nomeGene2
    elif len(rnaMensageiroString) < len(rnaMensageiroString2):
        maiorRna = rnaMensageiroString2
        nomeMaiorRna = nomeGene2
        menorRna = rnaMensageiroString
        nomeMenorRna = nomeGene1
    else: 
        nomeMaiorRna = "Possuem o mesmo tamanho"
        nomeMenorRna = "Possuem o mesmo tamanho"

    # Inicializa uma string para armazenar o resultado do alinhamento
    resultadoAlinhadoRna = ''
    contador = 0
    # Percorre cada posição na sequência mais longa
    for i in range(len(maiorRna)):
        # Verifica se a posição está dentro do comprimento da outra sequência
        if i < len(menorRna):
            # Verifica se os nucleotídeos correspondentes são iguais
            if maiorRna[i] == menorRna[i]:
                resultadoAlinhadoRna += maiorRna[i]  # Se são iguais, adiciona o nucleotídeo à sequência alinhada
                contador += 1
            else:
                resultadoAlinhadoRna += '-'  # Se são diferentes, adiciona um traço à sequência alinhada
        else:
            resultadoAlinhadoRna += '-'
            # Adiciona um traço à sequência alinhada para as posições além do comprimento da outra sequência
            
        tamanhoMaior = len(maiorRna)
        tamanhoMenor = len(menorRna)
        porcentagemMaiorRna = round(contador * 100 / tamanhoMaior, 2) # Arredonda o valor e realiza a porcentagem de
        porcentagemMenorRna = round(contador * 100 / tamanhoMenor, 2) # similaridade
        
    
    
    resultado = f"Porcentagem de semelhança:\n\nMaior RNA: {nomeMaiorRna}\nMenor RNA: {nomeMenorRna}\n\nPorcentagem em relação ao {nomeMaiorRna}: {porcentagemMaiorRna}%\n\nPorcentagem em relação ao {nomeMenorRna}: {porcentagemMenorRna}%"
    return resultadoAlinhadoRna, resultado

def compararProteinas(cadeiaProteica, cadeiaProteica2):
    # Determina a maior e menor cadeia de proteínas
    if len(cadeiaProteica) > len(cadeiaProteica2):
        maiorCadeiaProteica = cadeiaProteica
        menorCadeia = cadeiaProteica2
        nomeMaiorCadeia = nomeGene1
        nomeMenorCadeia = nomeGene2
    elif len(cadeiaProteica) < len(cadeiaProteica2):
        maiorCadeiaProteica = cadeiaProteica2
        menorCadeia = cadeiaProteica
        nomeMaiorCadeia = nomeGene2
        nomeMenorCadeia = nomeGene1
    else:
        return "As cadeias de proteínas possuem o mesmo tamanho."

    resultadoAlinhadoProteinas = ''
    contador = 0

    # Criação do alinhamento
    for i in range(len(maiorCadeiaProteica)):
        if i < len(menorCadeia):
            if maiorCadeiaProteica[i] == menorCadeia[i]:
                resultadoAlinhadoProteinas += maiorCadeiaProteica[i]  # Aminoácido igual
                contador += 1
            else:
                resultadoAlinhadoProteinas += '-'  # Aminoácidos diferentes
        else:
            resultadoAlinhadoProteinas += '-'  # Posições restantes da maior cadeia

    # Criação do alinhamento da segunda cadeia
    resultadoAlinhadoMenor = ''
    for i in range(len(maiorCadeiaProteica)):
        if i < len(menorCadeia):
            if maiorCadeiaProteica[i] != menorCadeia[i]:
                resultadoAlinhadoMenor += menorCadeia[i]  # Aminoácido da menor cadeia
            else:
                resultadoAlinhadoMenor += '-'  # Para manter o alinhamento

    # Cálculo das porcentagens de semelhança
    tamanhoMaior = len(maiorCadeiaProteica)
    porcentagemMaiorCadeia = round(contador * 100 / tamanhoMaior, 2)

    resultado = (f"Porcentagem de semelhança:\n\n"
                 f"Maior proteína: {nomeMaiorCadeia}\n"
                 f"Menor proteína: {nomeMenorCadeia}\n\n"
                 f"Porcentagem em relação ao {nomeMaiorCadeia}: {porcentagemMaiorCadeia}%")

    return resultadoAlinhadoProteinas, resultado
    

def mainAlgoritm():
    caminhoDoArquivo = globalVar.getCaminhoArquivo()
    caminhoSegundoArquivo = globalVar.getCaminhoSegundoArquivo()
    
    nucleotideo, seQ = leitura(caminhoDoArquivo)
    nucleotideoDois, seQ2 = leitura(caminhoSegundoArquivo)
    
    rnaMensageiroString, nmr1 = transcricao(seQ)
    rnaMensageiroString2, nmr2 = transcricao(seQ2)
    
    proteinasA = traducao(rnaMensageiroString)
    proteinasB = traducao(rnaMensageiroString2)
    
    cadeiaProteica = traducao(proteinasA)
    cadeiaProteica2 = traducao(proteinasB)
   
    resultadoAlinhamentoDna, comparacaoDna = compararDna(seQ, seQ2)
    resultadoAlinhamentoRna, comparacaoRna = compararRna(rnaMensageiroString, rnaMensageiroString2)
    
    resultadoAlinhamentoProteinas, comparacaoProteina = compararProteinas(cadeiaProteica, cadeiaProteica2)
    
    return {
        'sequencia1': seQ,
        'sequencia2': seQ2,
        'rna1': rnaMensageiroString,
        'rna2': rnaMensageiroString2,
        'proteinasA': proteinasA,
        'proteinasB': proteinasB,
        'alinhamentoDna': resultadoAlinhamentoDna,
        'alinhamentoRna': resultadoAlinhamentoRna,
        'alinhamentoProteinas': resultadoAlinhamentoProteinas,   
        'porcentagemDna': comparacaoDna,
        'porcentagemRna': comparacaoRna,
        'porcentagemProteinas': comparacaoProteina
    }

def atualizarResultados():
    global resultados
    resultados = mainAlgoritm()

def returnSequencia():
    return resultados.get('sequencia1', 'Resultados não encontraodos')

def returnSequencia2():
    return resultados.get('sequencia2', 'Resultados não encontraodos')

def returnRna1():
    return resultados.get('rna1', 'Resultados não encontraodos')

def returnRna2():
    return resultados.get('rna2', 'Resultados não encontraodos')

def returnProteinasA():
    return resultados.get('proteinasA', 'Resultados não encontraodos')

def returnProteinasB():
    return resultados.get('proteinasB', 'Resultados não encontraodos')

def returnPorcentagemDna():
    return resultados.get('porcentagemDna', 'Resultados não encontraodos')

def returnPorcentagemRna():
    return resultados.get('porcentagemRna', 'Resultados não encontraodos')

def returnPorcentagemProteinas():
    return resultados.get('porcentagemProteinas')

def returnAlinhamentoDna():
    return resultados.get('alinhamentoDna', 'Resultados não encontraodos')

def returnAlinhamentoRna():
    return resultados.get('alinhamentoRna', 'Resultados não encontraodos')

def returnAlinhamentoProteinas():
    return resultados.get('alinhamentoProteinas', 'Resultados não encontrados')

atualizarResultados()
