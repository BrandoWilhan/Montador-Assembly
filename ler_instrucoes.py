from dis import Instruction
from turtle import rt
entrada = open('example_saida.txt', 'r')

#Filtra a linha 
def filtra(lin):
    lin = lin.replace("(", " ")
    lin = lin.replace(")", "")
    lin = lin.replace("$","")
    lin = lin.replace(",","")
    lin = lin.replace("Label: ", "")
    return lin

#Recebe uma linha e retorna os dados dela
def ler_linha(linha):
    nova_l = filtra(linha)
    nova_l = nova_l.split() #transforma linha em umas lista
    func = nova_l[0] #function 
    rd = nova_l[1] #registrador de destino
    rs = nova_l[2] #registrador de origem 1
    rt=""
    if len(nova_l)>3:  
        rt = nova_l[3] #registrador de destino 2
    print(func, rd, rs, rt)

entrada.seek(0) #Coloca o ponteiro no inicio da lista
for linha in entrada:
    linha = linha.strip()
    if linha == ".text":
        break
linhas = entrada.readlines()
ler_linha(linhas[7])

entrada.close