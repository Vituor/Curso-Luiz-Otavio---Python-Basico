"""
Introdrução ao desempacotamento 
"""

nome1, nome2, nome3 =['Maria','Helena','Luiz']
# print(nome2) - aqui ele retorna o nome da Helena

nome1, *_ =['Maria','Helena','Luiz']
#print(nome1, resto) - aqui ele retorna  - Maria ['Helena', 'Luiz'] - pois criou uma variável *_ (convensão )

""" TUPLES(tuplas)
é uma lista imutável - um pouco mais eficiente. """

nome1, nome2, nome3 = 'Maria','Helena','Luiz'
#conversão de lista para puples - nome = tuple(nomes)