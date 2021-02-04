import sqlite3
from sqlite3 import Error
from todo_api.settings import DATABASES

db_path = DATABASES['default']['NAME']
build_script = 'scripts/table_creation_script.sql'
fill_script = 'scripts/fill.sql'


def db_connection(func):
    def wrapper(*args, **kwargs):
        connection = None
        data = None
        try:
            connection = sqlite3.connect(db_path)
            data = func(*args, **kwargs, connection=connection)
            connection.close()
            return data
        except Error as er:
            print(er)
        finally:
            if connection:
                connection.close()
            return data

    return wrapper

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
