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
while True:
    tabuada = 1
    opcao = input(f"""
Digite uma das opções:
    -> adicao
    -> subtracao
    -> multiplicacao
    -> divisao
Para sair digite: sair
Selecione: """)
    if opcao == "sair":
        break;
    while tabuada <= 10:
        numero = 1
        if opcao == 'adicao':
            while numero <= 10:
                print(f"{tabuada} + {numero} = {tabuada+numero}")
                numero += 1
        elif opcao == 'subtracao':
            while numero <= 10:
                print(f"{tabuada} - {numero} = {tabuada - numero}")
                numero += 1
        elif opcao == 'divisao':
            while numero <= 10:
                print(f"{tabuada} / {numero} = {tabuada / numero}")
                numero += 1
        else:
            while numero <= 10:
                print(f"{tabuada} x {numero} = {tabuada * numero}")
                numero += 1
        tabuada += 1







