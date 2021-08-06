import ipaddress

ip = '192.168.0.1'
rede = '192.168.0.0/24'


endereco = ipaddress.ip_address(ip)
network = ipaddress.ip_network(rede)

print(endereco)
print(network)

print(endereco + 1500)
print("#"*60)

for n in network:
    print(n)