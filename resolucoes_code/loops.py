# ESTRUTURAS DE REPETIÇÃO EM PYTHON (LOOPS)
# Usamos para repetir ações várias vezes

print("=== EXEMPLOS DE LOOPS ===\n")

# 1. LOOP FOR COM RANGE
print("1. Contando de 1 a 5:")
for i in range(1, 6):  # range(início, fim) - fim não é incluído
    print(f"Número: {i}")

print("\n" + "="*30 + "\n")

# 2. LOOP FOR COM LISTA
print("2. Iterando sobre uma lista de frutas:")
frutas = ["maçã", "banana", "laranja", "uva"]
for fruta in frutas:
    print(f"Eu gosto de {fruta} 🍎")

print("\n" + "="*30 + "\n")

# 3. LOOP WHILE
print("3. Contagem regressiva com while:")
contador = 5
while contador > 0:
    print(f"Faltam {contador} segundos...")
    contador = contador - 1  # Pode ser escrito como: contador -= 1
print("🚀 Decolagem!")

print("\n" + "="*30 + "\n")

# 4. EXEMPLO PRÁTICO: TABUADA
numero = int(input("Digite um número para ver sua tabuada: "))
print(f"\n📊 Tabuada do {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} × {i} = {resultado}")

print("\n" + "="*30 + "\n")

# 5. LOOP COM ACUMULADOR
print("5. Somando números de 1 a 10:")
soma_total = 0
for num in range(1, 11):
    soma_total += num  # Mesma coisa que: soma_total = soma_total + num
    print(f"Somando {num}, total até agora: {soma_total}")

print(f"\n🧮 Soma final: {soma_total}")

print("\n" + "="*30 + "\n")

# 6. LOOP COM ENTRADA DO USUÁRIO
print("6. Digite números para somar (digite 0 para parar):")
soma = 0
while True:  # Loop infinito
    numero = int(input("Digite um número: "))
    if numero == 0:
        break  # Sai do loop
    soma += numero
    print(f"Soma atual: {soma}")

print(f"💯 Soma final de todos os números: {soma}")

print("\n" + "="*30 + "\n")

# 7. LOOP COM CONTINUE (pula iteração)
print("7. Números pares de 1 a 10:")
for i in range(1, 11):
    if i % 2 != 0:  # Se for ímpar
        continue  # Pula para a próxima iteração
    print(f"Número par: {i}")

print("\n🎉 Fim dos exemplos de loops!")
