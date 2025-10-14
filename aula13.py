nome = 'Hary Fernando Herdt'
altura = 1.76
peso = 100
imc = peso / (altura * altura) # Calcula o Indice de Massa Corporal (IMC)
# ou imc = peso / altura ** 2
"f-string" # String formatada (f de format)
linha_1 = f'{nome} tem {altura:.2f} de altura' # Formata a altura com 2 casas decimais
linha_2 = f'pesa {peso} quilos e seu IMC é {imc:.2f}' # Formata o IMC com 2 casas decimais
# ou linha_2 = f'pesa {peso} quilos e seu IMC é {imc:.2f}'
print(linha_1) # Exibe o texto da variável linha_1
print(linha_2 ) # Exibe o texto da variável linha_2
