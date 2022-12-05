import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
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
        self.sel_course_id = None
        self.selected_mentors = []
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
        org_options = [
        "Choose an organization",
        ]
        for organization in orgs:
            org_options.append(organization[1])

        org_name = tk.StringVar()
        org_name.set(org_options[0]) # default value
        tk.OptionMenu(menu_frame,
                    org_name,
                    *org_options,
                    command=lambda e:self.submit_org_choice(org_name.get(), course_table, mentor_prfs_table)).grid(row = 0, column = 1, pady = 10)        
        ## Menu Section End --------------------------------------------------------------------------

        # COURSE TABLE section start -----------------------------------------------
        tk.Label(head_frame,
                text= 'Select a course to see the applications for it',
                bg='pink',
                font=organizations.fonts.main).grid(row = 2, column = 0, pady=25)

        course_frame = tk.Label(head_frame)
        course_frame.grid(row = 3, column = 0)

        course_table = ttk.Treeview(course_frame,
                                    columns=['ID', 'Course ID', 'Course Name', 'Subject Area', 'Organization Name', 
                                            'Start Date', 'End Date', 'Day', 'Start Time', 'End Time'])
        course_t_style = ttk.Style(course_table)
        course_t_style.configure('TreeView')
        course_t_style.map('Treeview', background=[('selected', 'lightgrey')], foreground=[('selected', 'black')])
        course_table.grid(row = 0, column = 0, sticky="NSEW")

        course_table.heading('ID', text='ID')
        course_table.heading('Course ID', text='Course ID')
        course_table.heading('Course Name', text='Course Name')
        course_table.heading('Subject Area', text='Subject Area')
        course_table.heading('Organization Name', text='Organization Name')
        course_table.heading('Day', text='Day')
        course_table.heading('Start Date', text='Start Date')
        course_table.heading('End Date', text='End Date')
        course_table.heading('Start Time', text='Start Time')
        course_table.heading('End Time', text='Start Time')

        course_table.column('#0', anchor=tk.W, width=0, stretch=tk.NO)
        course_table.column('ID', anchor="center", width=40)
        course_table.column('Course ID', anchor="center", width=60)
        course_table.column('Course Name', anchor="center")
        course_table.column('Subject Area', anchor="center")
        course_table.column('Organization Name', anchor="center")
        course_table.column('Day', anchor="center", width=110)
        course_table.column('Start Date', anchor="center", width=110)
        course_table.column('End Date', anchor="center", width=110)
        course_table.column('Start Time', anchor="center", width=90)
        course_table.column('End Time', anchor="center", width=90)
        course_table.bind('<ButtonRelease-1>', lambda e: self.handle_course_sel(e, course_table, mentor_prfs_table))
        # COURSE TABLE section end -----------------------------------------------

        tk.Label(head_frame,
                text= 'Select mentor(s) for the course',
                bg='pink',
                font=organizations.fonts.main).grid(row = 4, column = 0, pady=25)

        mentor_frame = tk.Label(head_frame)
        mentor_frame.grid(row = 5, column = 0)

        mentor_prfs_table = ttk.Treeview(mentor_frame,
                                    columns=['Mentor Id', 'First Name', 'Last Name', 'Mentor Email',
                                        'Cell Phone', 'Subject Area', 'Current Employer'])
        mentor_t_style = ttk.Style(mentor_prfs_table)
        mentor_t_style.configure('TreeView', background=[('selected', 'lightgrey')], foreground=[('selected', 'black')])
        mentor_prfs_table.grid(row = 0, column = 0, sticky="NSEW")

        mentor_prfs_table.heading('#0', text='Approve')
        mentor_prfs_table.heading('Mentor Id', text='Mentor Id')
        mentor_prfs_table.heading('First Name', text='First Name')
        mentor_prfs_table.heading('Last Name', text='Last Name')
        mentor_prfs_table.heading('Mentor Email', text='Mentor Email')
        mentor_prfs_table.heading('Cell Phone', text='Cell Phone')
        mentor_prfs_table.heading('Subject Area', text='Subject Area')
        mentor_prfs_table.heading('Current Employer', text='Current Employer')

        mentor_prfs_table.column('#0', anchor="center", width=110)
        mentor_prfs_table.column('Mentor Id', anchor="center", width=60)
        mentor_prfs_table.column('First Name', anchor="center", width=100)
        mentor_prfs_table.column('Last Name', anchor="center", width=100)
        mentor_prfs_table.column('Mentor Email', anchor="center", width=130)
        mentor_prfs_table.column('Cell Phone', anchor="center", width=100)
        mentor_prfs_table.column('Subject Area', anchor="center", width=200)
        mentor_prfs_table.column('Current Employer', anchor="center", width=200)
        mentor_prfs_table.bind('<ButtonRelease-1>', lambda e: self.handle_mentor_sel(e, mentor_prfs_table))

        submit_selection_lb = tk.Label(head_frame)
        submit_selection_lb.grid(row = 6, column = 0)
        submit_btn = tk.Button(submit_selection_lb,
                                text='Submit',
                                font=organizations.fonts.sub,
                                command=lambda: self.submit_selection())
        submit_btn.grid(row = 1, column = 0)
        return head_frame
        #end of construct frame method ---------------------------------------

    def get_sel_course_id(self):
        return self.sel_course_id

    def set_sel_course_id(self, course_id):
        self.sel_course_id = course_id

    def get_selected_mentors(self):
        return self.selected_mentors

    def set_selected_mentors(self, mentors):
        self.selected_mentors = mentors

    def handle_course_sel(self, event, course_table, mentor_prfs_table):
        cur_row = course_table.identify_row(event.y)
        values = course_table.item(cur_row)['values']
        course_id = values[0]
        self.set_sel_course_id(course_id)
        self.set_selected_mentors([])
        mentor_prfs = self.mentor_prf_model.select_by_course_id(course_id)
        self.populate_preference_table(mentor_prfs_table, mentor_prfs)

    def handle_mentor_sel(self, event, table):
        mentor_ids = self.get_selected_mentors().copy()
        cur_row = table.identify_row(event.y)
        id = table.item(cur_row)['values'][0]
        if id in mentor_ids:
            mentor_ids.remove(id)
            self.toggle_preference_row_tag(table, cur_row)
            self.set_selected_mentors(mentor_ids)
        elif len(mentor_ids) == 2:
            messagebox.showerror("Error", "Cannot choose more than two mentors for the same course.")
        elif len(mentor_ids) < 2:
            mentor_ids.append(id)
            self.toggle_preference_row_tag(table, cur_row)
            self.set_selected_mentors(mentor_ids)

    def toggle_preference_row_tag(self, table, row):
        row_tag = table.item(row, "tags")[0]
        if row_tag == 'checked':
            table.item(row, tags='unchecked')
            table.item(row, image=self.im_unchecked)
        else:
            table.item(row, tags='checked')
            table.item(row, image=self.im_checked)

    def populate_preference_table(self, table, preferences):
        for item in table.get_children():
            table.delete(item)

        for r in range(len(preferences)):
            preference = list(preferences[r]).copy()
            is_approved = preference.pop(-0) # get is_approved status

            img = self.im_unchecked
            tag = 'unchecked'
            if is_approved == 1:
                temp = self.get_selected_mentors().copy()
                temp.append(preference[0])
                self.set_selected_mentors(temp)
                img = self.im_checked
                tag = 'checked'

            table.insert(parent='', index='end',
                        iid=r, values=tuple(preference),
                        image=img, tags=tag)

    def populate_course_table(self, table, courses):
        for item in table.get_children():
            table.delete(item)

        for r in range(len(courses)):
            program_copy = list(courses[r]).copy()
            program_copy.pop(-1) # remove end time type
            program_copy.pop(-2) # remove start time type
            start_day = self.time_con.unixtimestamp_to_date(program_copy[-5]) # start date
            end_day = self.time_con.unixtimestamp_to_date(program_copy[-4]) # end date
            start_time = self.time_con.format_humanreadable(program_copy[-2])
            end_time = self.time_con.format_humanreadable(program_copy[-1])
            program_copy[-5] = start_day
            program_copy[-4] = end_day
            program_copy[-2] = start_time
            program_copy[-1] = end_time
            table.insert(parent='', index='end',
                        iid=r, values=tuple(program_copy))

    def submit_org_choice(self, org_name, course_table, mentor_prfs_table):
        self.set_sel_course_id(None)
        self.set_selected_mentors([])
        self.populate_preference_table(mentor_prfs_table, [])
        programs = self.program_model.select_program_by_org_name(org_name)
        self.populate_course_table(course_table, programs)

    def submit_selection(self):
        row_count = self.mentor_prf_model.set_approved_preferences(str(self.get_sel_course_id()),
                                                        self.get_selected_mentors())
        if row_count > 0:
            messagebox.showinfo("Successful", "Updated Successfully")