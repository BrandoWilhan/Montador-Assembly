#Esse codigo lê a entrada, formata linha por linha e retorna os dados puros.
#Além de retornar funções do tipo R e algumas tipo F(ler linhas 33, 34, 95, 96).
entrada = open('example_saida.asm', 'r')

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
        rt = nova_l[3] #registrador de origem 2
    # AQUI DIO BRANDO!
    print(func, rd, rs, rt) 
    print("r_Funct: ", r_function(func))
    print("f_Funct: ", f_function(func))

#Função que recebe a instrução e retorna seu codigo
#tipo r
def r_function(funct): #O retorno é declarado como uma string, pois em casos com 0 a esquerda 
                       #e ao menos um 1 a direita, é gerado um erro por procedencia do tipo numero 
    # msubu? (Multiply subtract unsigned)
    # madd? (Multiply add)
    if(funct == "add"):
        return '100000'
    if(funct == "sub"):
        return  '100010'
    if(funct == "and"):
        return '100100'
    if(funct == "nor"):
        return '100111'
    if(funct == "xor"):
        return '100110'
    if(funct == "or"):
        return  '100101'
    if(funct == "jr"):
        return '001000'
    if(funct == "slt"):
        return '101010'
    if(funct == "addu"):
        return '100001'
    if(funct == "subu"):
        return '100011' 
    if(funct == "sll"):
        return '000000'
    if(funct == "srl"):
        return '000010'
    #if(funct == "clo"): 
        #count of number of leading ones
        #https://stackoverflow.com/questions/8871204/count-number-of-1s-in-binary-representation
    if(funct == "sra"):
        return '000011'
    if(funct == "srav"):
        return '000111'
    if(funct == "mult"):
        return '011000'
    if(funct == "div"):
        return '011010'
    #if(funct == "movn"): 
        #coloca $t1 como $t2 se $t3 não for zero
        #function=??? (chamar função de comparação)
    if(funct == "mfhi"):
        return  '010000'
    if(funct == "mflo"):
        return '010010'
    #if(funct == "teq"):
        #Faz alguma coisa(?) se $t1 igual a $t2
        #00100: equal
    if(funct == "jalr"):
        return '001001'
    if(funct == "sltu"):
        return '101011'

#tipo f
def f_function(funct): #OpCode: 010001    #Format: 10000
    if(funct == "add.s"):
        return '000000'
    if(funct == "sub.s"):
        return '000001'
    if(funct == "mul.s"):
        return '000010'  
    if(funct == "div.s"):
        return '000011'
    #Falta: add.d, sub.d, mul.d, div.d 
    #       c.eq.s(compara igualdade com precisão simples), c.eq.d(... precisão dupla)

entrada.seek(0) #Coloca o ponteiro no inicio da lista
for linha in entrada:
    linha = linha.strip()
    if linha == ".text":
        break
linhas = entrada.readlines()
ler_linha(linhas[0])

entrada.close