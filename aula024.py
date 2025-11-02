# Operadores 'in'  'not in' # Usados para verificar a presença de um valor em uma sequência.
# Strings são iteráveis em Python, o que significa que podemos 
# verificar a presença de caracteres ou substrings dentro de uma
# string usando os operadores 'in' e 'not in'.
# 0 1 2 3 # Índices
# H a r y # String
# -6 -5 -4 -3 -2 -1 # Índices negativos
nome = 'Hary'
#print(nome[2]) # Acessando caractere por índice
#print(nome[-4]) # Acessando caractere por índice negativo
#print('y' in nome)  # Verifica se 'y' está em nome -> True  
#print('F' in nome)  # Verifica se 'F' está em nome -> False
#print('Har' in nome)  # Verifica se 'Har' está em nome -> True
#print(10 * '-')  # Imprime uma linha de separação
#print( 'Har' not in nome)  # Verifica se 'Har' não está em nome -> False
#print( 'F' not in nome)  # Verifica se 'F' não está em nome -> True

nome = input('Digite o seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')

# Teste de auto-sync: esta linha foi adicionada automaticamente