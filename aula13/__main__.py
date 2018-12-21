import sys
import requests, json


frase = input('\nSolta a voz, qual é a frase? \n')

try:
    url = 'http://api.funtranslations.com/translate/morse?text='+frase
    res = requests.get(url)
    r_json = json.loads(res.text)
    if r_json['error'] is not None:
        print('Mostro deu erro na API de bosta.')
    else:
        print(' ')
        print('Ae mostrão ta ai tua frase em Morse:')
        print(' ')
        print(r_json['contents']['translated'])
except:
    print('Não da pra abrir essa merda de site porra mostro!!!')