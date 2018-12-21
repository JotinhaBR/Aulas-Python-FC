
print(' ')
print('Bora convidar geral pra festa do Bambam !!!')
print(' ')


add_convidado = input('\nSolta a voz, quem tu quer chamar?  (Use "HORA DO SHOW" para fechar)\n')
convidados = []

while add_convidado != 'HORA DO SHOW':
    convidados.append(add_convidado)
    add_convidado = input('\nSolta a voz, quem tu quer chamar?  (Use "HORA DO SHOW" para fechar)\n')
else:
    print(' ')
    print('Seguinte cumpade tivemos ', len(convidados), ' convidados')
    print(' ')
    print('E esses é nossos convidados:')
    for convidado in convidados:
        print(convidado)
        pass
