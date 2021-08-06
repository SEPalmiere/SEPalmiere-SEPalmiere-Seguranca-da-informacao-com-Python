import os
import time
print("#"*60)

with open('hosts') as file:
    dump = file.read()
    dump = dump.splitlines()


for ip in dump:
    print("Verificando o ip: ", ip)
    os.system('ping -n 2 {}'.format(ip))
    print("-"*60)
    time.sleep(5)

    print("#"*60)