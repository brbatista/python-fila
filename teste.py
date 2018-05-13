import Fila

def teste():
    print("*********************************")
    print("*******Fila de alunos!*******")
    print("*********************************")

    fila = Fila.Fila()

    escolha = 0

    while(escolha != 5):
        print("(1) Adicionar (2) Remover (3) Verificar se lista está vazia (4) Olhar fila (5) Sair")
        escolha = int(input("Escolha uma ação: "))

        if(escolha == 1):
            aluno = input("Digite o nome do aluno: ")
            fila.insere(aluno)

        elif(escolha == 2):
            print("Removendo aluno")
            fila.remove()

        elif(escolha == 3):
            if(fila.vazia()):
                print("Fila está vazia")
            else:
                print("Fila não está vazia")

        elif(escolha == 4):
            fila.olhar_fila()

if(__name__ == "__main__"):
    teste()