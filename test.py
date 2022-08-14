imediato = '16'

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

imediato = bin(int(imediato))[2:]
    
if(len(imediato) < 16):
    imediato = (16 - len(imediato))*'0' + imediato

print(imediato)