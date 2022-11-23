import sqlite3
from sqlite3 import Error


class TrainingProgramModel:

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
        c.execute(""" CREATE TABLE IF NOT EXISTS TrainingProgram (
                        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        course_id TEXT NOT NULL,
                        course_name TEXT NOT NULL,
                        subject_area TEXT NOT NULL,
                        start_date TEXT NOT NULL,
                        end_date TEXT NOT NULL,
                        start_time TEXT NOT NULL,
                        end_time TEXT NOT NULL
                ); """)
        self.close_connection(conn)

#
    def add_trainingProgram(self, trainingProgram):
        """
        Create a new trainingProgram into the trainingProgram table
        :param trainingProgram:
        :return: course_id
        """
        conn = self.create_connection()
        sql = ''' INSERT INTO TrainingProgram(course_id,course_name,subject_area,start_date,end_date,start_time,end_time)
              VALUES(?,?,?,?,?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, trainingProgram)
        conn.commit()
        self.close_connection(conn)
        print("added a new record, ID", cur.lastrowid)
        return cur.lastrowid

    def update_trainingProgram(self, trainingProgram):
        """
        update course_id, course_name, subject_area, start_date, end_date, start_time,and end_date  of trainingProgram
        :param trainingProgram:
        """
        conn = self.create_connection()
        sql = ''' UPDATE TrainingProgram
                SET course_id = ? ,
                    course_name = ? ,
                    subject_area = ? ,
                    start_date = ? ,
                    end_date = ? ,
                    start_time = ? ,
                    end_time = ?
                WHERE id = ?'''
        cur = conn.cursor()
        cur.execute(sql, trainingProgram)
        conn.commit()
        self.close_connection(conn)
        print('Updated', trainingProgram)

    def select_all(self):
        """
        Query all rows in the trainingProgram table
        :return:
        """
        conn = self.create_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM TrainingProgram")
        rows = cur.fetchall()
        self.close_connection(conn)
        return rows

    def delete_trainingProgram(self, id):
        print('deleted', id)
        """
        Delete an trainingProgram by course_id
        :param id: id of the trainingProgram
        :return:
        """
        conn = self.create_connection()
        sql = 'DELETE FROM TrainingProgram WHERE id=?'
        cur = conn.cursor()
        cur.execute(sql, (id,))
        conn.commit()
        self.close_connection(conn)

    def select_program_by_id(self, id):
        """
        Query TrainingProgram by id
        :param id:
        :return:
        """
        conn = self.create_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM TrainingProgram WHERE id=?", (id,))
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