import sqlite3
from sqlite3 import Error
from todo_api.settings import DATABASES

db_path = DATABASES['default']['NAME']


def db_connection(func):
    def wrapper(*args, **kwargs):
        connection = sqlite3.connect(db_path)
        data = func(*args, **kwargs, connection=connection)
        connection.close()
        return data
    return wrapper
