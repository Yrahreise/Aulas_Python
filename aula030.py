"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 81 # velocidade atual do carro
local_carro = 100  # local em que o carro está na estrada

RADAR_1 = 80  # velocidade máxima no radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1 # alcance do radar

vel_carro_pass_radar_1 = velocidade > RADAR_1 # Velocidade do carro passou do radar 1
carro_passou_radar_1 = (
    local_carro >= (LOCAL_1 - RADAR_RANGE)
    and local_carro <= (LOCAL_1 + RADAR_RANGE)
)  # Carro passou no radar 1
carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1 # Carro multado no radar 1

if carro_passou_radar_1: # Se o carro passou no radar 1
    print('Carro passou no radar 1') 

if vel_carro_pass_radar_1: # Velocidade do carro ao passar no radar 1
    print('Velocidade do carro no radar 1 foi de:', velocidade, 'km/h') 

if carro_multado_radar_1: # Se o carro foi multado no radar 1
    print('Carro multado no radar 1')