from Bio import SeqIO
import globalVar, fix

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
    genomaTranscrito = []
    transcricaoSeq = []
    contador = 0
    for seq in sequencia: # Inteirando sobre o arquivo fasta
        for nucleotideo in seq:# Inteirando no método transcrição # n²
            if nucleotideo == 'T':
                transcricaoSeq.append('A')
                contador += 1
            elif nucleotideo == 'A':
                transcricaoSeq.append('U')
                contador += 1
            elif nucleotideo == 'G':
                transcricaoSeq.append('C')
                contador += 1
            elif nucleotideo == 'C':
                transcricaoSeq.append('G')
                contador += 1
    genomaTranscrito.append(''.join(transcricaoSeq)) # Cocatena os nucleotídeos em uma única string.
    genoma = ''.join(genomaTranscrito)
    return genoma, contador

#Método responsável pela tradução
def traducao(rnaMensageiro):
    sinteseProteica = []
    proteinasConcatenadas = []
    cont = 0
    for x in range(0, len(rnaMensageiro), 3):  # Iterador para dividir as bases de 3 em 3, formando os códons
        codon = rnaMensageiro[x:x + 3]  # Pega o códon formado
        if codon == 'AUG':  # condição para formação das proteínas
            sinteseProteica.append('Met')
            cont += 1
        elif codon in ['AUC', 'AUU', 'AUA']:
            sinteseProteica.append('Ile')  # Verifica qual é a sequencia do codon e adiciona a proteina de acordo.
            cont += 1
        elif codon in ['UCG', 'UCA', 'UCC', 'UCU', 'AGU', 'AGC']:
            sinteseProteica.append('Ser')
            cont += 1
        elif codon in ['UUU', 'UUC']:
            sinteseProteica.append('Phe')
            cont += 1
        elif codon in ['UUA', 'UUG']:
            sinteseProteica.append('Leu')
            cont += 1
        elif codon in ['GUU', 'GUC', 'GUA', 'GUG']:
            sinteseProteica.append('Val')
            cont += 1
        elif codon in ['CUU', 'CUC', 'CUA', 'CUG']:
            cont += 1
            sinteseProteica.append('Leu')
        elif codon in ['CCU', 'CCC', 'CCA', 'CCG']:
            cont += 1
            sinteseProteica.append('Pro')
        elif codon in ['ACU', 'ACC', 'ACA', 'ACG']:
            cont += 1
            sinteseProteica.append('Thr')
        elif codon in ['GCU', 'GCC', 'GCA', 'GCG']:
            cont += 1
            sinteseProteica.append('Ala')
        elif codon in ['UAU', 'UAC']:
            cont += 1
            sinteseProteica.append('Tyr') 
        elif codon in ['CAU', 'CAC']:
            cont += 1
            sinteseProteica.append('His')
        elif codon in ['CAA', 'CAG']:
            cont += 1
            sinteseProteica.append('Gln')
        elif codon in ['AAU', 'AAC']:
            cont += 1
            sinteseProteica.append('Asn')
        elif codon in ['AAA', 'AAG']:
            cont += 1
            sinteseProteica.append('Lys')
        elif codon in ['GAU', 'GAC']:
            cont += 1
            sinteseProteica.append('Asp')
        elif codon in ['GAA', 'GAG']:
            cont += 1
            sinteseProteica.append('Glu')
        elif codon in ['UGU', 'UGC']:
            cont += 1
            sinteseProteica.append('Cys')
        elif codon == 'UGG':
            cont += 1
            sinteseProteica.append('Trp')
        elif codon in ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG']:
            cont += 1
            sinteseProteica.append('Arg')
        elif codon in ['GGU', 'GGC', 'GGA', 'GGG']:
            cont += 1
            sinteseProteica.append('Gly')
        elif codon in ['UAA', 'UAG', 'UGA']:
            cont += 1
            sinteseProteica.append('Parada')
        
        #Concatena as strings retornadas pela sinteseProteica  
        proteinasConcatenadas.append(''.join(sinteseProteica))
        sinteseProteica = []
        contador = cont
        
    sobra = len(rnaMensageiro) % 3 # Verifica se sobram bases nitrogenadas
    if sobra == 1:
        sobra1 = rnaMensageiro[-1]
        proteinasConcatenadas.append(sobra1)
    elif sobra == 2:
        sobra2 = rnaMensageiro[-2:]
        proteinasConcatenadas.append(''.join(sobra2))

    proteinas = ' - '.join(proteinasConcatenadas)
    
    return proteinas
 
