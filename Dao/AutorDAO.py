from Dao.Dao import DAO


class AutorDAO(DAO):
    def get(self):
        con = self.get_connection
        cur = con.cursor()
        con.commit()
        cur.execute('SELECT * FROM autor')
        return cur.fetchall()

    def insert(self, args):
        con = self.get_connection
        cur = con.cursor()
        print('insert into autor (cpf, nome) VALUES (%s, %s)', (args[0],args[1]))
        cur.execute("""insert into autor (cpf, nome) VALUES (%s, %s)""", (args[0],args[1]))
        con.commit()
        #autores = cur.fetchall()

    def update(self, args):
        con = self.get_connection
        cur = con.cursor()
        cur.execute("""UPDATE autor SET nome = %s WHERE cpf = %s;""", (args[1], args[0]))
        con.commit()

    def delete(self, args):
        pass