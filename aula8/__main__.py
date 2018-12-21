import sys
import os

argv = sys.argv
caminho = os.getcwd()
caminho_arq = ''+caminho+'\\'+ argv[1]+''

if os.path.isdir(caminho_arq) is not False:
    os.system('py '+caminho_arq)
    pass
else:
    print("Mostro fala pra min uma aula certa porra !!!")
    pass