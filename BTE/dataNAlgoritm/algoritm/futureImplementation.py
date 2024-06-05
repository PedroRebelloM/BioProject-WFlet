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

# def lerSequencia(caminho):
#    nuc = []
#    with open(caminho, 'r') as dnA:
#        for seque in SeqIO.parse(dnA, 'fasta'):
#            nuc.append(str(seque.seq))
#    return nuc

#a = lerSequencia(caminhoDoArquivo)
#b = lerSequencia(caminhoSegundoArquivo)
        
        

