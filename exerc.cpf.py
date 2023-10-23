cpf_infor_usurario= '38724592870' #cpf da pessoa

nove_digitos = cpf_infor_usurario[:9] #selecionando os 9 primeiros digitos.
contador_regressivo = 10 

#print(nove_digitos,contador_regressivo) #somente para teste

resultado = 0
#aqui começa o programa para identificar o primeiro digito do cpf

for digito in nove_digitos: #aqui cria uma variável 'digito' dentro dos 9 digitos
    resultado += int(digito)*contador_regressivo #pegou cada digito, transformou em um numero 'int' 
    contador_regressivo -= 1 
    # print(digito) - teste 
    # print(resultado) #- neste teste ele mostra o valor da multiplicação do 9 primeiros digitos com o contador regressivo
digito = (resultado * 10) % 11 #pegou resultado da multiplicadção anterior, multiplicou por 10 e dividiu por 11 exibiu o resto da divisão com o %
#print(digito) - teste do resultado 
digito = digito if digito <= 9 else 0 #se o resto da divisão for menor que 9 continua o mesmo numero se for maior ele passa a ser 0 
#print(digito) #- teste do resultado da condição

# segundo digito do cpf 

# cpf= '74682489070'

dez_digitos = cpf_infor_usurario[:10]
contador_regressivo_1 = 11

resultado_1 = 0

for digito_1 in dez_digitos:
    resultado_1 += int(digito_1)*contador_regressivo_1
    contador_regressivo_1 -= 1

digito_1 = (resultado_1 * 10) % 11
# print(digito_1) - teste 
digito_1 = digito_1 if digito_1 <= 9 else 0
#print(digito_1)

cpf_gerado = f'{nove_digitos}{digito}{digito_1}'

#print(cpf_gerado) #-PARA TESTE

if cpf_infor_usurario == cpf_gerado:
    print(f' O CPF: {cpf_infor_usurario} é VÁLIDO')
else:
    print('CPF INVÁLIDO.')
