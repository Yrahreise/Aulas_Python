"""
Iterando strings com while
"""
# 13 caracteres espaço tb conta (começa do 0 1 2 3... etc)
nome = 'Hary Fernando'
tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)
print(nome[3])

novastring = '*'  # cria a variável com o * inicial
i = 0             # indice começa do zero

while i < tamanho_nome:  #roda enquanto i < 13
    novastring += nome[i] + '*'  # acumula letra + *
    i += 1  # avaça o indice

print(novastring)  # imprime *H*a*r*y* *Fe*r*n*a*n*d*o*