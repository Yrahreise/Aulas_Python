"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}.') # espaços à esquerda
print(f'{variavel: <10}.') # espaços à direita
print(f'{variavel: ^10}.') # espaços ao centro
print(f'{1000.4873648123746:0=+10,.1f}') # força o número a aparecer antes dos zeros
print(f'O hexadecimal de 1500 é {1500:08X}') # hexadecimal com 8 dígitos
print(f'{variavel!r}') # usa a representação oficial da variável