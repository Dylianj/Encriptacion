import random

palabra = input("Ingrese una palabra a encriptar: ")
key = ''.join([str(random.randint(0,1)) for _ in range(len(palabra))]) 

def encryp(palabra, key):
    encriptado = ""
    for i in range(len(palabra)):
        xor = ord(palabra[i]) ^ int(key[i]) 
        encriptado += chr(xor)    
    return encriptado

encriptado = encryp(palabra,key)
desencriptado = encryp(encriptado,key)

print(encriptado)
print(desencriptado)
