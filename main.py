opc = input("Digite c se quiser criptografar e d se quiser descriptografar um texto: ")
texto = input("Digite o texto: ")
num = int(input("Digite o número de casas: "))

if(opc == 'd'):
    num = int(-num)

resp = ''

for char in texto:
    if(ord(char)>96 and ord(char)<123):
        v = (ord(char)) + num
        if(v<97):
            v = 123 - (97 - v)
        elif(v>122):
            v = 97 + (v - 123)
        resp += chr(v)
    else:
        resp += char

print(resp)

