"""
LISTAS EM PYTHON
Tipo de list - Mutável
Suporta vários valores de qualquer tipo
Conhecimento reutilizável - índices e fatiamento
Métodos úteis: APPEND, INSERT, POP, DEL, CLEAR, EXTEND, +
(CRUD - CREATE, READ,UPDATE,DELETE)
"""
#         01234
#        -54321
# string = 'ABCDE'  # cadeia de caracteres (len-checa a quantidade de caracteres da string)
#lista = list() não é a forma mais comum.
# lista =[123, True, 'Luis Otávio', 1.235, []] #mais comum - lista vazia é falsy
# print(lista) #imprimi td o que tem na lista
#MÉTODOS ÚTEIS.
#append = adicionar no ÚLTIMO item da lista - lista.apend()
#pop = remove o último item da lista adicionado ou escolhido - lista.pop()
#del - remove o último item da lista - del.lista[-1] = -1 sempre vai ser o último índice.
#clear - limpa a lista = lista.clear()
#insert - ele adiciona um num. a lista = lista.insert (0 {aqui mostra o indice},5 {valor que vai acrescentar.})

# lista = [10,20,30,40]
# lista.append(50)
# lista.pop()
# lista.append(60)
# lista.append(70)
# lista.pop()
# lista.append(80)
# print(lista)

lista_a = ['a,b,c']
lista_b = [1,2,3]
lista_c = lista_a + lista_b
lista_d =lista_a.extend(lista_b)
print(lista_d)