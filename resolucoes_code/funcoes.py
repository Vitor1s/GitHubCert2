# FUNÇÕES EM PYTHON
# Funções são blocos de código que fazem uma tarefa específica
# É como criar suas próprias "ferramentas" para usar várias vezes

print("=== TRABALHANDO COM FUNÇÕES ===\n")

# 1. FUNÇÃO SIMPLES (sem parâmetros e sem retorno)
def saudacao():
    """Esta função exibe uma saudação"""
    print("Olá! Bem-vindo ao Python! 👋")

print("1. Função simples:")
saudacao()  # Chamando a função

print("\n" + "="*40 + "\n")

# 2. FUNÇÃO COM PARÂMETROS
def saudacao_personalizada(nome):
    """Esta função recebe um nome e exibe uma saudação personalizada"""
    print(f"Olá, {nome}! Como você está hoje? 😊")

print("2. Função com parâmetros:")
saudacao_personalizada("Maria")
saudacao_personalizada("João")

print("\n" + "="*40 + "\n")

# 3. FUNÇÃO COM RETORNO
def somar(a, b):
    """Esta função soma dois números e retorna o resultado"""
    resultado = a + b
    return resultado

print("3. Função com retorno:")
soma_resultado = somar(5, 3)
print(f"5 + 3 = {soma_resultado}")
print(f"10 + 20 = {somar(10, 20)}")  # Usando direto

print("\n" + "="*40 + "\n")

# 4. FUNÇÃO COM MÚLTIPLOS PARÂMETROS E PARÂMETROS PADRÃO
def calcular_area_retangulo(largura, altura=1):
    """Calcula a área de um retângulo. Se altura não for fornecida, usa 1"""
    area = largura * altura
    return area

print("4. Função com parâmetro padrão:")
print(f"Área de retângulo 5x3: {calcular_area_retangulo(5, 3)}")
print(f"Área de quadrado 4x4: {calcular_area_retangulo(4, 4)}")
print(f"Área de linha 7x1: {calcular_area_retangulo(7)}")  # usa altura padrão

print("\n" + "="*40 + "\n")

# 5. FUNÇÃO QUE RETORNA MÚLTIPLOS VALORES
def operacoes_basicas(a, b):
    """Realiza operações básicas com dois números"""
    soma = a + b
    subtracao = a - b
    multiplicacao = a * b
    divisao = a / b if b != 0 else "Divisão por zero!"
    
    return soma, subtracao, multiplicacao, divisao

print("5. Função com múltiplos retornos:")
num1, num2 = 15, 3
s, sub, mult, div = operacoes_basicas(num1, num2)
print(f"Números: {num1} e {num2}")
print(f"Soma: {s}")
print(f"Subtração: {sub}")
print(f"Multiplicação: {mult}")
print(f"Divisão: {div}")

print("\n" + "="*40 + "\n")

# 6. FUNÇÃO QUE TRABALHA COM LISTAS
def encontrar_maior(lista_numeros):
    """Encontra o maior número em uma lista"""
    if not lista_numeros:  # Se a lista estiver vazia
        return None
    
    maior = lista_numeros[0]
    for numero in lista_numeros:
        if numero > maior:
            maior = numero
    return maior

def calcular_media(lista_numeros):
    """Calcula a média de uma lista de números"""
    if not lista_numeros:
        return 0
    return sum(lista_numeros) / len(lista_numeros)

print("6. Funções que trabalham com listas:")
numeros = [23, 45, 12, 67, 34, 89, 15]
print(f"Lista: {numeros}")
print(f"Maior número: {encontrar_maior(numeros)}")
print(f"Média: {calcular_media(numeros):.2f}")

print("\n" + "="*40 + "\n")

# 7. FUNÇÃO RECURSIVA (função que chama ela mesma)
def fatorial(n):
    """Calcula o fatorial de um número usando recursão"""
    if n <= 1:
        return 1
    else:
        return n * fatorial(n - 1)

print("7. Função recursiva (fatorial):")
for i in range(1, 6):
    print(f"{i}! = {fatorial(i)}")

print("\n" + "="*40 + "\n")

# 8. EXEMPLO PRÁTICO: CALCULADORA COM FUNÇÕES
def menu():
    """Exibe o menu da calculadora"""
    print("\n🧮 CALCULADORA")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sair")
    return input("Escolha uma opção: ")

def obter_numeros():
    """Solicita dois números ao usuário"""
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    return a, b

def dividir_seguro(a, b):
    """Divide dois números com verificação de divisão por zero"""
    if b == 0:
        return "Erro: Divisão por zero!"
    return a / b

print("8. Exemplo prático - Calculadora:")
print("Simulação de uso da calculadora...")

# Exemplo de uso da calculadora
opcao = "1"  # Simulando escolha do usuário
if opcao == "1":
    # Simulando entrada do usuário
    x, y = 10, 5
    resultado = somar(x, y)
    print(f"Simulação: {x} + {y} = {resultado}")

print("\n🎉 Agora você já sabe como criar e usar funções em Python!")
print("💡 Dica: Funções tornam o código mais organizado e reutilizável!")
