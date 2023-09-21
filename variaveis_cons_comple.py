"""
CONSTANTES = "variáveis" que não mudam o valor -> SEMPRE LETRA MAIUSCULA
Muitas condições (if) <- RUIM para o código
... <- Contagem de Complexibilidade (ruim)
"""

velocidade_1 = 100  #velocidade atual do carro
local_carro = 95 #km da estrada que o carro se encontra

RADAR_1 = 60 #velocidade máx no rada 1 
LOCAL_1 = 100 #km da estrada onde o RADAR_1 se encontra
RADAR_RANGE = 1 #distancia de cobertura do radar 
TOTAL_RANGE = (LOCAL_1 + RADAR_1)

# tomou multa se tiver acima da velocidade no radar1 + Range

if velocidade_1 > RADAR_1:
    print('tomou multa')
elif local_carro != TOTAL_RANGE:
    print('não tomou multa')
else:
    print ('não tomou multa')


