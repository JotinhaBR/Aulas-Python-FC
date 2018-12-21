import sys
import requests

try:
    url = sys.argv[1]
except:
    print('Mostro você não passou o site porra!!')
    sys.exit()

try:
    cabecalho = sys.argv[2]
except:
    cabecalho = ""
try:
    cookies = sys.argv[3]
except:
    cookies = ""
try:
    dados = sys.argv[4]
except:
    dados = ""

try:
    res = requests.post(url, headers=cabecalho, cookies=cookies, data=dados)
    print(' ')
    print('Foi mostro acessou o site, se liga no conteudo:')
    print(' ')
    print(res.text)
except:
    print('Não da pra abrir essa merda de site porra mostro!!!')