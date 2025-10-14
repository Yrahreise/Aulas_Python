# if / elif      / else
# se / se não se / se não

condicao1 = True # True ou False
condicao2 = True
condicao3 = True
condicao4 = True

if condicao1: 
    print('Código para condição 1') # bloco 1
elif condicao2:
    print('Código para condição 2')
elif condicao3:
    print('Código para condição 3')
elif condicao4: # pode ter quantos elif quiser
    print('Código para condição 4')

else:
    print('Nenhuma condição foi satisfeita') # bloco else é opcional

if 10 == 10: # True
    print('Outro if') # bloco 2

print('Fora do if') # bloco 3 - sempre será executado
