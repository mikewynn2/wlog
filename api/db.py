import sqlite3
from exceptions import UserExists
import datetime
import os.path

USER_COLUMNS = ['id', 'email', 'username', 'first_name', 'last_name', 'date_created']
POST_COLUMNS = ['id', 'author_id', 'title', 'content', 'date_created', 'date_edited']
COMMENT_COLUMNS = ['id', 'author_id', 'post_id', 'content', 'date_created', 'date_edited']


class DBEngine(object):
    def __init__(self):
        super(DBEngine, self).__init__()

        # if the database was not created yet, create a new db file
        if not os.path.isfile('wlog.db'):
            init_db()

        self.conn = sqlite3.connect('wlog.db')

    def create_user(self, username, email, first_name='', last_name=''):
        try:
            c = self.conn.cursor()
            c.execute(
                """
                INSERT INTO user (username, email, first_name, last_name, date_created)
                          VALUES (?, ?, ?, ?, ?)
                """, [
                    username,
                    email,
                    first_name,
                    last_name,
                    datetime.datetime.utcnow().timestamp()
                ]
            )
            self.conn.commit()
            return c.lastrowid
        except sqlite3.IntegrityError:
            raise UserExists()

    def create_post(self, author, title, content):
        try:
            c = self.conn.cursor()
            c.execute(
                """
                INSERT INTO post (author_id, title, content, date_created, date_edited)
                          VALUES (?, ?, ?, ?, ?)
                """, [
                    author,
                    title,
                    content,
                    datetime.datetime.utcnow().timestamp(),
                    datetime.datetime.utcnow().timestamp()
                ]
            )
            self.conn.commit()
            return c.lastrowid
        except Exception as e:
            print(e)

    def create_comment(self, author, post_id, content, response=None):
        try:
            c = self.conn.cursor()
            if response is None:
                c.execute(
                    """
                    INSERT INTO comment (author_id, post_id, content, date_created, date_edited)
                              VALUES (?, ?, ?, ?, ?)
                    """, [
                        author,
                        post_id,
                        content,
                        datetime.datetime.utcnow().timestamp(),
                        datetime.datetime.utcnow().timestamp(),
                    ]
                )
            else:
                c.execute(
                    """
                    INSERT INTO comment (author_id, post_id, response, content, date_created, date_edited)
                              VALUES (?, ?, ?, ?, ?, ?)
                    """, [
                        author,
                        post_id,
                        response,
                        content,
                        datetime.datetime.utcnow().timestamp(),
                        datetime.datetime.utcnow().timestamp(),
                    ]
                )
            self.conn.commit()
            return c.lastrowid
        except Exception as e:
            print(e)

    def get_users(self):
        try:
            c = self.conn.cursor()
            users = c.execute(
                """SELECT * FROM user ORDER BY id;"""
            ).fetchall()
            return [process_record(USER_COLUMNS, user) for user in users]

        except Exception as e:
            print(e)

    def get_posts(self):
        try:
            c = self.conn.cursor()
            posts = c.execute(
                """SELECT * FROM post ORDER BY id;"""
            ).fetchall()
            return [process_record(POST_COLUMNS, post) for post in posts]

        except Exception as e:
                print(e)

    def get_comments(self, post_id):
        try:
            c = self.conn.cursor()
            comments = c.execute(
                """SELECT * FROM comment WHERE post_id = ? ORDER BY id;""", [post_id]
            ).fetchall()
            return [process_record(COMMENT_COLUMNS, comment) for comment in comments]

        except Exception as e:
            print(e)

    def get_user(self, user_id):
        try:
            c = self.conn.cursor()
            user = c.execute("""SELECT * FROM user WHERE id = ?;""", [user_id]).fetchone()

            return process_record(USER_COLUMNS, user)
        except Exception as e:
            print(e)
            raise e

    def get_post(self, post_id):
        try:
            c = self.conn.cursor()
            post = c.execute("""SELECT * FROM post WHERE id = ?;""", [post_id]).fetchone()

            return process_record(POST_COLUMNS, post)
        except Exception as e:
            print(e)
            raise e

    def get_comment(self, comment_id):
        try:
            c = self.conn.cursor()
            comment = c.execute("""SELECT * FROM comment WHERE id = ?;""", [comment_id]).fetchone()

            return process_record(COMMENT_COLUMNS, comment)
        except Exception as e:
            print(e)
            raise e

    def delete_user(self, user_id):
        try:
            c = self.conn.cursor()
            c.execute("""DELETE FROM user WHERE id = ?;""", [user_id])
            self.conn.commit()
        except Exception as e:
            print(e)

    def delete_post(self, post_id):
        try:
            c = self.conn.cursor()
            c.execute("""DELETE FROM post WHERE id = ?;""", [post_id])
            c.execute("""DELETE FROM comment WHERE post_id = ?;""", [post_id])
            self.conn.commit()
        except Exception as e:
            print(e)

    def delete_comment(self, comment_id):
        try:
            c = self.conn.cursor()
            c.execute("""DELETE FROM comment WHERE id = ?;""", [comment_id])
            self.conn.commit()
        except Exception as e:
            print(e)


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
            response INTEGER,
            content TEXT NOT NULL,
            date_created INTEGER NOT NULL,
            date_edited INTEGER,
            FOREIGN KEY (author_id) REFERENCES user(id),
            FOREIGN KEY (post_id) REFERENCES post(id),
            FOREIGN KEY (response) REFERENCES comment(id)
        )""")

        conn.commit()

        conn.close()
    except Exception as e:
        print(e)
        result = False

    return result


def process_record(column_names, record):
    processed_record = {}
    for i, column in enumerate(column_names):
        processed_record[column] = record[i]
    return processed_record


if __name__ == '__main__':
    init_db()
