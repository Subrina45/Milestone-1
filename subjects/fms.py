import sqlite3
from sqlite3 import Error

class subjectsModel:

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
        """ create a table from the create_table_sql statement
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        conn = self.create_connection()
        c = conn.cursor()
        c.execute(""" CREATE TABLE IF NOT EXISTS subjects (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    subject_area TEXT NOT NULL
                ); """)
        self.close_connection(conn)

    def add_subject(self, subject):
        """
        Create a new subject into the subjects table
        :param subject:
        :return: subject
        """
        conn = self.create_connection()
        sql = ''' INSERT INTO subjects(subject_area)
                VALUES(?) '''
        cur = conn.cursor()
        cur.execute(sql, subject)
        conn.commit()
        self.close_connection(conn)
        print("added a new subject, ID", cur.lastrowid)
        return cur.lastrowid

    def update_subject(self, subject):
        """
        update subject_id, subject_area of subject
        :param subject:
        """
        conn = self.create_connection()
        sql = ''' UPDATE subjects
                SET
                subject_area = ? 
                WHERE id = ?'''
        cur = conn.cursor()
        cur.execute(sql, subject)
        conn.commit()
        self.close_connection(conn)
        print('Updated', subject)

    def select_all(self):
        """
        Query all rows in the mentors table
        :return:
        """
        conn = self.create_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM subjects")
        rows = cur.fetchall()
        self.close_connection(conn)
        return rows

    def select_subject_by_id(self, id):
        """
        Query subjects by id
        :param id:
        :return:
        """
        conn = self.create_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM subjects WHERE id=?", (id,))
        rows = cur.fetchall()
        self.close_connection(conn)
        return rows

    def select_subject_by_subject_area(self, subject_area):
        """
        Query subjects by subject area
        :param subject_area:
        :return:
        """
        conn = self.create_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM subjects WHERE subject_area LIKE ?", ('%' + subject_area + '%',))
        rows = cur.fetchall()
        self.close_connection(conn)
        return rows

    def delete_subject(self, id):
        print('delete', id)
        """
        Delete a subject by subject id
        :param id: id of the subject
        :return:
        """
        conn = self.create_connection()
        sql = 'DELETE FROM subjects WHERE id=?'
        cur = conn.cursor()
        cur.execute(sql, (id,))
        conn.commit()
        self.close_connection(conn)

    def select_by_name(self, subject_area):
        """
        Query subject area by name
        :param name:
        :return:
        """
        conn = self.create_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM subjects WHERE subject_area=?", (subject_area,))
        rows = cur.fetchall()
        self.close_connection(conn)
        return rows