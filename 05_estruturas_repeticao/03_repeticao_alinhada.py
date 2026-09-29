# Repetições aninhadas são quando utlizados uma estrutura de repetição dentro da outra

# Exemplo - Tabuada com repetição aninhadas

# tabuada = 1
# while tabuada <= 10:
#     numero = 1
#     while numero <= 10:
#         print(f"{tabuada} x {numero} = {tabuada*numero}")
#         numero += 1
#     tabuada += 1

# Exercicio 5.22
# while True:
#     tabuada = 1
#     opcao = input(f"""
# Digite uma das opções:
#     -> adicao
#     -> subtracao
#     -> multiplicacao
#     -> divisao
# Para sair digite: sair
# Selecione: """)
#     if opcao == "sair":
#         break;
#     while tabuada <= 10:
#         numero = 1
#         if opcao == 'adicao':
#             while numero <= 10:
#                 print(f"{tabuada} + {numero} = {tabuada+numero}")
#                 numero += 1
#         elif opcao == 'subtracao':
#             while numero <= 10:
#                 print(f"{tabuada} - {numero} = {tabuada - numero}")
#                 numero += 1
#         elif opcao == 'divisao':
#             while numero <= 10:
#                 print(f"{tabuada} / {numero} = {tabuada / numero}")
#                 numero += 1
#         else:
#             while numero <= 10:
#                 print(f"{tabuada} x {numero} = {tabuada * numero}")
#                 numero += 1
#         tabuada += 1
#
#

# Exercício - 5.25 -- Metodo de Newton Raiz Quadrada
# while True:
#     i = 1
#     number = int(input("Digite o número a obter a raiz quadrada: "))
#     base = 2
#     p = (base+(number/base))/2
#     quad_p = p**2
#     print(f"Estimativa {i}: {p}")
#     while True:
#         if abs(number - quad_p) < 0.0001:
#             break;
#         base = p
#         p = (base+(number/base))/2
#         quad_p = p**2
#         i +=1
#         print(f"Estimativa {i}: {p}")

# Revisão F-Strings
# cash = float(input("Digite a quantidade de cash: "))
# print(f"Cash: {cash:5.2f}") # <- Padrão definindo as casas decimais
# print(f"Cash: {cash:.2f}") # <- Define apenas após virgula
# print("-"*30)
# print("Inserir espaços a esquerda (<); direita (>); Ao centro (^)")
# print(f"Cash: {cash:^10.2f}")
# print(f"Cash: {cash:<10.2f}")
# print(f"Cash: {cash:>10.2f}")
# print("-"*30)
# print("Inserir caracteres nos espaços")
# print(f"Cash: {cash:x^10.2f}")
# print(f"Cash: {cash:y<10.2f}")
# print(f"Cash: {cash:z>10.2f}")



