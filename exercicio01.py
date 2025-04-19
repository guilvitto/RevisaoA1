repetir=5
while repetir==5:
    n1= float(input("Digite o primeiro número: "))
    n2= float(input("Digite o segundo número: "))
    operacao= int(input("Digite a operação(SOMA=1, SUBTRAÇÃO=2, MULTIPLICAÇÃO=3, DIVISÃO=4, REPETIR=5, SAIR=6): "))
    if operacao==1:
        print("Você escolheu a soma! ")
        resultado=n1+n2
        print(f"Sua soma = {resultado}\nPrograma finalizado!")
        break
    elif operacao == 2:
        print("Você escolheu a subtração! ")
        resultado = n1 - n2
        print(f"Sua subtração = {resultado}\nPrograma finalizado!")
        break
    elif operacao == 3:
        print("Você escolheu a multiplicação! ")
        resultado = n1 * n2
        print(f"Sua multiplicação = {resultado}\nPrograma finalizado!")
        break
    elif operacao == 4:
        print("Você escolheu a divisão! ")
        resultado = n1 / n2
        print(f"Sua divisão = {resultado}\nPrograma finalizado!")
        break
    elif operacao == 5:
        repetir = operacao
        print("Reiniciando...")
    else:
        print("Programa finalizado!")
        repetir = operacao