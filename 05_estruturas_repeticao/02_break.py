# break -> Interrompe a execução

# Exemplo -- break
# word = ""
# while True:
#     word = input("Digite 'Começar' para inciarmos: ")
#     if word == 'Começar':
#         break
# print(f"Result: {word}")

# Exercicio 5.14

# i = 0
# sum_n = 0
#
#
# while True:
#     number = int(input("Digite números inteiros: "))
#     if number == 0:
#         break;
#     else:
#         sum_n += number
#         i += 1
# med = sum_n/i
# print(f"Total Números Digitados: {i} | Soma: {sum_n} | Média: {med}")

# Exercicios 5.15

# total = 0
# preco_prod = 0.00
# while True:
#     produto_cod = int(input("Inserir o código do produto: "))
#     if produto_cod == 0:
#         print(f"Total Compras: {total}")
#         break;
#     elif produto_cod == 1:
#         preco_prod = 0.50
#     elif produto_cod == 2:
#         preco_prod = 1.00
#     elif produto_cod == 3:
#         preco_prod = 4.00
#     elif produto_cod == 5:
#         preco_prod = 7.00
#     elif produto_cod == 9:
#         preco_prod = 8.00
#     else:
#         print("Código inválido")
#         break;
#     quant_prod = int(input("Quantide comprada: "))
#     total += preco_prod * quant_prod

