import tkinter as tk
from tkinter import ttk
import mentorPreference.fonts


class StartPage(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.main_frame_row = 0
        self.parent = parent
        self.pack(side = "top", fill = "both", expand = True)
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)
        self.construct_frame()

    def increment_main_frame_row(self):
        self.main_frame_row += 1

    def construct_frame(self):
        label = ttk.Label(self, text = "Mentor Preference & Availability Dashboard", font = mentorPreference.fonts.LARGEFONT)
        label.grid(row = self.main_frame_row, column = 0)
        self.increment_main_frame_row()

        ttk.Label(self, text = "Please log in", font = mentorPreference.fonts.LARGEFONT).grid(row = self.main_frame_row, column = 0)
        self.increment_main_frame_row()

        menu_frame = ttk.Label(self)
        menu_frame.grid(row = self.main_frame_row, column = 0)
        self.increment_main_frame_row()

        entries_container = tk.Label(menu_frame)
        entries_container.grid(row = self.main_frame_row, column = 0, sticky="NSEW")
        self.increment_main_frame_row()

        tk.Label(entries_container, text='ID:', font=mentorPreference.fonts.sub).grid(row = 0, column = 0)
        id = tk.Entry(entries_container, font=mentorPreference.fonts.sub)
        id.grid(row = 0, column = 1, pady = 10)

        tk.Label(entries_container, text='First Name:', font=mentorPreference.fonts.sub).grid(row = 1, column = 0)
        first_name = tk.Entry(entries_container, font=mentorPreference.fonts.sub)
        first_name.grid(row = 1, column = 1, pady = 10)

        tk.Label(entries_container, text='Last Name:', font=mentorPreference.fonts.sub).grid(row = 2, column = 0)
        last_name = tk.Entry(entries_container, font=mentorPreference.fonts.sub)
        last_name.grid(row = 2, column = 1, pady = 10)

        submit_btn = ttk.Button(menu_frame, text="Submit", command = lambda : self.parent.submit_login(id, first_name, last_name))
        submit_btn.grid(row = self.main_frame_row, column = 0, pady=15)
        self.increment_main_frame_row()
