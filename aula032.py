"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""# Solicita entrada do usuário
entrada = input('Digite um número inteiro: ')

# Tenta converter a entrada para inteiro
try:
    numero = int(entrada)
    
    # Verifica se o número é par ou ímpar
    # Um número é par quando o resto da divisão por 2 é zero
    if numero % 2 == 0:
        print(f'O número {numero} é par.')
    else:
        print(f'O número {numero} é ímpar.')
        
except ValueError:
    # Se a conversão falhar, informa que não é um número inteiro
    print('Você não digitou um número inteiro.')
"""


"""Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23."""

"""entrada = input('Digite a hora (0-23): ') # Solicita a hora ao usuário

# Tenta converter para inteiro e validar
try:
    hora = int(entrada)
    
    # Verifica se a hora está no intervalo válido (0 a 23)
    if hora < 0 or hora > 23:
        print('Hora inválida! Digite um valor entre 0 e 23.')
    # Verifica o período do dia usando condicionais encadeados
    elif hora >= 0 and hora <= 11:
        print('Bom dia!')
    elif hora >= 12 and hora <= 17:
        print('Boa tarde!')
    elif hora >= 18 and hora <= 23:
        print('Boa noite!')
        
except ValueError:
    # Se a conversão falhar, informa que não é um número válido
    print('Por favor, digite um número inteiro válido.')
"""


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# Solicita o primeiro nome do usuário
nome = input('Digite seu primeiro nome: ')

# Remove espaços extras no início e fim
nome = nome.strip()

# Calcula o tamanho do nome usando len()
tamanho = len(nome)

# Verifica o tamanho e exibe a mensagem apropriada
if tamanho > 0:
    if tamanho <= 4:
        print('Seu nome é curto')
    elif tamanho <= 6:
        # Se chegou aqui, tamanho é 5 ou 6 (porque não é <= 4)
        print('Seu nome é normal')
    else:
        # Se chegou aqui, tamanho é maior que 6
        print('Seu nome é muito grande')
else:
    print('Você não digitou nenhum nome!')