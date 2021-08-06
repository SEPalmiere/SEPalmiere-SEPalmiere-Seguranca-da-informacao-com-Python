import hashlib

string = input("Digite o texto a ser gerado o Hash: ")
#resultado = hashlib.md5(b'Python Security') # O b nos parenteses serve para converter string em bytes

menu = int(input(''' #### MENU - Escolha o tipo de HASH ####
        1) MD5
        2) SHA1
        3) SHA256
        4) SHA512
        Digite o número do Hash a ser gerado: '''))

if menu == 1:
    resultado = hashlib.md5(string.encode('utf-8')) # O b nos parenteses serve para converter string em bytes
    print('A Hash MD5 da string: ', string, 'é: ', resultado.hexdigest())
elif menu == 2:
    resultado = hashlib.sha1(string.encode('utf-8')) # O b nos parenteses serve para converter string em bytes
    print('A Hash SHA1 da string: ', string, 'é: ', resultado.hexdigest())
elif menu == 3:
    resultado = hashlib.sha256(string.encode('utf-8')) # O b nos parenteses serve para converter string em bytes
    print('A Hash SHA256 da string: ', string, 'é: ', resultado.hexdigest())
elif menu == 4:
    resultado = hashlib.sha512(string.encode('utf-8')) # O b nos parenteses serve para converter string em bytes
    print('A Hash SHA512 da string: ', string, 'é: ', resultado.hexdigest())
else:
    print('Opção escolhida não reconhecida, tente novamente!')