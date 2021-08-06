import hashlib

arquivo1 = 'a.txt'
arquivo2 = 'b.txt'

hash1 = hashlib.new('ripemd160')  # Construtor para definir qual hash será usado
hash1.update(open(arquivo1, 'rb').read()) # Cria o hash do arquivo

hash2 = hashlib.new('ripemd160')  # Construtor definindo qual hash será usado
hash2.update(open(arquivo2, 'rb').read())  # Cria o hash do arquivo

print('O hash do arquivo a.txt é: ', hash1.hexdigest())
print('O hash do arquivo b.txt é: ', hash2.hexdigest())

if hash1.digest() != hash2.digest():
    print(f'O arquivo: {arquivo1} é diferente do arquivo: {arquivo2} ')
else:
    print(f'O arquivo: {arquivo1} é igual ao arquivo: {arquivo2} ')