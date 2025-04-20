nprimeiro=int(input("Digite o primeiro número do intervalo: "))
nultimo=int(input("Digite o último número do intervalo: "))
soma=0
for i in range (nprimeiro,nultimo+1):
    if i%2==0:
        soma = soma + i
        print(f"{i} é Par!",end=" ")
print(f"\nA soma total foi: {soma}")
