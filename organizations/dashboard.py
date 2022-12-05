import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from programs.tpm import TrainingProgramModel
from mentorPreference.model import MentorPreferenceModel
from timeconverter.converter import TimeConverter
from organizations.om import OrganizationsModel
import organizations.fonts

class OrganizationDashboard(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.pack(side = "top", fill = "both", expand = True)
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)
        self.parent_controller = parent
        self.time_con = TimeConverter()
        self.org_model = OrganizationsModel(r"" + parent.get_db_path())
        self.program_model = TrainingProgramModel(r"" + parent.get_db_path())
        self.mentor_prf_model = MentorPreferenceModel(r"" + parent.get_db_path())
        self.im_checked = ImageTk.PhotoImage(Image.open('checked.png'))
        self.im_unchecked = ImageTk.PhotoImage(Image.open('unchecked.png'))
        self.construct_frame()

    def construct_frame(self):
        time_types = [
        "AM",
        "PM",
        ]

        head_frame = tk.Frame(self)
        head_frame.grid(row = 0, column = 0)
        head_frame.grid_rowconfigure(0, weight = 1)
        head_frame.grid_columnconfigure(0, weight = 1)

        heading_lb = tk.Label(head_frame,
                            text='Organization Dashboard',
                            font=organizations.fonts.main,
                            bg='pink')
        heading_lb.grid(row = 0, column = 0)

        menu_frame = tk.Label(head_frame)
        menu_frame.grid(row = 1, column = 0)

        ## Menu section start ------------------------------------------------------------------
        orgs = self.org_model.select_all()
        # organizations_lb = tk.LabelFrame(menu_frame, text='Organization:', font=organizations.fonts.sub)
        # organizations_lb.grid(row = 0, column = 0, sticky=tk.W, pady = 10)

        org_options = [
        "Choose an organization",
        ]
        for organization in orgs:
            org_options.append(organization[1])

        org_name = tk.StringVar()
        org_name.set(org_options[0]) # default value
        tk.OptionMenu(menu_frame, org_name, *org_options).grid(row = 0, column = 1, pady = 10)

        course_options = [
        "Choose a course",
        ]
        course_name = tk.StringVar()
        course_name.set(course_options[0]) # default value
        tk.OptionMenu(menu_frame, course_name, *course_options).grid(row = 1, column = 1, pady = 10)
        
        ## Menu Section End --------------------------------------------------------------------------
        return head_frame