"""
enumera - enumra iteráveis (índices) """

lista = ['Maria', 'Helena','Luiz']
lista.append('João') #adicionei o João
lista.pop() #removi o ultimo item

#para criar uma lista enumerada 

lista_enumerada = enumerate(lista) #variável para enumerar 

# for item in lista_enumerada: #PARA ITEM EM LISTA ENUMERADA
#     print(item)

for indice, nome in lista_enumerada: 
    print(indice, nome)

#enumerate - enumera cada item de uma lista.