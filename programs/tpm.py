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
                        day TEXT NOT NULL,
                        start_time TEXT NOT NULL,
                        start_time_type TEXT NOT NULL,
                        end_time TEXT NOT NULL,
                        end_time_type TEXT NOT NULL,
                        organization_id INTEGER NULL
                ); """)
        self.close_connection(conn)

    def add_trainingProgram(self, trainingProgram):
        print('add_trainingProgram Called')
        """
        Create a new trainingProgram into the trainingProgram table
        :param trainingProgram:
        :return: course_id
        """
        conn = self.create_connection()
        sql = '''
                INSERT INTO TrainingProgram(course_id, course_name,
                                            subject_area,
                                            start_date, end_date,
                                            day,
                                            start_time, start_time_type,
                                            end_time, end_time_type,
                                            organization_id)
                VALUES(?,?,?,?,?,?,?,?,?,?,?)
            '''
        cur = conn.cursor()
        cur.execute(sql, trainingProgram)
        conn.commit()
        self.close_connection(conn)
        print("added a new record, ID", cur.lastrowid)
        return cur.lastrowid

    def update_trainingProgram(self, trainingProgram):
        """
        update course_id, course_name, 
                subject_area, start_date, 
                end_date, start_time, day,
                start_time_type,
                end_time, end_time_type, and
                organization_id of trainingProgram
        :param trainingProgram:
        """
        conn = self.create_connection()
        sql = ''' UPDATE TrainingProgram
                SET course_id = ? ,
                    course_name = ? ,
                    subject_area = ? ,
                    start_date = ? ,
                    end_date = ? ,
                    day = ? ,
                    start_time = ? ,
                    start_time_type = ? ,
                    end_time = ? ,
                    end_time_type = ? ,
                    organization_id = ?
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
        cur.execute("""
                    SELECT 
                        TrainingProgram.id,
                        TrainingProgram.course_id,
                        TrainingProgram.course_name,
                        subjects.subject_area,
                        organizations.name,
                        TrainingProgram.start_date,
                        TrainingProgram.end_date,
                        TrainingProgram.day,
                        TrainingProgram.start_time,
                        TrainingProgram.start_time_type,
                        TrainingProgram.end_time,
                        TrainingProgram.end_time_type
                    FROM TrainingProgram
                    JOIN organizations
                    ON organizations.id = TrainingProgram.organization_id
                    JOIN subjects
                    ON subjects.id = TrainingProgram.subject_area"""
                )
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
        cur.execute("""
                    SELECT TrainingProgram.*, organizations.name, subjects.subject_area
                    FROM TrainingProgram 
                    JOIN organizations 
                    ON organizations.id = TrainingProgram.organization_id
                    JOIN subjects
                    ON subjects.id = TrainingProgram.subject_area
                    WHERE TrainingProgram.id=?
                    """, (id,))
        rows = cur.fetchall()
        self.close_connection(conn)
        return rows

    def select_program_by_org_name(self, org_name):
        """
        Query mentors by subject area
        :param subject_area:
        :return:
        """
        conn = self.create_connection()
        cur = conn.cursor()
        cur.execute("""
                    SELECT
                        TrainingProgram.id,
                        TrainingProgram.course_id,
                        subjects.subject_area,
                        TrainingProgram.course_name,
                        organizations.name,
                        TrainingProgram.start_date,
                        TrainingProgram.end_date,
                        TrainingProgram.day,
                        TrainingProgram.start_time,
                        TrainingProgram.start_time_type,
                        TrainingProgram.end_time,
                        TrainingProgram.end_time_type
                    FROM TrainingProgram
                    JOIN organizations 
                    ON organizations.id = TrainingProgram.organization_id
                    JOIN subjects
                    ON subjects.id = TrainingProgram.subject_area
                    WHERE organizations.name LIKE ?
                    """, ('%' + org_name + '%',))
        rows = cur.fetchall()
        self.close_connection(conn)
        return rows

    def select_program_by_time(self, start_time, end_time):
        print('start_time', start_time, 'end_time', end_time)
        """
        Query mentors by subject area
        :param subject_area:
        :return:
        """
        conn = self.create_connection()
        cur = conn.cursor()
        cur.execute("""
                    SELECT
                        TrainingProgram.id,
                        TrainingProgram.course_id,
                        subjects.subject_area,
                        TrainingProgram.course_name,
                        organizations.name,
                        TrainingProgram.start_date,
                        TrainingProgram.end_date,
                        TrainingProgram.day,
                        TrainingProgram.start_time,
                        TrainingProgram.start_time_type,
                        TrainingProgram.end_time,
                        TrainingProgram.end_time_type
                    FROM TrainingProgram
                    JOIN organizations 
                    ON organizations.id = TrainingProgram.organization_id
                    JOIN subjects
                    ON subjects.id = TrainingProgram.subject_area
                    WHERE
                        TrainingProgram.start_time >= ?
                    AND
                        TrainingProgram.end_time <= ?
                    """, (start_time, end_time))
        rows = cur.fetchall()
        self.close_connection(conn)
        return rows

