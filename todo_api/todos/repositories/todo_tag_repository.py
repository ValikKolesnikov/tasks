from todos.db_services import db_connection


class ToDoTagRepository:
    @db_connection
    def get_all(self, connection=None):
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM todos_todo_tag')
        return cursor.fetchall()

    @db_connection
    def get_by_todo(self, pk, connection=None):
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM todos_todo_tag
                          WHERE todo_id = ?''', (pk,))
        return cursor.fetchall()

    @db_connection
    def delete(self, todo, tag, connection=None):
        cursor = connection.cursor()
        cursor.execute('''DELETE FROM todos_todo_tag
                          WHERE todo_id = ? AND  tag_id = ?''', (todo.id, tag.id))
        connection.commit()

    @db_connection
    def insert(self, instance, connection=None):
        cursor = connection.cursor()
        cursor.execute('''INSERT INTO todos_todo_tag (todo_id, tag_id)
                              VALUES(?, ?)''', (instance.todo_id, instance.tag_id))
        connection.commit()
