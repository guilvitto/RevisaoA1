qtd_alunos=int(input("Digite o número de alunos: "))
for i in range(1,qtd_alunos+1):
    aluno=input("Digite o nome do aluno: ")
    n1=float(input("Digite a nota 1 do aluno: "))
    while n1<0 or n1>10:
        print("Nota inválida! 0-10")
        n1 = float(input("Digite novamente a nota 1 do aluno: "))
    n2 = float(input("Digite a nota 2 do aluno: "))
    while n2<0 or n2>10:
        print("Nota inválida! 0-10")
        n2=float(input("Digite novamente a nota 2 do aluno: "))
    media = (n1+n2)/2
    print(f"A média de {aluno} foi: {media}")
    if media<5:
        print(f"{aluno} está reprovado!")
    elif media>=7:
        print(f"{aluno} está aprovado!")
    else:
        print(f"{aluno} está em recuperação!")

