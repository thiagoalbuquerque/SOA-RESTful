class Edicao():

    data = ""
    qualis = ""

    def __init__(self, data, qualis):
        self.data = data
        self.qualis = qualis

    def toJson(self):

        return {"data" :self.data, "nome" : self.qualis}