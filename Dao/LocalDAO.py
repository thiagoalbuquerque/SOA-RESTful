from Dao.Dao import DAO


class LocalDAO(DAO):
    def get(self):
        con = self.get_connection
        cur = con.cursor()
        con.commit()
        cur.execute('SELECT * FROM local')
        return cur.fetchall()

    def insert(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass