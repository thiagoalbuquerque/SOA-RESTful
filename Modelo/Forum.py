class forum():

    nome = ""
    tipo = ""
    sigla = ""


    def __init__(self, nome, tipo, sigla ):
        self.nome = nome
        self.tipo = tipo
        self.sigla = sigla

    def toJson(self):

        return {"nome" :self.nome, "tipo" : self.tipo, "sigla" : self.sigla}