nome = input(f"Olá, bem vindo ao teste de operações condicionais! Qual seu nome? ")

print(f"Olá, {nome}. Seja Bem vindo.")
print(f"este é um teste do operações condicionais")

entrada = input(f"você deseja entrar ou sair? ")


if entrada == "entrar":
    print(f"seja bem vindo {nome}!")

elif entrada =="sair":
    print(f"obrigado {nome} por sair do sistema. Até a próxima!")

else:
    print(f"{nome} está digitando uma opção que não é válida.")

entrar = input(f" você sabe sua senha?")

if entrar == "sim":
    print(f"obrigado")
else:
    print(f"até logo")


senha = input(f"Qual sua senha?")

if senha == "casaamarela":
    print(f"senha correta")
else: 
    print(f"senha incorreta")


print(f"obrigado por entrar no sistema")



