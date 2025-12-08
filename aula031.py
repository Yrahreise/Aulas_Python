"""
Flag (Bandeira) - marcar um local no código
None = Não valor
is e is not = é ou não é(tipo,valor, identidade)
id = identidade do objeto
"""

#v1 = 'a' # variável recebe o valor 'a'
#v2 = 'b' # variável recebe o valor 'b'
#print(id(v1)) # imprime o id (identidade) do objeto v1
#print(id(v2)) # imprime o id (identidade) do objeto v2

condicao = True
passou_no_if = None

if condicao:
     passou_no_if = True
     print('Faça algo') 
else:
     print('Não faça algo')


if passou_no_if is None:
     print('Não passou no if')
else:
     print('Passou no if')