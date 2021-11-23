'''Crie um código em Python que teste se o site pudim está acessível pelo computador usado.'''
import urllib.request

try:
    site = urllib.request.urlopen('http://www.google.com')
except:
    print('\033[31mERRO! - site indisponível\033[m')
else:
    print('Site disponível')
    print(site.read())

