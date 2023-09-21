informacao_peso = float(input(f'Qual seu peso em KG:  '))
informacao_altura = float(input(f'Qual sua altura em centimetros: '))

#altura = float(informacao_altura)
#peso = float(informacao_peso)

IMC = informacao_peso / (informacao_altura**2)

#IMC = peso / (altura**2)

try:
    print(f'seu  é de: {IMC}')  
except:
    print('isto não é um numero valido')