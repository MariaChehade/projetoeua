from funcoes import limpaTela, aguarde

while True:
    limpaTela()
    print("(0) Sair")
    print("(1) Incluir aluno")
    print("(2) Mostrar Lista")
    print("(3) |Deletar todos os registros")
    opcao=input()
    if opcao=="0":
        break
    elif opcao=="1":
        nome=input("Nome: ")
        email=input("E-mail: ")
        arquivo=open("bd.atitus","a")
        arquivo.write(nome+" "+ email+"\n")
        arquivo.close()

        print("Arquivos salvos")
        aguarde(3)
    elif opcao=="2":
        try:
            arquivo=open("bd.atitus","r")
            dados=arquivo.read()
            print(dados)
            arquivo.close()
            aguarde(5)
        except:
            print("Banco de dados não localizado.")
            print("Estamos montando um para você.")
            arquivo=open("bd.atitus","w")
            arquivo.close()
            aguarde(3)
    else:
        print("Opção invalida")
        aguarde(3)
