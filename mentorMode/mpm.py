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
        """ create a table from the create_table_sql statement
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """

        # conn = self.create_connection()
        # c = conn.cursor()
        # c.execute(""" CREATE TABLE IF NOT EXISTS mentors (
        #             id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        #             first_name TEXT NOT NULL,
        #             last_name TEXT NOT NULL,
        #             email TEXT NOT NULL,
        #             cell_phone TEXT NOT NULL,
        #             subject_area TEXT NOT NULL,
        #             current_employer TEXT NOT NULL
        #         ); """)
        # self.close_connection(conn)


    def add(self, mentorPreference):
        print('add Called')
        """
        Create a new MentorPreference into the MentorPreference table
        :param MentorPreference:
        :return: 
        """