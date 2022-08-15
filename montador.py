from dis import Instruction
from turtle import rt

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

def bit_filler():
        return '00000'

def upper_bits(imediato):
    
    decimal = False

    for i in range(2, 10):
        if(f'{i}' in imediato):
                decimal = True        
    if('x' in imediato):
        imediato = imediato.lstrip("0x")
        imediato = imediato[:4]
        imediato += 4*'0'
        imediato = bin(int(imediato, 16))[2:]
        if(len(imediato) < 32):
            imediato = (32 - len(imediato))*'0' + imediato
        imediato = imediato[:16]
    #if(decimal):
     #   imediato = offset_to_binary(imediato)

    return imediato

def lower_bits(imediato):
    
    decimal = False

    for i in range(2, 10):
        if(f'{i}' in imediato):
                decimal = True        
    if('x' in imediato):
        imediato = imediato.lstrip("0x")
        imediato = imediato[4:]
        imediato += 4*'0'
        imediato = bin(int(imediato, 16))[2:]
        if(len(imediato) < 32):
            imediato = (32 - len(imediato))*'0' + imediato
        imediato = imediato[:16]
    #if(decimal):
     #   imediato = offset_to_binary(imediato)

    return imediato

def jump_calc(LABEL):
    
    contador = 0
    
    entrada.seek(0) #Coloca o ponteiro no inicio da lista
    for linha in entrada:
        linha = linha.strip()
        if linha == ".text":
            break
    for linha in entrada:
        linha = linha.strip()
        contador += 1
        if linha == LABEL:
            break
    return contador
    

