import sys

try:
    caminho = sys.argv[1]
except:
    print('Mostro você não passou o caminho do arquivo que quer abrir porra!!')
    sys.exit()

try:
    arq = open(caminho, 'r')
    pergunta = input('Se quer ver essa porra? \n')
    if pergunta == 's' or pergunta == 'sim' or pergunta == 'y' or pergunta == 'yes':
        print('\nTa ai mostro o conteudo: ')
        for lins in arq:
            print(lins)
    else:
        print('\nBlz Mostro mas abriu a porra do arquivo!!!')
    
except:
    print('Não da pra abrir essa merda de arquivo porra mostro!!!')