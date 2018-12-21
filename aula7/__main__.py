def nMaiorMenor(array, tipo):
    if tipo == "MAIOR":
        return max(array)
    elif tipo == "MENOR":
        return min(array)
    else:
        return "ERRO: passe um tipo certo."
    pass




add_number = input('\nVai monstro, fala os numero!!  (Use "HORA DO SHOW" para fechar)\n')
numeros = []

while add_number != 'HORA DO SHOW':
    numeros.append(add_number)
    add_number = input('\nVai monstro, fala os numero!!  (Use "HORA DO SHOW" para fechar)\n')
else:
    print(' ')
    print('Ele que a gente quer? \n', nMaiorMenor(numeros, "MAIOR"), ' (Maior conteudo)')
    print(' ')
    print('Ou é ele? \n', nMaiorMenor(numeros, "MENOR"), ' (Menor conteudo)')
    print(' ')
    print('Mostro tá ai geral:')
    print(numeros)
