import sys
import requests

try:
    url = sys.argv[1]
except:
    print('Mostro você não passou o site porra!!')
    sys.exit()

try:
    res = requests.get(url)
    print(' ')
    print('Foi mostro acessou o site, se liga no conteudo:')
    print(' ')
    print(res.text)
except:
    print('Não da pra abrir essa merda de site porra mostro!!!')