import sqlite3
from sqlite3 import Error


class MentorPreferenceModel:

    def __init__(self, path_to_db):
        self.path = path_to_db
        self.create_table()

    def create_connection(self):
        """ create a database connection to the SQLite database
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(self.path)
            return conn
        except Error as e:
            print(e)

        return conn

    def close_connection(self, conn):
        conn.close()

    def create_table(self):
        """ create a table named mentor_preferences
        """
        conn = self.create_connection()
        c = conn.cursor()
        c.execute("""
                    CREATE TABLE IF NOT EXISTS mentor_preferences (
                        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        mentor_id INTEGER NOT NULL,
                        program_id INTEGER NOT NULL,
                        is_approved TINYINT DEFAULT 0,
                        UNIQUE(mentor_id, program_id)
                    );
                """)
        self.close_connection(conn)

    def add(self, course_ids, mentor_id):
        """
        Create a new mentor preference(s) into the mentor_preferences table
        param preferences:
        """
        values = []
        for id in course_ids:
            values.append(mentor_id)
            values.append(id)

        conn = self.create_connection()
        sql = 'INSERT INTO mentor_preferences(mentor_id, program_id)'
        sql += ' VALUES '

        values_for_sql = []
        for id in course_ids: # as many values as the number of course ids
            values_for_sql.append('(?,?)')
        sql += ",".join(values_for_sql)

        cur = conn.cursor()
        cur.execute(sql, tuple(values))
        conn.commit()
        self.close_connection(conn)
