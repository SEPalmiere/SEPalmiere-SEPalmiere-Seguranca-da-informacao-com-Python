import os

print("#"*60)

ip_ou_host = input("Digite o IP ou HOST a ser verificado: ")

os.system('ping -n 6 {}'.format(ip_ou_host))

print("-"*60)