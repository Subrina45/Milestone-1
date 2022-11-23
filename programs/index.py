import tkinter as tk
from tkinter import ttk
from programs.tpm import TrainingProgramModel
from organizations.om import OrganizationsModel
import programs.fonts

class TrainingProgram(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.pack(side = "top", fill = "both", expand = True)
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)
        self.parent_controller = parent
        self.model = TrainingProgramModel(r"" + parent.get_db_path())
        self.org_model = OrganizationsModel(r"" + parent.get_db_path())
        self.container = self.get_initial_frame(self)

    def get_initial_frame(self, parent_frame):
        head_frame = tk.Frame(parent_frame)
        head_frame.pack(pady=10)
        head_frame.pack_propagate(False)
        head_frame.configure(width=400, height=600)

        heading_lb = tk.Label(head_frame, text='Programs and Courses Registration System',
                     font=programs.fonts.main,
                     bg='pink')
        heading_lb.pack(fill=tk.X, pady=5)

        course_id_lb = tk.Label(head_frame, text='Course ID:', font=programs.fonts.sub)
        course_id_lb.place(x=0, y=40)
        course_id_entry = tk.Entry(head_frame, font=programs.fonts.sub)
        course_id_entry.place(x=110, y=40, width=180)

        course_name_lb = tk.Label(head_frame, text='Course Name:', font=programs.fonts.sub)
        course_name_lb.place(x=0, y=80)
        course_name_entry = tk.Entry(head_frame, font=programs.fonts.sub)
        course_name_entry.place(x=110, y=80, width=180)

        subject_area_lb = tk.Label(head_frame, text='Subject Area:', font=programs.fonts.sub)
        subject_area_lb.place(x=0, y=120)
        subject_area_entry = tk.Entry(head_frame, font=programs.fonts.sub)
        subject_area_entry.place(x=110, y=120, width=180)


        # Drop down menu to choose an university or organization
        # --------------------------------------------------------------------------------    
        organizations = self.org_model.select_all()
        organizations_lb = tk.Label(head_frame, text='Organization:', font=programs.fonts.sub)
        organizations_lb.place(x=0, y=160)
        options = [
        "Choose an organization",
        ]

        for organization in organizations:
            options.append(organization[1])

        op_menu_value = tk.StringVar()
        op_menu_value.set(options[0]) # default value
        w = tk.OptionMenu(head_frame, op_menu_value, *options)
        w.place(x=110, y=160, width=180)
        # --------------------------------------------------------------------------------   


        start_date_lb = tk.Label(head_frame, text='Start Date:', font=programs.fonts.sub)
        start_date_lb.place(x=0, y=200)

        start_date_entry = tk.Entry(head_frame, font=programs.fonts.sub)
        start_date_entry.place(x=110, y=200, width=180)

        end_date_lb = tk.Label(head_frame, text='End Date:', font=programs.fonts.sub)
        end_date_lb.place(x=0, y=250)

        end_date_entry = tk.Entry(head_frame, font=programs.fonts.sub)
        end_date_entry.place(x=110, y=250, width=180)

        start_time_lb = tk.Label(head_frame, text='Start Time:', font=programs.fonts.sub)
        start_time_lb.place(x=0, y=300)

        start_time_entry = tk.Entry(head_frame, font=programs.fonts.sub)
        start_time_entry.place(x=110, y=300, width=180)

        end_time_lb = tk.Label(head_frame, text='End Time:', font=programs.fonts.sub)
        end_time_lb.place(x=0, y=350)

        end_time_entry = tk.Entry(head_frame, font=programs.fonts.sub)
        end_time_entry.place(x=110, y=350, width=180)

        #______________________________Buttons____________________________________________________
        register_btn = tk.Button(head_frame, text='Register', font=programs.fonts.mid,
                                command=lambda: self.add_program(record_table, [course_id_entry, course_name_entry, 
                                                                subject_area_entry, start_date_entry, end_date_entry,
                                                                start_time_entry, end_time_entry], op_menu_value))
        register_btn.place(x=0, y=400)

        update_btn = tk.Button(head_frame, text='Update', font=programs.fonts.mid,
                            command=lambda: self.update_program(record_table, course_id_entry, course_name_entry, 
                                                                subject_area_entry, start_date_entry, end_date_entry,
                                                                start_time_entry, end_time_entry, op_menu_value))
        update_btn.place(x=85, y=400)

        delete_btn = tk.Button(head_frame, text='Delete', font=programs.fonts.mid,
                            command=lambda: self.delete_program(record_table, [course_id_entry, course_name_entry, 
                                                                subject_area_entry, start_date_entry, end_date_entry,
                                                                start_time_entry, end_time_entry], op_menu_value))
        delete_btn.place(x=160, y=400)

        clear_btn = tk.Button(head_frame, text='Clear', font=programs.fonts.mid,
                            command=lambda: self.clear_inputs([course_id_entry, course_name_entry, 
                                                                subject_area_entry, start_date_entry, end_date_entry,
                                                                start_time_entry, end_time_entry], op_menu_value)
                            )
        clear_btn.place(x=230, y=400)

        back_btn = tk.Button(head_frame, text ="Back", font=programs.fonts.mid,
                            command = lambda : self.parent_controller.show_frame('StartPage'))
        back_btn.place(x=230, y=450)
        #________________________________Buttons____________________________________________________

        search_bar_frame = tk.Frame(parent_frame)

        search_lb = tk.Label(search_bar_frame,
                            text='Search a course/program for a specified university or training organization',
                            font=programs.fonts.sub)
        search_lb.pack(anchor=tk.W)

        search_by_org_entry = tk.Entry(search_bar_frame,
                            font=programs.fonts.sub)
        search_by_org_entry.pack(anchor=tk.W)

        #New______________________________________________________________________________
        search_by_org_entry.bind('<KeyRelease>', lambda e: self.find_program_by_org(record_table, search_by_org_entry.get()))
        #_________________________________________________________________________________

        search_bar_frame.pack(pady=0)
        search_bar_frame.pack_propagate(False)
        search_bar_frame.configure(width=400, height=50)

        record_frame = tk.Frame(parent_frame)
        record_frame.pack(pady=10)
        record_frame.pack_propagate(False)
        record_frame.configure(width=900, height=700)

        record_lb = tk.Label(record_frame, text= 'Select Record for Delete or Update',
                            bg='pink', font=programs.fonts.main)
        record_lb.pack(fill=tk.X)

        record_table = ttk.Treeview(record_frame)
        record_table.pack(fill=tk.X, pady=5)
                            
        #New___________________________________________________________________
        record_table.bind('<ButtonRelease-1>', lambda e: self.put_into_entries(record_table, course_id_entry, course_name_entry, 
                                                                            subject_area_entry, start_date_entry, end_date_entry,
                                                                            start_time_entry, end_time_entry, op_menu_value))
        #______________________________________________________________________

        record_table['column'] = ['ID', 'Course ID', 'Course Name', 'Subject Area', 'Organization Name', 
                                'Start Date', 'End Date', 'Start Time', 'End Time']

        record_table.heading('ID', text='ID', anchor=tk.W)
        record_table.heading('Course ID', text='Course ID', anchor=tk.W)
        record_table.heading('Course Name', text='Course Name', anchor=tk.W)
        record_table.heading('Subject Area', text='Subject Area', anchor=tk.W)
        record_table.heading('Organization Name', text='Organization Name', anchor=tk.W)
        record_table.heading('Start Date', text='Start Date', anchor=tk.W)
        record_table.heading('End Date', text='End Date', anchor=tk.W)
        record_table.heading('Start Time', text='Start Time', anchor=tk.W)
        record_table.heading('End Time', text='Start Time', anchor=tk.W)

        record_table.column('#0', anchor=tk.W, width=0, stretch=tk.NO)
        record_table.column('ID', anchor=tk.W, width=20)
        record_table.column('Course ID', anchor=tk.W, width=60)
        record_table.column('Course Name', anchor=tk.W, width=150)
        record_table.column('Subject Area', anchor=tk.W, width=150)
        record_table.column('Organization Name', anchor=tk.W, width=150)
        record_table.column('Start Date', anchor=tk.W, width=100)
        record_table.column('End Date', anchor=tk.W, width=100)
        record_table.column('Start Time', anchor=tk.W, width=100)
        record_table.column('End Time', anchor=tk.W, width=100)

        self.load_data(record_table)

        return head_frame

    def load_data(self, record_table):
        programs = self.model.select_all()
        for item in record_table.get_children():
            record_table.delete(item)

        for r in range(len(programs)):
            program_copy = list(programs[r]).copy()
            program_copy.pop(-2)
            program_copy[4], program_copy[-1] = program_copy[-1], program_copy[4]
            record_table.insert(parent='', index='end', text='',
                                iid=r, values=tuple(program_copy))

    def put_into_entries(self, record_table, course_id_entry, course_name_entry,
                        subject_area_entry, start_date_entry, end_date_entry,
                        start_time_entry, end_time_entry, op_menu_value):
        curItem = record_table.focus()
        values = record_table.item(curItem)['values']
        program_id = values[0]

        program = self.model.select_program_by_id(program_id)[0]
        print(program)

        course_id_entry.delete(0, tk.END)
        course_name_entry.delete(0, tk.END)
        subject_area_entry.delete(0, tk.END)
        start_date_entry.delete(0, tk.END)
        end_date_entry.delete(0, tk.END)
        start_time_entry.delete(0, tk.END)
        end_time_entry.delete(0, tk.END)

        course_id = program[1]
        course_name = program[2]
        sub_area = program[3]
        stat_date = program[4]
        end_date = program[5]
        start_time = program[6]
        end_time = program[7]
        org_name = program[-1]
        
        course_id_entry.insert(0, course_id)
        course_name_entry.insert(0, course_name)
        subject_area_entry.insert(0, sub_area)
        start_date_entry.insert(0, stat_date)
        end_date_entry.insert(0, end_date)
        start_time_entry.insert(0, start_time)
        end_time_entry.insert(0, end_time)
        op_menu_value.set(org_name)

    def clear_inputs(self, entries, org_option):
        for element in entries:
            element.delete(0, tk.END)
        org_option.set("Choose an organization")

    def add_program(self, record_table, elements, org_option):
        values = []
        organization_id = self.org_model.select_by_name(org_option.get())[0][0]

        for element in elements:
            values.append(element.get())

        values.append(organization_id)
        print(values)
        id = self.model.add_trainingProgram(tuple(values))
        self.clear_inputs(elements, org_option)
        self.load_data(record_table)

    def update_program(self, record_table, course_id_entry, course_name_entry, 
                        subject_area_entry, start_date_entry, end_date_entry,
                        start_time_entry, end_time_entry, op_menu_value):
        curItem = record_table.focus()
        program_id = record_table.item(curItem)['values'][0]
        organization_id = self.org_model.select_by_name(op_menu_value.get())[0][0]
        values = []
        values.append(course_id_entry.get())
        values.append(course_name_entry.get())
        values.append(subject_area_entry.get())
        values.append(start_date_entry.get())
        values.append(end_date_entry.get())
        values.append(start_time_entry.get())
        values.append(end_time_entry.get())
        values.append(organization_id)
        values.append(program_id)

        self.model.update_trainingProgram(tuple(values))

        self.load_data(record_table)
        self.clear_inputs([course_id_entry, course_name_entry, 
                        subject_area_entry, start_date_entry, end_date_entry,
                        start_time_entry, end_time_entry], op_menu_value)

    def delete_program(self, record_table, elements, op_menu_value):
        curItem = record_table.focus()
        values = record_table.item(curItem)['values']
        program_id = values[0]
        print(program_id)
        self.model.delete_trainingProgram(program_id)
        self.load_data(record_table)
        self.clear_inputs(elements, op_menu_value)

    def find_program_by_org(self, record_table, org_name):
        if org_name != "":
            programs = self.model.select_program_by_org_name(org_name)

            for item in record_table.get_children():
                record_table.delete(item)

            for r in range(len(programs)):
                program_copy = list(programs[r]).copy()
                program_copy.pop(-2)
                program_copy[4], program_copy[-1] = program_copy[-1], program_copy[4]
                record_table.insert(parent='', index='end', text='',
                                iid=r, values=tuple(program_copy))
        else:
            self.load_data(record_table)