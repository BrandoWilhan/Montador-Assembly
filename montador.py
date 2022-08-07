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