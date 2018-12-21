import time

add_frase = input('\nSolta a voz, qual é a frase?  (Use "HORA DO SHOW" para fechar)\n')
frases = []

while add_frase != 'HORA DO SHOW':
    frases.append(add_frase)
    add_frase = input('\nSolta a voz, qual é a frase?  (Use "HORA DO SHOW" para fechar)\n')
else:
    print(' ')
    print('Array das frases:')
    print(frases)
    print(' ')
    print('Frases salvas no arquivo:')
    w_arquivo = open('aula10/frases.txt', 'w+')
    for frase in frases:
        w_arquivo.write(frase+"\n")
        print(frase)
    