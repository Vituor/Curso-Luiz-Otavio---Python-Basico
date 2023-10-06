"""DEFINIR A PALAVRA SECRETA
   EXIBIR QUANTAS TENTATIVAS
   LETRAS ACERTADAS
   A PALAVRA DEVE SER "COBERTA" POR (*)  """

"""for letra_secreta in PALAVRA_SECRETA:
        if letra_secreta in LETRAS_ACERTADAS:
            PALAVRA_FORMADA += letra_secreta
        else:
            PALAVRA_FORMADA +='*'
    print(PALAVRA_FORMADA) 
    AQUI ESTA O LÓGICA DO CÓDIGO."""

PALAVRA_SECRETA = 'grampeador'
LETRAS_ACERTADAS = ''
NUM_DE_TENTATIVAS = 0



while True: #começa colocando o laço de repetição.

    letra_digitada = input('DIGITE UMA LETRA: ')
    NUM_DE_TENTATIVAS +=1 #começa a contra a quantidade de tentativas

    if len(letra_digitada) >1:
        print('Digite apenas uma letra')
        continue #para continuar o WHILE

    #aqui é para garantir que o usuário vai digitar apenas uma letra por vez.

    if letra_digitada in PALAVRA_SECRETA: #aqui se a letra digitada estiver na apalavra secreta
        LETRAS_ACERTADAS += letra_digitada

    PALAVRA_FORMADA = '' #aqui as letras acertadas irão aparecer 

    for letra_secreta in PALAVRA_SECRETA:
        if letra_secreta in LETRAS_ACERTADAS:
            PALAVRA_FORMADA += letra_secreta
        else:
            PALAVRA_FORMADA +='*'
    print(PALAVRA_FORMADA)

    if PALAVRA_FORMADA == PALAVRA_SECRETA:
        print(f'Parabéns, VOCÊ GANHOU. A PALAVRA SECRETA É {PALAVRA_SECRETA}. ')
        print(f'Você tentou {NUM_DE_TENTATIVAS} para acertar.')



