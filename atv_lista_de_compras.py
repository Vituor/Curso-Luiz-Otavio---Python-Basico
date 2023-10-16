"""
FAÇA UMA LISTA DE COMPRAR COM LISTAS
O USUÁRIO DEVE TER A POSSIBILIDADE DE 
INSIRIR, APAGAR E LISTAR VALORES DA SUA LISTA
NÃO PERMITA QUE O PROGRAMA QUEBE COM ERROS DE INDICES
INESTENTE NA LISTA
"""

import os
lista =[]

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        valor = input('Valor:')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input('Escolha o índice para apagar:')

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Digite um numero inteiro')
        except IndexError:
            print('Índice não existe na lista.')   
        except Exception:
            print('Erros desconhecido.')
    
    elif opcao == 'l':
        os.system('clear')

        if len(lista) == 0:
            print('Não tem nada na lista')
        
        for i, valor in enumerate(lista):
            print(i,valor)




    else:
        print('Por favor escolha i, a ou l')
