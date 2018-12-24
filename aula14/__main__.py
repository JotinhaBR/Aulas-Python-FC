import re


i_email = input('\nVai mostrão, qual é seu e-mail? \n')

verificar = re.findall(r'[^@]+@[^@]+\.[^@]+', i_email)

if verificar:
    print('Mostro email encontrados:')
    print(' ')
    print(verificar)
else:
    print('Mostro você não digitou um e-mail valido!!!')