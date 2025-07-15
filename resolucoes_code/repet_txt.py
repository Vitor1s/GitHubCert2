texto = input("Digite uma string: ")
numero = int(input("Digite um número inteiro: "))

print((texto + ' ')* numero)  # Repete a string 'numero' vezes

# Primeira sugestão dada pelo Copilot o join evita o espaço extra no final 
# print(' '.join([texto] * numero))  # Repete a string com espaço entre elas