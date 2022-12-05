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

    def select_by_time_sub_area(self, time_obj, sub_area):
        print('time_obj', time_obj)
        """
        Search for courser/programs by matching the time and subject area
        param time_obj: a dictionary containing information with days and times
        param subject_area:
        return: list
        """

        sql_values = []
        for day in time_obj['selected_days']:
            sql_values.append(day)

        sql_values.append(time_obj['start_time'])
        sql_values.append(time_obj['end_time'])
        sql_values.append(sub_area)

        # if a value for the start date is passed, add an appropriate sql condition
        start_date_filter = ''
        if time_obj['start_date'] != '':
            start_date_filter = 'AND TrainingProgram.start_date >= ?'
            sql_values.append(time_obj['start_date'])

        # if a value for the end date is passed, add an appropriate sql condition
        end_date_filter = ''
        if time_obj['end_date'] != '':
            end_date_filter = 'AND TrainingProgram.end_date <= ?'
            sql_values.append(time_obj['end_date'])

        query = """
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
                    TrainingProgram.day IN ({})
                AND
                    TrainingProgram.start_time >= ?
                AND
                    TrainingProgram.end_time <= ?
                AND
                    subjects.id = ?
                """.format(','.join('?' for day in time_obj['selected_days']))
        query += start_date_filter
        query += end_date_filter

        conn = self.create_connection()
        cur = conn.cursor()
        cur.execute(query, tuple(sql_values))
        rows = cur.fetchall()
        self.close_connection(conn)
        return rows
