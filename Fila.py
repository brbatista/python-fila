class Fila(object):

    def __init__(self):
        self.alunos = []

    def insere(self, aluno):
        ultima_posicao = len(self.alunos)
        self.alunos.insert(ultima_posicao, aluno)

    def remove(self):
        if(not self.vazia()):
            self.alunos.pop(0)
        else:
            print("Lista está vazia")

    def vazia(self):
        return len(self.alunos) == 0

    def olhar_fila(self):
        i = 0
        total_alunos = len(self.alunos)
        while(i < total_alunos):
            print(self.alunos[i])
            i+=1


