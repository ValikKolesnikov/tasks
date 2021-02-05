from todos.db_services import db_connection
from todo_api.settings import DATABASES

db_path = DATABASES['default']['NAME']
build_script = 'todos/scripts/table_creation_script.sql'
fill_script = 'todos/scripts/fill.sql'


@db_connection
def run_script(script_path, connection=None):
    query = ''
    try:
        with open(script_path, 'r') as script_file:
            query += script_file.read()
        cursor = connection.cursor()
        cursor.executescript(query)
        connection.commit()
    except FileNotFoundError as not_found:
        print(not_found)


if __name__ == '__main__':
    run_script(script_path=build_script)
    run_script(script_path=fill_script)
