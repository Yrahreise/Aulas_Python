"""
Repetições (while)
Executa uma ação enquanto uma condição for verdadeira.

Exemplos:
- Loop controlado: repete até a condição tornar-se falsa.
- Loop infinito: quando a condição nunca se torna falsa.
- `break`: interrompe imediatamente o loop (usado aqui para demonstrar).
"""
contador = 0

# Enquanto 'contador' for menor ou igual a 10, o loop continua.
while contador <= 100:
    contador += 1  # aumenta o contador em 1 antes de imprimir (imprime 1,2,3,...)
    
    if contador == 6:
        print('Não vou mostrar o 6.')  # exibe o valor atual do contador
        continue  # pula o restante do código no loop e volta para a próxima iteração

        print(contador)  # executado após o término do loop (seja por condição ou por break)

    # Interrompe o loop quando o contador atingir 4.
    # Isso demonstra o uso de `break` para sair do while prematuramente.
    if contador == 40:
        break
