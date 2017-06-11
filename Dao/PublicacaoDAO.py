from Dao.Dao import DAO


class PublicacaoDAO(DAO):
    def get(self):
        con = self.get_connection
        cur = con.cursor()
        con.commit()
        cur.execute('SELECT * FROM publicacao')
        return cur.fetchall()


    def get_publicacoes_by_autor(self, cpf):
        con = self.get_connection
        cur = con.cursor()
        cur.execute("SELECT pub.titulo, e.qualis, autor.nome FROM Edicao e "
                    "INNER JOIN publicacao pub ON e.idedicao = pub.id_edicao "
                    "INNER JOIN publicacao_autor pa ON pub.id = pa.id "
                    "INNER JOIN autor ON autor.cpf = pa.cpf WHERE autor.cpf = %s;",(cpf,))
        con.commit()
        return cur.fetchall()

    def insert(self, titulo):
        con = self.get_connection
        cur = con.cursor()
        cur.execute("""INSERT INTO publicacao(titulo) VALUES (%s);""", (titulo,))
        con.commit()
        cur.close()
        con.close()

    def update(self):
        pass

    def delete(self):
        pass
