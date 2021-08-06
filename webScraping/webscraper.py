import requests
from bs4 import BeautifulSoup

site = requests.get("https://climatempo.com.br/").content # objeto site recebe o conteudo da requisição http do site

soup = BeautifulSoup(site, 'html.parser') # objeto soup baixa o html dosite

print(soup.prettify()) # transforma a estrutura html em string

#temperatura_hoje = soup.find( "p", class_="-gray _flex _align-center")
#print(temperatura_hoje.string)

print(soup.title.string)
print(soup.a) # imprime a  primeira ancora"
print(soup.p.string) # imprime o primeiro texto

print(soup.find('admin'))