def instruction_op_code(instruction):
    
    opcode = '000000' #tipo r default

    tipo_r = ['add', 'sub', 'and', 'nor', 'xor', 'or', 'jr', 'slt', 'addu', 
              'subu', 'sll', 'srl', 'sra', 'srav', 'mult', 'div', 'movn'
              , 'mfhi', 'mflo', 'sltu']
    tipo_f_s = ['add.s', 'sub.s', 'c.eq.s', 'mul.s', 'div.s']
    tipo_f_d = ['add.d', 'sub.d', 'c.eq.d', 'mul.d', 'div.d']
    
    if instruction[0] in tipo_r:
        return instruction_hex(opcode + register_coder(instruction[2]) + register_coder(instruction[3]) + register_coder(instruction[1]) + bit_filler() + r_function(instruction[0]))
    
    if instruction[0] in tipo_f_s:
        opcode = '010001'
        return instruction_hex(opcode + '10000' + register_f_coder(instruction[3]) + register_f_coder(instruction[2]) + register_f_coder(instruction[1]) + f_function(instruction[0]))
    
    if instruction[0] in tipo_f_d:
        opcode = '010001'
        return instruction_hex(opcode + '10001' + register_f_coder(instruction[3]) + register_f_coder(instruction[2]) + register_f_coder(instruction[1]) + f_function(instruction[0]))
    
    if(instruction[0] == 'clo'):
        opcode = '011100'
        return instruction_hex(opcode + register_coder(instruction[2]) + bit_filler() + register_coder(instruction[1]) + '00000' + r_function(instruction[0]))

    if(instruction[0] == 'c.eq.d'):
        opcode = '010001'
        return instruction_hex(opcode + '10001' + register_f_coder(instruction[2]) +register_f_coder(instruction[1]) + f_function(instruction[0]))

    if(instruction[0] == 'c.eq.s'):
        opcode = '010001'
        return instruction_hex(opcode + '10000' + register_f_coder(instruction[2]) +register_f_coder(instruction[1]) + f_function(instruction[0]))

    if(instruction[0] == 'lw'):
        opcode = '100011'
        return instruction_hex(opcode + register_coder(instruction[3]) + register_coder(instruction[1]) + offset_to_binary(instruction[2]))
    
    if(instruction[0] == 'sw'):
        opcode = '101011'
        return instruction_hex(opcode + register_coder(instruction[3]) + register_coder(instruction[1]) + offset_to_binary(instruction[2]))
    
    if(instruction[0] == 'teq'):
        opcode = '000000'
        return instruction_hex(opcode + register_coder(instruction[1]) + register_coder(instruction[2]) + bit_filler() + bit_filler() + r_function(instruction[0]))

    if(instruction[0] == 'j'):
        opcode = '000010'
        return opcode
    
    if(instruction[0] == 'jal'):
        opcode = '000011'
        return opcode

    if(instruction[0] == 'beq'):
        opcode = '000100'
        return opcode
    
    if(instruction[0] == 'bne'):
        opcode = '000101'
        return opcode
    
    if(instruction[0] == 'lui'):
        opcode = '001111'
        return instruction_hex(opcode + bit_filler() + register_coder(instruction[1]) + upper_bits(instruction[2]))
    
    if(instruction[0] == 'addi'):
        opcode = '001000'
        return instruction_hex(opcode + register_coder(instruction[2]) + register_coder(instruction[1]) + offset_to_binary(instruction[3]))
    
    if(instruction[0] == 'andi'):
        opcode = '001100'
        return instruction_hex(opcode + register_coder(instruction[2]) + register_coder(instruction[1]) + offset_to_binary(instruction[3]))
    
    if(instruction[0] == 'ori'):
        opcode = '001101'
        return instruction_hex(opcode + register_coder(instruction[2]) + register_coder(instruction[1]) + offset_to_binary(instruction[3]))
    
    if(instruction[0] == 'xori'):
        opcode = '001110'
        return instruction_hex(opcode + register_coder(instruction[2]) + register_coder(instruction[1]) + offset_to_binary(instruction[3]))
        
    if(instruction[0] == 'bgez'):
        opcode = '000001'
        return opcode

    if(instruction[0] == 'madd'):
        opcode = '011100'
        return instruction_hex(opcode + register_coder(instruction[1]) + register_coder(instruction[2]) + bit_filler() + bit_filler() + bit_filler())

    if(instruction[0] == 'mul'):
        opcode = '011100'
        return instruction_hex(opcode + register_coder(instruction[2]) + register_coder(instruction[3]) + register_coder(instruction[1]) + bit_filler() + '000010')
    
    if(instruction[0] == 'msubu'):
        opcode = '011100'
        return instruction_hex(opcode + register_coder(instruction[1]) + register_coder(instruction[2]) + bit_filler() + bit_filler() + '000101')
    
    if(instruction[0] == 'bgezal'):
        opcode = '000001'
        return opcode

    if(instruction[0] == 'addiu'):
        opcode = '001001'
        return instruction_hex(opcode + register_coder(instruction[2]) + register_coder(instruction[1]) + offset_to_binary(instruction[3]))

    if(instruction[0] == 'lb'):
        opcode = '100000'
        return instruction_hex(opcode + register_coder(instruction[3]) + register_coder(instruction[1]) + offset_to_binary(instruction[2]))

    if(instruction[0] == 'sb'):
        opcode = '101000'
        return instruction_hex(opcode + register_coder(instruction[3]) + register_coder(instruction[1]) + offset_to_binary(instruction[2]))

    if(instruction[0] == 'slti'):
        opcode = '001010'
        return instruction_hex(opcode + register_coder(instruction[2]) + register_coder(instruction[1]) + offset_to_binary(instruction[3]))
    
    if(instruction[0] == 'li'):
        temp_register = instruction[1]
        temp_imediate = instruction[2]
        
        if(int(instruction[2], 16) >= 65536):
            instruction[0] = 'lui'
            instruction[1] = '1'
            first = instruction_op_code(instruction)
            instruction[0] = 'ori'
            instruction[1] = temp_register
            instruction[2] = '1'
            instruction.append('')
            instruction[3] = lower_bits(temp_imediate)
            second = instruction_op_code(instruction)
            return first + '\n' + second        
        else:
            instruction[0] = 'addi'
            instruction.append('')
            instruction[3] = instruction[2]
            instruction[2] = '0'
            instruction[3] = instruction[3].lstrip("0x")
            instruction[3] = int(instruction[3],16)
            instruction[3] = str(instruction[3])
            return instruction_op_code(instruction)
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

    if(funct == "clo"): 
        return '100001'

    if(funct == "sra"):
        return '000011'

    if(funct == "srav"):
        return '000111'

    if(funct == "mult"):
        return '011000'

    if(funct == "div"):
        return '011010'

    if(funct == "movn"): 
        return '001011'
        
    if(funct == "mfhi"):
        return  '010000'

    if(funct == "mflo"):
        return '010010'

    if(funct == "teq"):
        return '110100'

    if(funct == "jalr"):
        return '001001'

    if(funct == "sltu"):
        return '101011'
#tipo f
def f_function(funct): #OpCode: 010001    #Format: (s)10000
    if(funct == "add.s" or funct == "add.d"):
        return '000000'
    if(funct == "sub.s" or funct == "sub.d"):
        return '000001'
    if(funct == "mul.s" or funct == "mul.d"):
        return '000010'  
    if(funct == "div.s" or funct == "div.d"):
        return '000011'
    if(funct == "c.eq.s" or funct == "c.eq.d"):
        return '110010'

    #       c.eq.s(compara igualdade com precisão simples), c.eq.d(... precisão dupla)
def offset_to_binary(offset):

    imediato = bin(int(offset))[2:]
    
    if(len(imediato) < 16):
        imediato = (16 - len(imediato))*'0' + imediato
    
    return imediato
    
#for i in range(32):
 #   print(f'f{i} ' + register_f_coder(f'f{i}'))

def instruction_hex(binary):
    hexa = hex(int(binary, 2))[2:]

    if(len(hexa) < 8):
        hexa = '0' + hexa
    return hexa

 
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
    instrucao = nova_l.split() #transforma linha em umas lista
    return instrucao

entrada.seek(0) #Coloca o ponteiro no inicio da lista
for linha in entrada:
    linha = linha.strip()
    if linha == ".text":
        break
linhas = entrada.readlines()

entrada.close

for i in range(len(linhas)):
    print(instruction_op_code(ler_linha(linhas[i])))





