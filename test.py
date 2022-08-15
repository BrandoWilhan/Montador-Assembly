imediato = '0x10010000'

decimal = False

if('x' in imediato):
    imediato = imediato.lstrip("0x")
    imediato = imediato[4:]
    imediato += 4*'0'
    imediato = bin(int(imediato, 16))[2:]
    if(len(imediato) < 32):
        imediato = (32 - len(imediato))*'0' + imediato
    imediato = imediato[:16]

    
if(len(imediato) < 16):
    imediato = (16 - len(imediato))*'0' + imediato

print(imediato)