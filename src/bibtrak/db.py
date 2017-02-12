import sqlite3

database_filename = ".bibtrak.db"

def get_db_file(directory=None):
    import os

    if directory is None:
        directory = os.getcwd()

    return os.path.join(directory, database_filename)


def init(directory=None):
    import os

    database = get_db_file(directory=directory)

    if os.path.exists(database):
        raise FileExistsError

    # Create db
    with sqlite3.connect(database) as conn:
        c = conn.cursor()

        c.execute("""
            CREATE TABLE database
            (id text, key text, val text)
        """)

        conn.commit()


def fetch(database, handler, handler_id, id):
    data = handler.fetch(handler_id)
    for key, value in data.items():
        insert(database, id, key, value)


def insert(database, id, key, value):
    with sqlite3.connect(database) as conn:
        c = conn.cursor()

        c.execute("""
            INSERT INTO database
            VALUES (?,?,?)
        """, (id, key, value))

        conn.commit()


def insert_all(database, id, keys, values):
    for key, value in zip(keys, values):
        insert(database, id, key, value)


def link(database, id, filename):
    with sqlite3.connect(database) as conn:
        c = conn.cursor()

        c.execute("""
            INSERT INTO database
            VALUES (?,?,?)
        """, (id, "file", filename))

        conn.commit()


def find_file(database, field, query):
    with sqlite3.connect(database) as conn:
        c = conn.cursor()

        result = c.execute("""
            SELECT id FROM database
            WHERE key=? and val LIKE ?
        """, (field, query))

        for r in result:
            print(r)

        conn.commit()
