na=int(input("Cadastre a senha de 0-10 com 1 digito : "))
nf=int(input("Digite sua senha: "))
i=1
if nf!=na:
    while True:
        print("Senha incorreta!")
        nf = int(input("Digite novamente sua senha: "))
        if nf == na:
            print("Senha correta!")
            print(f"Foram {i} tentativa(s)")
            break
        i = i + 1
else:
    print("Senha correta!")
