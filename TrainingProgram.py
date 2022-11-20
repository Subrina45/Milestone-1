import tkinter as tk
import tkinter.messagebox as tkMessage
from tkinter import ttk
import sqlite3
from sqlite3 import Error
import os
import subprocess

class TrainingProgram(tk.Tk):

    def __init__(self) -> None:
        super().__init__()

        script_dir = os.path.abspath( os.path.dirname( __file__ ) )
        print( script_dir )
        conn = self.create_connection(r"" + script_dir +"\mentor_network.db")
        self.create_table(conn)

        cursor = conn.cursor()

        sql = ''' SELECT * FROM TrainingProgram '''
        cursor.execute(sql)
        records = cursor.fetchall()

        print("Total rows are:  ", len(records))

        # Create an instance of tkinter frame
        self.title('My example')
        self.geometry("1000x500")
        
        style = ttk.Style()
        style.theme_names()
        # style.theme_use(self.selected_theme.get())

        btnRefresh = ttk.Button(self, text = 'Refresh', command = self.refresh)
        # btn.configure(command=self.RunWrapper())
        btnRefresh.pack()

        btn = ttk.Button(self, text = 'Add Course', command=self.RunWrapper)
        # btn.configure(command=self.RunWrapper())
        btn.pack()

        topframe = tk.Frame(self, width=900, height=100)
        topframe.pack(fill=tk.BOTH, side=tk.TOP)

        # Add a Treeview widget
        tree = ttk.Treeview(topframe, column=("Course ID", "Course Name", "Subject Area", "Date", "Time"), show='headings', height=100)
        tree.column("# 1", anchor=tk.CENTER)
        tree.heading("# 1", text="Course ID")
        tree.column("# 2", anchor=tk.CENTER)
        tree.heading("# 2", text="Course Name")
        tree.column("# 3", anchor=tk.CENTER)
        tree.heading("# 3", text="Subject Area")
        tree.column("# 4", anchor=tk.CENTER)
        tree.heading("# 4", text="Date")
        tree.column("# 5", anchor=tk.CENTER)
        tree.heading("# 5", text="Time")

        if len(records) > 0:
            for row in records:
                # Insert the data in Treeview widget
                tree.insert('', 'end', text="1", values=(row[1], row[2], row[3], row[4] + "~" + row[5], row[6] + "~" +  row[7]))
        else:
            tree.insert('', 'end', text="1", values=("No Data"))

        tree.grid()


    def refresh(self):
        self.destroy()
        self.__init__()
            
    def RunWrapper(self):
        '''
            Call TrainingProgramAdd.py
        '''
        wrapper = ['python', 'TrainingProgramAdd.py']
        result1 = subprocess.Popen(wrapper,  stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)

    def create_connection(self, db_file):
        """ create a database connection to the SQLite database
            specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)

        return conn


    def create_table(self, conn):
        """ create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        sql_create_organizations_table = """ CREATE TABLE IF NOT EXISTS TrainingProgram (
                                        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                        course_id TEXT NOT NULL,
                                        course_name TEXT NOT NULL,
                                        subject_area TEXT NOT NULL,
                                        start_date TEXT NOT NULL,
                                        end_date TEXT NOT NULL,
                                        start_time TEXT NOT NULL,
                                        end_time TEXT NOT NULL
                                    ); """

        # create tables
        if conn is not None:
            # create organizations table
            try:
                c = conn.cursor()
                c.execute(sql_create_organizations_table)
            except Error as e:
                print(e)
        else:
            print("Error! cannot create the database connection.")

if __name__ == '__main__':
    TP = TrainingProgram()
    TP.mainloop()
