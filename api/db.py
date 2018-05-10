import sqlite3


def init_db(db_name=None):
    result = True

    if db_name is None:
        db_name = 'wlog.db'

    try:
        conn = sqlite3.connect(db_name)

        c = conn.cursor()

        c.execute("""
        CREATE TABLE IF NOT EXISTS user(
            id INTEGER PRIMARY KEY,
            email TEXT UNIQUE NOT NULL,
            username TEXT UNIQUE NOT NULL,
            first_name TEXT,
            last_name TEXT,
            date_created INTEGER NOT NULL
        )""")

        c.execute("""
        CREATE TABLE IF NOT EXISTS post(
            id INTEGER PRIMARY KEY,
            author_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            date_created INTEGER NOT NULL,
            date_edited INTEGER,
            FOREIGN KEY (author_id) REFERENCES user(id)
        )""")

        c.execute("""
        CREATE TABLE IF NOT EXISTS comment(
            id INTEGER PRIMARY KEY,
            author_id INTEGER NOT NULL,
            post_id INTEGER NOT NULL,
            content TEXT NOT NULL,
            date_created INTEGER NOT NULL,
            date_edited INTEGER,
            FOREIGN KEY (author_id) REFERENCES user(id),
            FOREIGN KEY (post_id) REFERENCES post(id)
        )""")

        conn.commit()

        conn.close()
    except Exception as e:
        print(e)
        result = False

    return result


if __name__ == '__main__':
    init_db()
