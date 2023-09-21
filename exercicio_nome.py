"""escreva seu nome e se ele tiver 4 letras ou menos escreva
seu nome é curto. 5 ou 6 letras seu nome é normal, 
mais de 6 letras seu nome é grande"""

escreva_seu_nome = input(f'ESCREVA SEU NOME:')
O_NOME =len(escreva_seu_nome)

print(f'seu nome tem {O_NOME} letras')

try:
    if O_NOME <= 4:
        print('seu nome é curto')  
    elif O_NOME >=5 and O_NOME <=6:
        print('seu nome é normal')
    else:
        print('seu nome é longo')
except O_NOME != str:
    print('isto não é um nome')
