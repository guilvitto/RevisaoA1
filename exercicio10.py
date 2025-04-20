pin=123
tentativas=1
tentativasr=3
resposta="Senha bloqueada!"
while tentativas<=3:
    senha=int(input("Digite a senha númerica de 3 digitos: "))
    if senha==pin:
        resposta="Senha correta!"
        break
    print("Senha incorreta!")
    tentativas += 1
    tentativasr-=1
    if tentativasr>0:
        print(f"Tentativas restantes = {tentativasr}")
print(resposta)



