from Bio import SeqIO
from Bio.Align import PairwiseAligner
from Bio.pairwise2 import format_alignment

#setando caminho do arquivo

caminhoDoArquivo = r'C:\Users\Pedro\Desktop\BioProject-WFlet\BTE\dataNAlgoritm\data\tumorNecrosis\ncbi_dataset\data\gene.fna'
caminhoSegundoArquivo = r'C:\Users\Pedro\Desktop\BioProject-WFlet\BTE\dataNAlgoritm\data\tumorProtein\ncbi_dataset\data\gene.fna'

#realizando leitura do arquivo fna
nucleotideo = []
with open(caminhoDoArquivo, 'r') as dna:
    for sequencia in SeqIO.parse(dna, 'fasta'):
        nucleotideo.append(str(sequencia.seq))
        seQ = str(sequencia.seq)


nucleotideoDois = []
with open(caminhoSegundoArquivo, 'r') as dna2:
    for sequenciaDois in SeqIO.parse(dna2, 'fasta'):
        nucleotideoDois.append(str(sequenciaDois.seq))
        seQ2 = str(sequenciaDois.seq)
        
# def lerSequencia(caminho):
#     nuc = []
#     with open(caminho, 'r') as dnA:
#         for seque in SeqIO.parse(dnA, 'fasta'):
#             nuc.append(str(seque.seq))
#     return nuc

# a = lerSequencia(caminhoDoArquivo)
# b = lerSequencia(caminhoSegundoArquivo)
         
         
# Método responsável pela transcrição
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

rnaMensageiroString, nmr1 = transcricao(nucleotideo) # Primeira  variável atribuida para cada base nitrogenada, e a segunda variável
rnaMensageiroString2, nmr2 = transcricao(nucleotideoDois) # atribuida para as bases nitrogenadas concatenadas

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

#Assume o valor retornado pela função de tradução
proteinasA = traducao(rnaMensageiroString)
proteinasB = traducao(rnaMensageiroString2)

#Método responsável pela comparação
def comparador(nucleotideo, nucleotideoDois):
    nucleotideoUmSep = []
    nucleotideoDoisSep = []
    contador = 0
    for bases in nucleotideo:
        for char in bases:
            nucleotideoUmSep.append(char) # Separa os nucleotídeos em caracteres
            
    for bases in nucleotideoDois:
        for char in bases:
            nucleotideoDoisSep.append(char) # Separa o nucleotídeo 2 em caracteres
        
    memoria = []
    contador = 0
    # indexSalvo = []
    for i, x in zip(nucleotideoUmSep, nucleotideoDoisSep):# Verifica se os valores são iguais em formato de tupla
            if i == x:
                contador += 1
                memoria.append((i, x)) 
    
    # Comparador em relação oa maior ou menor dna
    if len(nucleotideoUmSep) >= len(nucleotideoDoisSep):
        maiorDna = len(nucleotideoUmSep)
        menorDna = len(nucleotideoDoisSep)
    else:
        maiorDna = len(nucleotideoDoisSep)
        menorDna = len(nucleotideoUmSep)
        
        
    #Define as porcentagem com parâmetros dos genes comparados           
    porcentagemMaior = contador * 100 / maiorDna
    porcentagemMenor = contador * 100 / menorDna
    
    #Arredonda os números para duas casas
    porcentagemMaiorDna = round(porcentagemMaior, 2)
    porcentagemMenorDna = round(porcentagemMenor, 2)
    
    return maiorDna, menorDna, porcentagemMaiorDna, porcentagemMenorDna

maior, menor, dnaMaiorComparado, dnaMenorComparado = comparador(nucleotideo, nucleotideoDois)
 
    
# Funções para o layout
def returnSequencia():
    return seQ

def returnSequencia2():
    return seQ2
        
def returnRna1():
    return rnaMensageiroString

def returnRna2():
    return rnaMensageiroString2

def returnProteinasA():
    return proteinasA

def returnProteinasB():
    return proteinasB