""" FAÇA UM PROGRAMA QUE PERGUNTE AO 
USUÁRIO, E BASENADO-SE NO HORAIO 
DESCRITO, EXIBIR A SAUDAÇÃO APROPRIADA:
EX: BOM DIA - 0 -11
BOA TARDE 12 - 17
BOA NOITE 18 - 23"""

hora_fornecida = input(f'FORNEÇA UMA HORA INTEIRA: ')

try:
    HORA = int(hora_fornecida)

    if HORA >= 0 and HORA <= 11:
        print(f'bom dia')
    elif HORA >= 12 and HORA <=17:
        print(f'boa tarde')
    elif HORA >= 18 and HORA <= 23:
        print(f'boa noite')
    else:
        print(f'não conheço essa hora')
except:
    print(f'isto não é uma hora válida.')
