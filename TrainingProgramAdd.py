import tkinter as tk
import sqlite3
from sqlite3 import Error
import os

script_dir = os.path.abspath( os.path.dirname( __file__ ) )

print( script_dir )

def create_connection(db_file):
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

conn = create_connection(r"" + script_dir +"\mentor_network.db")

# Form ====================================================================================

window = tk.Tk()
window.title('My example')
window.geometry("700x250")

title_text = tk.Label(master=window,text="Admin Dashboard for adding, deleting, and modifying Courses/Training Programs")
title_text.grid(column=0, row=0)

course_id_label = tk.Label(master=window,text="Course ID")
course_id_label.grid(column=0, row=1)
course_id_entry = tk.Entry(master=window,width=50)
course_id_entry.grid(column=1, row=1)

course_name_label = tk.Label(master=window,text="Course Name")
course_name_label.grid(column=0, row=2)
course_name_entry = tk.Entry(master=window,width=50)
course_name_entry.grid(column=1, row=2)

subj_area_label = tk.Label(master=window,text="Subject Area")
subj_area_label.grid(column=0, row=3)
subj_area_entry = tk.Entry(master=window,width=50)
subj_area_entry.grid(column=1, row=3)

start_date_label = tk.Label(master=window,text="Start Date")
start_date_label.grid(column=0, row=4)
start_date_entry = tk.Entry(master=window,width=50)
start_date_entry.grid(column=1, row=4)

end_date_label = tk.Label(master=window,text="End Date")
end_date_label.grid(column=0, row=5)
end_date_entry = tk.Entry(master=window,width=50)
end_date_entry.grid(column=1, row=5)

start_time_label = tk.Label(master=window,text="Start Time")
start_time_label.grid(column=0, row=6)
start_time_entry = tk.Entry(master=window,width=50)
start_time_entry.grid(column=1, row=6)

end_time_label = tk.Label(master=window,text="End Time")
end_time_label.grid(column=0, row=7)
end_time_entry = tk.Entry(master=window,width=50)
end_time_entry.grid(column=1, row=7)

def add_training(conn, training_info):
    """
    Create a new training program into the TrainingProgram table
    :param conn:
    :param TrainingProgram:
    :return: TrainingProgram id
    """
    sql = ''' INSERT INTO TrainingProgram(course_id,course_name,subject_area,start_date,end_date,start_time,end_time)
              VALUES(?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, training_info)
    conn.commit()
    return cur.lastrowid

def submitData():
    course_id_value = course_id_entry.get()
    course_name_value = course_name_entry.get()
    subj_area_value = subj_area_entry.get()
    start_date_value = start_date_entry.get()
    end_date_value = end_date_entry.get()
    start_time_value = start_time_entry.get()
    end_time_value = end_time_entry.get()

    training_info = (course_id_value, course_name_value, subj_area_value, start_date_value, end_date_value, start_time_value, end_time_value)
    training_id = add_training(conn, training_info)

    output_text = tk.Text(master=window, height=2, spacing1=10)
    output_text.grid(column=0, row=41)
    output_text.insert(tk.END, "Course ID: " + str(training_id) + ". Training Program successfully inserted.")
    window.destroy()

submit_button = tk.Button(text="Submit", command=submitData).grid(column=0, row=39)
quit_button = tk.Button(text="Quit", command=window.destroy).grid(column=0, row=40)

window.mainloop()
