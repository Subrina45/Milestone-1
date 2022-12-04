import tkinter as tk
from tkinter import ttk

LARGEFONT = ("Verdana", 35)

class StartPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.pack(side = "top", fill = "both", expand = True)
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)

        label = ttk.Label(self, text ="Admin Dashboard", font = LARGEFONT)
        label.grid(row = 0, column = 0)

        menu_frame = ttk.Label(self)
        menu_frame.grid(row = 1, column = 0)

        button1 = ttk.Button(menu_frame, text ="Organizations", command = lambda : parent.show_frame('Organizations'))
        button1.grid(row = 0, column = 0, padx=15, pady=15)
  
        button2 = ttk.Button(menu_frame, text ="Programs / Courses", command = lambda : parent.show_frame('TrainingProgram'))
        button2.grid(row = 0, column = 1, padx=15, pady=15)
        
        button3 = ttk.Button(menu_frame, text = "Mentors", command = lambda : parent.show_frame('Mentors'))
        button3.grid(row = 1, column = 0, padx=15, pady=15)

        # added by Jye & Elvira to connect the new mentor preference dashboard 
        # button4 = ttk.Button(menu_frame, text = "Mentor Mode", command = lambda : parent.show_frame('MentorPreferences'))
        # button4.grid(row = 1, column = 1, padx=15, pady=15)

        button5 = ttk.Button(menu_frame, text = "Forms", command = lambda : parent.show_frame('SubjectsForm'))
        button5.grid(row = 1, column = 1, padx=15, pady=15)