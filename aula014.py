a = 'AAAA' # Variável do tipo string
b = 'BBBB' # Variável do tipo string
c = 1.1 # Variável do tipo float
string = 'a={nome1} b={nome2} c={nome3:.2f}' # String com placeholders
formato = string.format(nome1 = a, nome2 = b, nome3 = c) # Formata a string preenchendo os placeholders com a, b e c (c com 2 casas decimais)
print(formato) # Imprime a string formatada
