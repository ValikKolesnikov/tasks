from todos.db_services import db_connection


class CategoryRepository:
    @db_connection
    def get_all(self, connection=None):
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM todos_category')
        return cursor.fetchall()

    @db_connection
    def get(self, pk, connection=None):
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM todos_category
                          WHERE id = ?''', (pk,))
        return cursor.fetchone()

    @db_connection
    def delete(self, pk, connection=None):
        cursor = connection.cursor()
        cursor.execute('''DELETE FROM todos_category
                          WHERE id = ?''', (pk,))
        connection.commit()

    @db_connection
    def insert(self, instance, connection=None):
        cursor = connection.cursor()
        cursor.execute('''INSERT INTO todos_category (name)
                              VALUES(?)''', (instance.name, ))
        connection.commit()



if __name__ == '__main__':
    repo = CategoryRepository()
    a = repo.get(pk=2)
    b = 0
