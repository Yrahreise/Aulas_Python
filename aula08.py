from datetime import date

nome = 'Hary Fernando'
sobrenome = 'Herdt'

# Dados reais de nascimento
ano_nascimento = 1978
mes_nascimento = 4  # Abril
dia_nascimento = 22  # Dia correto de nascimento

# Cálculo dinâmico da idade considerando se já fez aniversário este ano
hoje = date.today()
idade = hoje.year - ano_nascimento - ((hoje.month, hoje.day) < (mes_nascimento, dia_nascimento))

maior_de_idade = idade >= 18    
altura_metros = 1.76
print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano de Nascimento:', ano_nascimento)
print('É maior de idade?', maior_de_idade)
print('Altura em metros:', altura_metros)
