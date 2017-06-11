class Local():
    pais = ""
    cidade = ""


    def __init__(self, pais, cidade):
        self.pais = pais
        self.cidade = cidade

    def toJson(self):
        return {"pais": self.pais , "cidade": self.cidade }