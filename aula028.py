"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""
nome = input('Digite seu nome:') # solicita o nome do usuário
idade = input('Digite sua idade:') # solicita a idade do usuário

if nome and idade: # verifica se ambos os campos foram preenchidos
    print(f'Seu nome é: {nome}') # exibe o nome do usuário
    print(f'Sua idade é: {idade}') # exibe a idade do usuário
    print(f'Seu nome invertido é: {nome[::-1]}') # exibe o nome invertido
    if ' ' in nome: # verifica se há espaços no nome
        print('Seu nome contém espaços.') # exibe que o nome contém espaços
    else: # se não houver espaços
        print('Seu nome não contém espaços.') # exibe que o nome não contém espaços
    print(f'Seu nome tem {len(nome)} letras.') # exibe a quantidade de letras no nome
    print(f'A primeira letra do seu nome é: {nome[0]}') # exibe a primeira letra do nome
    print(f'A última letra do seu nome é: {nome[-1]}')  # exibe a última letra do nome
else: # se algum dos campos estiver vazio
    print('Desculpe, você deixou campos vazios.') # exibe mensagem de erro