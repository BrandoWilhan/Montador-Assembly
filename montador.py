from dis import Instruction
from turtle import rt
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
        rt = nova_l[3] #registrador de destino 2
    print(func, rd, rs, rt)

entrada.seek(0) #Coloca o ponteiro no inicio da lista
for linha in entrada:
    linha = linha.strip()
    if linha == ".text":
        break
linhas = entrada.readlines()
ler_linha(linhas[0])

entrada.close

#decodificar registradores

def register_coder(register): 
    reg = '00000'
    if(register[0] == 'z' or register == '0'): #$zero
        return reg
    
    if(register[0] == 'a'):  #$ax
        for i in range(4):
            if(register[1] == str(i)):
                reg = bin(4 + i)[2:]
                reg1 = reg.split()
                if(len(reg) < 4):
                    reg1.insert(0, '0')
                    reg1.insert(0, '0')
                elif(len(reg) < 5):
                    reg1.insert(0, '0')
                reg = ''.join(reg1)
        if(register[1] == 't'):
            reg = '00001'

    if(register[0] == 's'): #$sx
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
    
    if(register[0] == 'v'): #$vx
        for i in range(2):
            if(register[1] == str(i)):
                reg = bin(2 + i)[2:]
                reg1 = reg.split()
                if(len(reg) < 4):
                    reg1.insert(0, '0')
                    reg1.insert(0, '0')
                if(len(reg) < 5):
                    reg1.insert(0, '0')
                reg = ''.join(reg1)
    
    if(register[0] == 't'): #$tx
        for i in range(8):
            if(register[1] == str(i)):
                reg = bin(8 + i)[2:]
                reg1 = reg.split()
                if(len(reg) < 4):
                    reg1.insert(0, '0')
                    reg1.insert(0, '0')
                elif(len(reg) < 5):
                    reg1.insert(0, '0')
                reg = ''.join(reg1)
        for i in range(8, 10):
            if(register[1] == str(i)):
                reg = bin(24 + i - 8)[2:]

    if(register[0] == 'k'): #$kx
        for i in range(2):
            if(register[1] == str(i)):
                reg = bin(26 + i)[2:]
        
    if(register == 'gp'): #$gp
        reg = bin(28)[2:]
        
    if(register == 'sp'): #$sp
        reg = bin(29)[2:]
        
    if(register == 'fp'): #$fp
        reg = bin(30)[2:]
       
    if(register == 'ra'): #$ra
        reg = bin(31)[2:]
        
    for c in range(1, 32):
        if(register == str(c)):
            reg = bin(c)[2:]
            reg1 = reg.split()
            if(len(reg) < 2):
                reg1.insert(0, '0')
                reg1.insert(0, '0')
                reg1.insert(0, '0')
                reg1.insert(0, '0')
            elif(len(reg) < 3):
                reg1.insert(0, '0')
                reg1.insert(0, '0')
                reg1.insert(0, '0')
            elif(len(reg) < 4):
                reg1.insert(0, '0')
                reg1.insert(0, '0')
            elif(len(reg) < 5):          
                reg1.insert(0, '0')
            reg = ''.join(reg1)
    
    return reg

def register_f_coder(register):

    for i in range(32):
        if(register == 'f' + str(i)):
            reg = bin(i)[2:]
            reg1 = reg.split()
            if(len(reg) < 2):
                reg1.insert(0, '0')
                reg1.insert(0, '0')
                reg1.insert(0, '0')
                reg1.insert(0, '0')
            elif(len(reg) < 3):
                reg1.insert(0, '0')
                reg1.insert(0, '0')
                reg1.insert(0, '0')
            elif(len(reg) < 4):
                reg1.insert(0, '0')
                reg1.insert(0, '0')
            elif(len(reg) < 5):          
                reg1.insert(0, '0')
            reg = ''.join(reg1)

    return reg

def instruction_op_code(instruction):
    
    opcode = '000000' #tipo r default

    tipo_r = ['add', 'sub', 'and', 'nor', 'xor', 'or', 'jr', 'slt', 'addu', 
              'subu', 'sll', 'srl', 'clo', 'sra', 'srav', 'mult', 'div', 'movn'
              , 'mfhi', 'mflo', 'teq', 'jalr', 'sltu']
    tipo_f = ['add.d', 'add.s', 'sub.d', 'sub.s', 'c.eq.d', 
              'c.eq.s', 'mul.d', 'mul.s', 'div.d', 'div.s']
    
    if instruction in tipo_r:
        return opcode
    
    if instruction in tipo_f:
        opcode = '010001'
        return opcode
    
    if(instruction == 'lw'):
        opcode = '100011'
        return opcode
    
    if(instruction == 'sw'):
        opcode = '101011'
        return opcode
    
    if(instruction == 'j'):
        opcode = '000010'
        return opcode
    
    if(instruction == 'jal'):
        opcode = '000011'
        return opcode

    if(instruction == 'beq'):
        opcode = '000100'
        return opcode
    
    if(instruction == 'bne'):
        opcode = '000101'
        return opcode
    
    
    if(instruction == 'lui'):
        opcode = '001111'
        return opcode
    
    if(instruction == 'addi'):
        opcode = '001000'
        return opcode
    
    if(instruction == 'andi'):
        opcode = '001100'
        return opcode
    
    if(instruction == 'ori'):
        opcode = '001101'
        return opcode
    
    if(instruction == 'xori'):
        opcode = '001110'
        return opcode
        
    if(instruction == 'bgez'):
        opcode = '000001'
        return opcode

    if(instruction == 'madd'):
        opcode = '011100'
        return opcode

    if(instruction == 'msubu' or instruction == 'mul'):
        opcode = '011100'
        return opcode
    
    if(instruction == 'bgezal'):
        opcode = '000001'
        return opcode

    if(instruction == 'addiu'):
        opcode = '001001'
        return opcode

    if(instruction == 'lb'):
        opcode = '100000'
        return opcode

    if(instruction == 'sb'):
        opcode = '101000'
        return opcode

    if(instruction == 'slti'):
        opcode = '001010'
        return opcode

    
    
#for i in range(32):
 #   print(f'f{i} ' + register_f_coder(f'f{i}'))