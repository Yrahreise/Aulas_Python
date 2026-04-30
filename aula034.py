"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito: um loop que não tem fim, ou seja, a condição nunca se torna falsa
"""

while True:
    nome = input('Qual é o seu nome? ')

    if nome == 'sair':
        print('Acabou...')
        break  # Interrompe o loop

    print(f'Seu nome é {nome}') # Imprime o nome do usuário
