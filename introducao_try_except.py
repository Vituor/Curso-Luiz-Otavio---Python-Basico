"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executara
erro = exceção
"""

#numero = input(f"Vou dobrar o número que você digitar: ")
#numero_float = float(numero)

#print(f'o dobro do número que você digitou é: {numero_float*2:.2f}')

numero_str = input(f'vou dobrar o número que vc digitar ')

try:
    numero_float = float(numero_str)
    #print(numero_float)
    print(f'o dobro do num.{numero_str} é: {numero_float*2:.0f}')
except:
    print(f'isto não é um numero {numero_str} ') 

 
