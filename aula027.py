"""
Fatiamento de strings
 012345678 # índices positivos
 Olá mundo 
-987654321 # índices negativos
Fatiamento [i:f:p] [::] # início:fim:passo
i = índice inicial (inclusivo)
f = índice final (exclusivo)
p = passo (pula caracteres)
Obs.: a função len retorna a qtd 
de caracteres da str 
"""
variavel = 'Olá mundo'
print(variavel[4:]) # escreve mundo
print(variavel[:5]) # escreve Olá
print(len(variavel)) # escreve quantos caracteres tem a str
print(variavel[0:9]) # escreve Olá mundo
print(variavel[0:9:2]) # escreve O âmdo (pula de 2 em 2)
print(variavel[-1:-10:-1]) # escreve odnum álO (str invertida)
