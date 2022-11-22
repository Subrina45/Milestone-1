import sqlite3
from sqlite3 import Error


class MentorsModel:

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
        c.execute(""" CREATE TABLE IF NOT EXISTS mentors (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    cell_phone TEXT NOT NULL,
                    subject_area TEXT NOT NULL,
                    current_employer TEXT NOT NULL
                ); """)
        self.close_connection(conn)

    def add_mentor(self, mentor):
        """
        Create a new mentor into the mentors table
        :param mentor:
        :return: mentor id
        """
        conn = self.create_connection()
        sql = ''' INSERT INTO mentors(first_name,last_name,email,cell_phone,subject_area,current_employer)
                VALUES(?,?,?,?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, mentor)
        conn.commit()
        self.close_connection(conn)
        print("added a new mentor, ID", cur.lastrowid)
        return cur.lastrowid

    def update_mentor(self, mentor):
        """
        update first_name, last_name, email, cell_phone, subject_area, current_employer of a mentor
        :param mentor:
        """
        conn = self.create_connection()
        sql = ''' UPDATE mentors
                SET first_name = ? ,
                    last_name = ? ,
                    email = ? ,
                    cell_phone = ? ,
                    subject_area = ? , 
                    current_employer = ?
                WHERE id = ?'''
        cur = conn.cursor()
        cur.execute(sql, mentor)
        conn.commit()
        self.close_connection(conn)
        print('Updated', mentor)

    def select_all(self):
        """
        Query all rows in the mentors table
        :return:
        """
        conn = self.create_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM mentors")
        rows = cur.fetchall()
        self.close_connection(conn)
        return rows

    def select_mentor_by_id(self, id):
        """
        Query mentors by id
        :param id:
        :return:
        """
        conn = self.create_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM mentors WHERE id=?", (id,))
        rows = cur.fetchall()
        self.close_connection(conn)
        return rows

    def select_mentor_by_subject_area(self, subject_area):
        """
        Query mentors by subject area
        :param subject_area:
        :return:
        """
        conn = self.create_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM mentors WHERE subject_area LIKE ?", ('%' + subject_area + '%',))
        rows = cur.fetchall()
        self.close_connection(conn)
        return rows

    def delete_mentor(self, id):
        print('delete', id)
        """
        Delete a mentor by mentor id
        :param id: id of the mentor
        :return:
        """
        conn = self.create_connection()
        sql = 'DELETE FROM mentors WHERE id=?'
        cur = conn.cursor()
        cur.execute(sql, (id,))
        conn.commit()
        self.close_connection(conn)