def compararDna(nucleotideo, nucleotideoDois):
    
    # Determina a maior sequência e sua correspondente
    if len(nucleotideo) >= len(nucleotideoDois):
        maiorDna = nucleotideo
        menorDna = nucleotideoDois
    else:
        maiorDna = nucleotideoDois
        menorDna = nucleotideo

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
        
    
    resultado = f"Porcentagem em relação ao maior DNA: {porcentagemMaiorDna}%\n\nPorcentagem em relação ao menor DNA: {porcentagemMenorDna}%" 
    return resultadoAlinhadoDna, resultado

    
def compararRna(rnaMensageiroString, rnaMensageiroString2):
    
    # Determina a maior sequência e sua correspondente
    if len(rnaMensageiroString) >= len(rnaMensageiroString2):
        maiorRna = rnaMensageiroString
        menorRna = rnaMensageiroString2
    else:
        maiorRna = rnaMensageiroString2
        menorRna = rnaMensageiroString

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
            resultadoAlinhadoRna += '-'  # Adiciona um traço à sequência alinhada para as posições além do comprimento da outra sequência
            
        tamanhoMaior = len(maiorRna)
        tamanhoMenor = len(menorRna)
        porcentagemMaiorRna = round(contador * 100 / tamanhoMaior, 2) # Arredonda o valor e realiza a porcentagem de
        porcentagemMenorRna = round(contador * 100 / tamanhoMenor, 2) # similaridade
        
    
    resultado = f"Porcentagem em relação ao maior RNA: {porcentagemMaiorRna}%\n\nPorcentagem em relação ao menor RNA: {porcentagemMenorRna}%"
    
    return resultadoAlinhadoRna, resultado

def mainAlgoritm():
    caminhoDoArquivo = globalVar.getCaminhoArquivo()
    caminhoSegundoArquivo = globalVar.getCaminhoSegundoArquivo()
    
    nucleotideo, seQ = leitura(caminhoDoArquivo)
    nucleotideoDois, seQ2 = leitura(caminhoSegundoArquivo)
    
    rnaMensageiroString, nmr1 = transcricao(nucleotideo)
    rnaMensageiroString2, nmr2 = transcricao(nucleotideoDois)
    
    proteinasA = traducao(rnaMensageiroString)
    proteinasB = traducao(rnaMensageiroString2)
    
    resultadoAlinhamentoDna, comparacaoDna = compararDna(seQ, seQ2)
    resultadoAlinhamentoRna, comparacaoRna = compararRna(rnaMensageiroString, rnaMensageiroString2)
    
    return {
        'sequencia1': seQ,
        'sequencia2': seQ2,
        'rna1': rnaMensageiroString,
        'rna2': rnaMensageiroString2,
        'proteinasA': proteinasA,
        'proteinasB': proteinasB,
        'alinhamentoDna': resultadoAlinhamentoDna,
        'alinhamentoRna': resultadoAlinhamentoRna,
        'porcentagemDna': comparacaoDna,
        'porcentagemRna': comparacaoRna
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

def returnAlinhamentoDna():
    return resultados.get('alinhamentoDna', 'Resultados não encontraodos')

def returnAlinhamentoRna():
    return resultados.get('alinhamentoRna', 'Resultados não encontraodos')

atualizarResultados()
