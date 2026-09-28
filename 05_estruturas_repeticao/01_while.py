# x = 10
# while x >= 0:
#     print(x)
#     x -= 1
# print("Fogo!!")
# print('-'*30)

# i = 0 #Contador
# var_fim = int(input("Digite um número -> "))
# while i <= var_fim:
#     if i % 2 != 0:
#         print(i)
#     i += 1
# print('-'*30)

# i = 0
# while i <= 10:
#     mult = i * 3
#     print(mult)
#     i += 1
# print('-'*30)


# inicio = int(input("Digite o número de inicio da tabuada -> "))
# fim = int(input("Digite o número final da tabuada -> "))

# while inicio <= fim:
#     mult = inicio*2
#     print(f"{2} x {inicio} = {mult}")
#     inicio += 1
# print('-'*30)


# num1 = int(input("Digite o número 1 da tabuada -> "))
# num2 = int(input("Digite o número 2 da tabuada -> "))
# i = 1
# result = 0
# while i <= num2:
#     result += num1 
#     i += 1

# print(f"{num1} x {num2} = {result}")

# n1 = int(input("Inserir o número a ser dividido: "))
# n2 = int(input("Inserir o número que vai dividir: "))

# i = 0
# divisao = n1
# while i < n1/n2:
#     divisao -= n2
#     i += 1
# print(f"Resultado divisão: {i} | Resto: {divisao}")

# -- Exemplo Média --
#soma = 0  
#i = 1 
#while i <= 3:
#    n = int(input("Entre com três números -> ")) 
#    soma += n
#    i += 1
#print(f"Média: {soma/3}")

# -- Exercício 5.11

#deposito = float(input("Digite o deposito inicial: "))
#tax_juros = int(input("Digite a taxa de juros: "))
#mes = 1 # Contador
#montante = 0
#total = 0 #Acumulador 
#while mes <= 24: 
    # montante = deposito x (1 + tax_juros)**mes
#   montante = deposito * (1 + (tax_juros/100))**mes
#   total += montante
#   print(f"Valor do rendimento: {montante:5.2f} | Mês: {mes} | Rendimento Real {montante - deposito:5.2f}")
#   mes += 1 
#print(f"Total de ganho com juros: {total:5.2f}")

