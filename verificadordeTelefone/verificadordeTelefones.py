import phonenumbers

from phonenumbers import geocoder

Num_tel = input('Digite o número do telefone no formato +55119999999: ')

phone_num = phonenumbers.parse(Num_tel)

print(geocoder.description_for_number(phone_num, 'pt'))