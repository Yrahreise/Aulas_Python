"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""
string = '1000' # String é imutável, ou seja, não pode ser alterada depois de criada
#outra_variavel = f'{string:3}'  # Formata a nova string; não altera 'string' 
# original (imutável)

#print(outra_variavel)  # Imprime a nova string formatada

print(string.zfill(10)) # Preenche a string com zeros à esquerda até 
#atingir 10 caracteres
