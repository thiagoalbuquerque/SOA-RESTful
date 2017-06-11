class Publicacao():
    titulo = ""

    def __init__(self, titulo):
        self.titulo = titulo

    def toJson(self):
        return {"titulo": self.titulo}

    def toJsonCompleto(self):
        return {"titulo": self.titulo, "qualis": self.qualis, "nome_autor": self.nome_autor}

    def set_qualis(self,qualis):
        self.__qualis = qualis

    def get_qualis(self):
        return self.__qualis

    def set_nome_autor(self, nome_autor):
        self.__nome_autor = nome_autor

    def get_nome_autor(self):
        return self.__nome_autor

    qualis = property(get_qualis, set_qualis)
    nome_autor = property(get_nome_autor, set_nome_autor)