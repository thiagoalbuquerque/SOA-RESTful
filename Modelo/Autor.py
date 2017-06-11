class Autor():

    cpf = ""
    nome = ""

    def __init__(self, cpf, nome):
        self.cpf = cpf
        self.nome = nome

    def toJson(self):

        return {"cpf" :self.cpf, "nome" : self.nome}