import itertools

string = input('String a ser perguntada: ')

# resultado = itertools.permutations('abcdefgh', 6) # itera as letras escolhidas com o tamanho passado como variavel
resultado = itertools.permutations(string, len(string))
j = 0

for i in resultado:
    print(''.join(i))
    j += 1

print("A string escolhida possui: ", j, 'iterações')