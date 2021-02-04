from todos.db_services import db_connection
from todos.models import ToDo, Category


class ToDoRepository:
    @db_connection
    def get_all(self, connection=None):
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM todos_todo')
        return cursor.fetchall()

    @db_connection
    def get(self, pk, connection=None):
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM todos_todo
                          WHERE id = ?''', (pk,))
        return cursor.fetchone()

    @db_connection
    def delete(self, pk, connection=None):
        cursor = connection.cursor()
        cursor.execute('''DELETE FROM todos_todo
                          WHERE id = ?''', (pk,))
        connection.commit()

    @db_connection
    def insert(self, instance, connection=None):
        category_id = instance.category.id if instance.category else None
        cursor = connection.cursor()
        cursor.execute('''INSERT INTO todos_todo (text, category_id)
                              VALUES(?, ?)''', (instance.text, category_id))

        connection.commit()
        return cursor.lastrowid

    @db_connection
    def update(self, instance, connection=None):
        category_id = instance.category.id if instance.category else None
        cursor = connection.cursor()
        cursor.execute('''UPDATE todos_todo
                              SET text = ?,
                                  category_id = ?
                              WHERE id = ?''', [instance.text, category_id, instance.id])
        connection.commit()
        return cursor.lastrowid


