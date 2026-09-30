# List -> Coleção de n tipos de dados para n quantidades
# list_number = [10,11,13]
# print(list_number[0])

# Exercício - 6.1

# notas = [0, 0, 0, 0, 0, 0, 0, 0]
# soma = 0
# x = 0
# while x < 8: # lista possui 7 elementos
#     notas[x] = float(input(f"Digite a {x} do aluno: "))
#     soma += notas[x]
#     x += 1
# x = 0
# while x < 8:
#     print(f"Nota {x}: {notas[x]:.2f}")
#     x += 1
# print(f"Média: {soma / x:.2f}")

# Copia e Fatiamento

# list_fruts = ["apple", "pineapple", "grapple"]
# fav_fruts = list_fruts[:] # Através de fatiamento fazemos uma cópia de elementos
#
# print(list_fruts)
# print(fav_fruts)
# fav_fruts[0] = "banana"
# print("São independentes:")
# print(list_fruts)
# print(fav_fruts)
# print("-"*30)
#
# print("Fatiamento")
# print(f"Menos o último: {fav_fruts[:-1]}")
# print(f"Apenas o primeiro elemeto: {fav_fruts[0:1]}")
# print(f"Apenas o último: {fav_fruts[-1:]}")
# print(f"Dois primeiros: {fav_fruts[0:2]}")

# Tamanho da lista -> len()
# list_names = ["Peter", "Bruce", "Gohan"]
# print(len(list_names))

# Adicionando elementos -> .append() e .extend()
# list_convidados = ["Isabele", "Ricardo", "Mosca"]
# print(f"Lista original: {list_convidados}")
#
# list_convidados.append("Ana")
# print(f"Com append: list_convidados")
#
# list_convidados_fred = ["William", "Ribamar", "Joyce"]
# list_convidados.extend(list_convidados_fred)
# print(f"Ampliando a lista com os convidados do Fred: {list_convidados}")
#
# list_excluidos = ["Pedro", "Murilo"]
# list_convidados.append(list_excluidos)
# print(f"Acessando outra lista dentro da convidados: {list_convidados[7]}")
#
# print(f"Lista final: {list_convidados}")

# Exercício - 6.2
# list_numbers = []
# list_math = []
# x = 0
# while x < 5:
#     number = int(input(f"Inserir o {x+1} número:"))
#     list_numbers.append(number)    
#     x+=1
# x = 0
# while x < 3:
#     tema = input(f"Inserir assuntos que goste de matematica: ")
#     list_math.append(tema)    
#     x+=1
#
# list_tres = []
# Forma 1
# list_tres = list_numbers[:]
# list_tres.extend(list_math)
# list_tres = list_numbers + list_math
# print(list_tres)
