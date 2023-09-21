"""
... perguntar um numero
... digitar se o numero é par ou impar

"""
numero_digitado = float(input(f'digite um numero inteiro que vou lhe dizer se é par ou impar: '))

if (numero_digitado % 2) == 0:
    print(f'este número é par')
elif numero_digitado != int(numero_digitado):
    print(f'você não digitou um numero inteiro.')
else:
    print(f'este número é impar')





