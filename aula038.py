"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
qtd_linhas = 5 # quantidade de linhas
qtd_colunas = 5 # quantidade de colunas

linha = 1 # contador de linhas
while linha <= qtd_linhas: # enquanto a linha for menor ou igual a quantidade de linhas
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=} {coluna=}') # f-string -> string formatada, permite colocar expressões dentro das chaves
        coluna += 1 # coluna = coluna + 1 -> incrementa a coluna em 1
    linha += 1 # linha = linha + 1 -> incrementa a linha em 1


print('Acabou')