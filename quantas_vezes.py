frase = 'O Python é uma linguagem de programa' \
'Multiparadigma' \
'Python foi criado por Guido Van Rossum '

i = 0
while i< len(frase):
    letra_atual = frase[i]
    quantas_vezes_letra_apareceu = frase.count(letra_atual)
    print(quantas_vezes_letra_apareceu)
    print (letra_atual)
    i += 1
