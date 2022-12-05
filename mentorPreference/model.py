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
                        is_pending TINYINT DEFAULT 1,
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

    def select_by_course_id(self, course_id):
        """
        Query mentor preferences by the course id
        param course_id:
        return:
        """

        conn = self.create_connection()
        cur = conn.cursor()
        cur.execute("""
                    SELECT
                        mentor_preferences.is_approved,
                        mentors.id,
                        mentors.first_name,
                        mentors.last_name,
                        mentors.email,
                        mentors.cell_phone,
                        mentors.subject_area,
                        mentors.current_employer
                    FROM mentor_preferences
                    JOIN mentors 
                    ON mentors.id = mentor_preferences.mentor_id
                    WHERE mentor_preferences.program_id = ?
                    """,
                    (course_id,))
        rows = cur.fetchall()
        self.close_connection(conn)
        return rows

    def select_by_mentor_id(self, mentor_id):
        """
        Query mentor preferences by the mentor id
        param mentor_id:
        return:
        """
        conn = self.create_connection()
        cur = conn.cursor()
        cur.execute("""
                    SELECT
                        *
                    FROM mentor_preferences
                    WHERE mentor_preferences.mentor_id = ?
                    """,
                    (mentor_id,))
        rows = cur.fetchall()
        self.close_connection(conn)
        return rows


    def set_approved_preferences(self, program_id, mentor_ids):
        """
        Update is_approved column for the passed mentor ids with the passed course id
        param program_id:
        param mentor_ids: list containing mentor ids
        return:
        """
        conn = self.create_connection()
        cur = conn.cursor()
        # first reset is_approved column of all rows to 0
        # that have program_id column equals to a passed program_id
        query = """
                UPDATE mentor_preferences
                SET is_approved = 0
                WHERE program_id = ?
                """
        cur.execute(query, tuple(program_id,))

        if len(mentor_ids) > 0:
            query = """
                    UPDATE mentor_preferences
                    SET is_approved = 1
                    WHERE program_id = ?
                    AND mentor_id IN ({})
                    """.format(','.join('?' for id in mentor_ids))
            cur.execute(query, tuple(program_id,) + tuple(mentor_ids))
        conn.commit()
        self.close_connection(conn)
        return cur.rowcount
                        