# and significa "e"
# mais de uma condição para checar na string , todas as condições precisam ser verdadeiras


"""entrada = input ('[E]ntrada [S]aida ')
senha_digitada = input("senha: ")
senha_permitida = "123456"

if entrada == 'E' and senha_digitada == senha_permitida:
    print(f"Entrar")
elif senha_digitada != senha_permitida:
    print("senha incorreta")
else:
    print("Sair")
"""
# se em qualquer lugar da expressão for avaliada como FALSE, a expressão toda será FALSE 
# São Considerados valores FALSY 
# 0 - 0.0 - '' (String Vazia) - FALSE

# AVALIAÇÃO DE CURTO CIRCUITO

# print(True and True and True and 0)

# OR significa OU

"""senha = input('senha: ') or 'sem senha'
print(senha)"""

##############################################

"""senha = input('senha: ')

if senha == '123456':
    print('ENTROU')
else:
    print('SENHA INCORRETA') """   


"""senha = input('senha: ')

if senha != '123456': #! = DIFERENTE
    

    print('SENHA INCORRETA')"""

#NOT - INVERTER O CÓDIGO.

"""print(not True) #false
print(not 0) #lembrando que 0 é False / TRUE
print(not 1)#false"""



