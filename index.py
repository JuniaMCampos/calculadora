import os

while True:
    os.system("clear")

    print(" 0: Soma")
    print(" 1: Subtração")
    print(" 2: Multiplicação")
    print(" 3: Divisão")
    print(" 4: Exponenciação")

    print("Escolha a operação que deseja realizar: ")

    operacao = int(input())

    if operacao == 0:
        print("Você escolheu Soma")
        print("Digite um número: ")
        n1 = int(input())
        print("Digite outro número: ")
        n2 = int(input())
        print("A soma de {} e {} é: {} ".format(n1, n2, n1 + n2))    

    elif operacao == 1:
        print("Você escolheu Subtração")
        print("Digite um número: ")
        n1 = int(input())
        print("Digite outro número: ")
        n2 = int(input())
        print("A subtração de {} e {} é: {} ".format(n1, n2, n1 - n2))  

    elif operacao == 2:
        print("Você escolheu Multiplicação")
        print("Digite um número: ")
        n1 = int(input())
        print("Digite outro número: ")
        n2 = int(input())
        print("A multiplicação de {} e {} é: {} ".format(n1, n2, n1 * n2))  

    elif operacao == 3:
        print("Você escolheu Divisão")
        print("Digite um número: ")
        n1 = int(input())
        print("Digite outro número: ")
        n2 = int(input())
        print("A divisão de {} e {} é: {} ".format(n1, n2, n1 / n2))  

    elif operacao == 4:
        print("Você escolheu exponenciação")
        print("Digite a base: ")
        n1 = int(input())
        print("Digite o expoente: ")
        n2 = int(input())
        print("{} elevado a {} é: {} ".format(n1, n2, n1 ** n2))  
    
    else:
        print("Operação não reconhecida")

    print("Deseja fazer outra operação? 0 - Sim, 1 - Não ")
    resposta = int(input())

    if resposta == 1:
        break
    

#Não consegui fazer voltar pro looping depois que o usuario aperta 0


