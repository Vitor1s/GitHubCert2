 # ESTRUTURAS DE REPETIÇÃO EM PYTHON (LOOPS)
 # Usamos loops para repetir ações várias vezes, sem precisar escrever o mesmo código várias vezes

print("=== EXEMPLOS DE LOOPS ===\n")  # Título dos exemplos

 # 1. LOOP FOR COM RANGE
 # O loop 'for' é usado para repetir uma ação um número definido de vezes
 # Aqui, vamos contar de 1 até 5
print("1. Contando de 1 a 5:")
for i in range(1, 6):  # range(início, fim) - o 'fim' não é incluído
    print(f"Número: {i}")  # Mostra o número atual

print("\n" + "="*30 + "\n")  # Separador visual

 # 2. LOOP FOR COM LISTA
 # Podemos usar o 'for' para passar por cada item de uma lista
print("2. Iterando sobre uma lista de frutas:")
frutas = ["maçã", "banana", "laranja", "uva"]  # Lista de frutas
for fruta in frutas:
    print(f"Eu gosto de {fruta} 🍎")  # Mostra cada fruta da lista

print("\n" + "="*30 + "\n")  # Separador visual

 # 3. LOOP WHILE
 # O loop 'while' repete enquanto uma condição for verdadeira
 # Aqui, fazemos uma contagem regressiva
print("3. Contagem regressiva com while:")
contador = 5  # Começa do 5
while contador > 0:
    print(f"Faltam {contador} segundos...")  # Mostra o tempo restante
    contador = contador - 1  # Diminui 1 a cada volta (pode usar contador -= 1)
print("🚀 Decolagem!")  # Mensagem final quando termina

print("\n" + "="*30 + "\n")  # Separador visual

 # 4. EXEMPLO PRÁTICO: TABUADA
 # Usando loop para mostrar a tabuada de um número
numero = int(input("Digite um número para ver sua tabuada: "))  # Pede um número ao usuário
print(f"\n📊 Tabuada do {numero}:")
for i in range(1, 11):  # Vai de 1 até 10
    resultado = numero * i  # Calcula o resultado da multiplicação
    print(f"{numero} × {i} = {resultado}")  # Mostra cada linha da tabuada

print("\n" + "="*30 + "\n")  # Separador visual

 # 5. LOOP COM ACUMULADOR
 # Usamos um acumulador para somar vários valores
print("5. Somando números de 1 a 10:")
soma_total = 0  # Começa com zero
for num in range(1, 11):  # Vai de 1 até 10
    soma_total += num  # Adiciona o número atual ao total (igual a soma_total = soma_total + num)
    print(f"Somando {num}, total até agora: {soma_total}")  # Mostra o progresso da soma

print(f"\n🧮 Soma final: {soma_total}")  # Mostra o resultado final

print("\n" + "="*30 + "\n")  # Separador visual

 # 6. LOOP COM ENTRADA DO USUÁRIO
 # O loop continua até o usuário digitar 0
print("6. Digite números para somar (digite 0 para parar):")
soma = 0  # Começa com zero
while True:  # Loop infinito (vai rodar até encontrar um break)
    numero = int(input("Digite um número: "))  # Pede um número ao usuário
    if numero == 0:  # Se o número for zero
        break  # Sai do loop
    soma += numero  # Adiciona o número à soma
    print(f"Soma atual: {soma}")  # Mostra a soma atual

print(f"💯 Soma final de todos os números: {soma}")  # Mostra o resultado final

print("\n" + "="*30 + "\n")  # Separador visual

 # 7. LOOP COM CONTINUE (pula iteração)
 # O 'continue' faz o loop pular para o próximo valor sem executar o resto do código
print("7. Números pares de 1 a 10:")
for i in range(1, 11):  # Vai de 1 até 10
    if i % 2 != 0:  # Se o número for ímpar
        continue  # Pula para a próxima volta do loop
    print(f"Número par: {i}")  # Mostra apenas os números pares

print("\n🎉 Fim dos exemplos de loops!")  # Mensagem final
