import buscar, postar

print(' ')
print('Menu: ')
print(' 1 - Para buscar coisas no twitter')
print(' 2 - Para twittar na conta do Jotinha_BR')
print(' ')

pergunta = input('Eai cumpade o que você quer fazer? \n')

if pergunta == '1':
    print(' ')
    buscar.go()
elif pergunta == '2':
    print(' ')
    postar.go()
else:
    print(' ')
    print('Cumpade digita um numero certo do menu !!')