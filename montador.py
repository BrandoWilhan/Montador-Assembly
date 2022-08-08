import string
from turtle import width
data = open('example_saida_data.mif', 'r')
text = open('example_saida_text.mif', 'r')

#Seleciona apenas o dado de cada linha(último elemento da string).
def head(lista, n):
    piece = lista[n]
    piece = piece.split()
    return piece[2]

data.seek(0)
c = ""
for linha in data:
    linha = linha.rstrip()
    if linha == "CONTENT":
        break  
    c = c + linha 

#Guarda dados do Cabecalho
depth = head(c.split(";"), 0)
width = head(c.split(";"), 1)
address_r = head(c.split(";"), 2)
data_r = head(c.split(";"), 3)  
print(depth, width, address_r, data_r)

data.close

def register_finder(linha_instrucao):
    i = 0
    codigo_reg = ''
    for x in range(len(linha_instrucao)):
        if(linha_instrucao[x] == '$'):
            codigo_reg[i] = linha_instrucao[x + 1]
            i = i + 1
    
    return codigo_reg

def register_coder(register): 

    if(register[0] == 'z' or register[0] == '0'):
        reg = '00000'
    if(register[0] == 'a'):
        for i in range(4):
            if(register[1] == str(i)):
                reg = bin(4 + i)[2:]
                reg1 = reg.split()
                if(len(reg) < 4):
                    reg1.insert(0, '0')
                    reg1.insert(0, '0')
                if(len(reg) < 5):
                    reg1.insert(0, '0')
                reg = ''.join(reg1)
        if(register[1] == 't'):
            reg = '00001'

    if(register[0] == 's'):
        for i in range(8):
            if(register[1] == str(i)):
                reg = bin(16 + i)[2:]
                reg1 = reg.split()
                if(len(reg) < 4):
                    reg1.insert(0, '0')
                    reg1.insert(0, '0')
                if(len(reg) < 5):
                    reg1.insert(0, '0')
                reg = ''.join(reg1)
    
    return reg

for i in range(8):
    print(register_coder(f's{i}'))