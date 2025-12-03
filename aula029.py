"""
Introdução ao try/except
try -> tentar executar o código
FLOAT -> número com casas decimais
float() -> converte uma string ou número para float
except -> ocorreu algum erro ao tentar executar
"""
numero_str = input('Vou dobrar o número que você digitar: ') #input sempre retorna uma string

try:    #Tenta executar o código dentro do bloco
    numero_float = float(numero_str) #Tenta converter a string para número float
    print('FLOAT: ', numero_float) #imprime o número convertido
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}') #imprime o dobro do número com 2 casas decimais
except:  #Se ocorrer algum erro na conversão    
    print('Isso não é um número.') #imprime mensagem de erro

