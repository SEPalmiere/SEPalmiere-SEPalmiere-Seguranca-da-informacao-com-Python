import random
import string

tamanho = int(input('Digite o tamanho da senha desejada: '))

chars = string.ascii_letters + string.digits + '!@#%&*()*+-=,ç[]{}.;:' # configuração dos caracteres aceitos

rnd = random.SystemRandom()
8
print(''.join(rnd.choice(chars) for i in range(tamanho))) # Mostrar a senha criada