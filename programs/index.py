import tkinter as tk
from tkinter import ttk
from programs.tpm import TrainingProgramModel
from organizations.om import OrganizationsModel
import programs.fonts
from timeconverter.converter import TimeConverter

class TrainingProgram(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.pack(side = "top", fill = "both", expand = True)
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)
        self.time_con = TimeConverter()
        self.parent_controller = parent
        self.model = TrainingProgramModel(r"" + parent.get_db_path())
        self.org_model = OrganizationsModel(r"" + parent.get_db_path())
        self.container = self.get_initial_frame(self)

    def get_initial_frame(self, parent_frame):
        time_types = [
        "AM",
        "PM",
        ]

        head_frame = tk.Frame(parent_frame)
        head_frame.grid(row = 0, column = 0)
        head_frame.grid_rowconfigure(0, weight = 1)
        head_frame.grid_columnconfigure(0, weight = 1)

        heading_lb = tk.Label(head_frame, text='Programs and Courses Registration System',
                     font=programs.fonts.main,
                     bg='pink')
        heading_lb.grid(row = 0, column = 0)

        menu_frame = tk.Frame(head_frame)
        menu_frame.grid(row = 1, column = 0)
        menu_frame.grid_rowconfigure(0, weight = 1)
        menu_frame.grid_columnconfigure(0, weight = 1)


        entries_frame = ttk.LabelFrame(menu_frame)
        entries_frame.grid(row = 1, column = 0, sticky="NSEW")

        entries_container = tk.Label(entries_frame)
        entries_container.grid(row = 0, column = 0, sticky="NSEW")

        course_id_lb = tk.Label(entries_container, text='Course ID:', font=programs.fonts.sub)
        course_id_lb.grid(row = 0, column = 0)
        course_id_entry = tk.Entry(entries_container, font=programs.fonts.sub)
        course_id_entry.grid(row = 0, column = 1, pady = 10)

        course_name_lb = tk.Label(entries_container, text='Course Name:', font=programs.fonts.sub)
        course_name_lb.grid(row = 1, column = 0)
        course_name_entry = tk.Entry(entries_container, font=programs.fonts.sub)
        course_name_entry.grid(row = 1, column = 1, pady = 10)

        subject_area_lb = tk.Label(entries_container, text='Subject Area:', font=programs.fonts.sub)
        subject_area_lb.grid(row = 2, column = 0)
        subject_area_entry = tk.Entry(entries_container, font=programs.fonts.sub)
        subject_area_entry.grid(row = 2, column = 1, pady = 10)


        # Drop down menu to choose an university or organization
        # --------------------------------------------------------------------------------    
        organizations = self.org_model.select_all()
        organizations_lb = tk.Label(entries_container, text='Organization:', font=programs.fonts.sub)
        organizations_lb.grid(row = 3, column = 0, pady = 10)
        options = [
        "Choose an organization",
        ]

        for organization in organizations:
            options.append(organization[1])

        op_menu_value = tk.StringVar()
        op_menu_value.set(options[0]) # default value
        tk.OptionMenu(entries_container, op_menu_value, *options).grid(row = 3, column = 1, pady = 10)
        # --------------------------------------------------------------------------------   


        start_date_lb = tk.Label(entries_container, text='Start Date:', font=programs.fonts.sub)
        start_date_lb.grid(row = 4, column = 0)
        start_date_entry = tk.Entry(entries_container, font=programs.fonts.sub)
        start_date_entry.grid(row = 4, column = 1, pady = 10)
        end_date_lb = tk.Label(entries_container, text='End Date:', font=programs.fonts.sub)
        end_date_lb.grid(row = 5, column = 0)
        end_date_entry = tk.Entry(entries_container, font=programs.fonts.sub)
        end_date_entry.grid(row = 5, column = 1, pady = 10)

        tk.Label(entries_container, text='Day:', font=programs.fonts.sub).grid(row = 6, column = 0, pady = 10)
        days = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
        ]
        day_choice = tk.StringVar()
        day_choice.set(days[0]) # default value
        tk.OptionMenu(entries_container, day_choice, *days).grid(row = 6, column = 1, pady = 10)


        start_time_lb = tk.Label(entries_container, text='Start Time(e.g 10:45):', font=programs.fonts.sub)
        start_time_lb.grid(row = 7, column = 0)
        start_time_entry = tk.Entry(entries_container, font=programs.fonts.sub)
        start_time_entry.grid(row = 7, column = 1, pady = 10)
        start_time_type = tk.StringVar()
        start_time_type.set(time_types[0]) # default value
        start_time_ops = tk.OptionMenu(entries_container, start_time_type, *time_types)
        start_time_ops.grid(row = 7, column = 2)

        end_time_lb = tk.Label(entries_container, text='End Time(e.g 11:45):', font=programs.fonts.sub)
        end_time_lb.grid(row = 8, column = 0)
        end_time_entry = tk.Entry(entries_container, font=programs.fonts.sub)
        end_time_entry.grid(row = 8, column = 1)
        end_time_type = tk.StringVar()
        end_time_type.set(time_types[0]) # default value
        end_time_ops = tk.OptionMenu(entries_container, end_time_type, *time_types)
        end_time_ops.grid(row = 8, column = 2)

        # #______________________________Buttons____________________________________________________
        buttons_frame = tk.Label(entries_frame)
        buttons_frame.grid(row = 9, column = 0, pady = 15)

        register_btn = tk.Button(buttons_frame, text='Register', font=programs.fonts.mid,
                                command=lambda: self.add_program(record_table, [course_id_entry, course_name_entry, 
                                                                subject_area_entry, start_date_entry, end_date_entry,
                                                                start_time_entry, end_time_entry],
                                                                day_choice,
                                                                [start_time_type, end_time_type], op_menu_value))
        register_btn.grid(row = 0, column = 0, padx = 10)

        tk.Button(buttons_frame, text='Update', font=programs.fonts.mid,
                command=lambda: self.update_program(record_table, course_id_entry, course_name_entry, 
                subject_area_entry, start_date_entry, end_date_entry, start_time_entry, end_time_entry,
                day_choice,
                start_time_type, end_time_type, op_menu_value)).grid(row = 0, column = 1)


        delete_btn = tk.Button(buttons_frame, text='Delete', font=programs.fonts.mid,
                            command=lambda: self.delete_program(record_table, [course_id_entry, course_name_entry, 
                                                                subject_area_entry, start_date_entry, end_date_entry,
                                                                start_time_entry, end_time_entry],
                                                                day_choice,
                                                                start_time_type, end_time_type, op_menu_value))
        delete_btn.grid(row = 0, column = 2, padx = 10)

        clear_btn = tk.Button(buttons_frame, text='Clear', font=programs.fonts.mid,
                            command=lambda: self.clear_inputs([course_id_entry, course_name_entry, 
                                                                subject_area_entry, start_date_entry, end_date_entry,
                                                                start_time_entry, end_time_entry],
                                                                day_choice,
                                                                start_time_type, end_time_type, op_menu_value)
                            )
        clear_btn.grid(row = 0, column = 3, padx = 10)

        back_btn = tk.Button(buttons_frame, text ="Back", font=programs.fonts.mid,
                            command = lambda : self.parent_controller.show_frame('StartPage'))
        back_btn.grid(row = 1, column = 3, pady = 5)
        # #________________________________Buttons____________________________________________________


        # # Search Section --------------------------------------------------------------------------

        search_frame = ttk.LabelFrame(menu_frame, text="Search")
        search_frame.grid(row = 1, column = 1, sticky="NSEW")

        search_time_lb = tk.Label(search_frame,
                            text='Search a course/program for a given time window',
                            font=programs.fonts.sub)
        search_time_lb.grid(row = 0, column = 0)
        time_search_container = tk.Label(search_frame)
        time_search_container.grid(row = 1, column = 0)
        search_from_lb = tk.Label(time_search_container, text='From (e.g 10:45):', font=programs.fonts.sub)
        search_from_lb.grid(row = 0, column = 0)
        # search_from_lb.place(x=0, y=20)
        search_start_time = tk.Entry(time_search_container, font=programs.fonts.sub)
        search_start_time.grid(row = 0, column = 1)

        from_meridiem = tk.StringVar()
        from_meridiem.set(time_types[0]) # default value
        from_ops = tk.OptionMenu(time_search_container, from_meridiem, *time_types)
        from_ops.grid(row =0, column = 2)
        search_start_time.bind('<KeyRelease>', lambda e: self.find_program_by_time(record_table, 
                                                                                    search_start_time.get(),
                                                                                    from_meridiem.get(),
                                                                                    search_end_time.get(),
                                                                                    to_meridiem.get()
                                                                                    ))

        search_to_lb = tk.Label(time_search_container, text='To (e.g 12:45):', font=programs.fonts.sub)
        search_to_lb.grid(row = 1, column = 0)
        search_end_time = tk.Entry(time_search_container, font=programs.fonts.sub)
        search_end_time.grid(row = 1, column = 1)
        to_meridiem = tk.StringVar()
        to_meridiem.set(time_types[1]) # default value
        to_ops = tk.OptionMenu(time_search_container, to_meridiem, *time_types)
        to_ops.grid(row = 1, column = 2)
        search_end_time.bind('<KeyRelease>', lambda e: self.find_program_by_time(record_table, 
                                                                                search_start_time.get(),
                                                                                from_meridiem.get(),
                                                                                search_end_time.get(),
                                                                                to_meridiem.get()
                                                                                ))

        tk.Label(search_frame, text='OR', font=('Bold', 15)).grid(row = 2, column = 0)
        search_org_lb = tk.Label(search_frame,
                            text='Search a course/program for a specified university or training organization',
                            font=programs.fonts.sub)
        search_org_lb.grid(row = 3, column = 0)
        search_by_org_entry = tk.Entry(search_frame, font=programs.fonts.sub)
        search_by_org_entry.grid(row = 4, column = 0)
        search_by_org_entry.bind('<KeyRelease>', lambda e: self.find_program_by_org(record_table, search_by_org_entry.get()))
        # Search Section End --------------------------------------------------------------------------

        tk.Label(head_frame,
                text= 'Select Record for Delete or Update',
                bg='pink', font=programs.fonts.main).grid(row = 2, column = 0, pady=25)

        record_frame = tk.Frame(head_frame)
        record_frame.grid(row = 3, column = 0, sticky="NSEW")

        record_table = ttk.Treeview(record_frame)
        record_table.grid(row = 0, column = 0, sticky="NSEW")
                            
        record_table.bind('<ButtonRelease-1>', lambda e: self.put_into_entries(record_table, course_id_entry, course_name_entry, 
                                                                            subject_area_entry, start_date_entry, end_date_entry,
                                                                            start_time_entry, end_time_entry, day_choice, 
                                                                            start_time_type, end_time_type, op_menu_value))

        record_table['column'] = ['ID', 'Course ID', 'Course Name', 'Subject Area', 'Organization Name', 
                                'Start Date', 'End Date', 'Day', 'Start Time', 'End Time']

        record_table.heading('ID', text='ID')
        record_table.heading('Course ID', text='Course ID')
        record_table.heading('Course Name', text='Course Name')
        record_table.heading('Subject Area', text='Subject Area')
        record_table.heading('Organization Name', text='Organization Name')
        record_table.heading('Day', text='Day')
        record_table.heading('Start Date', text='Start Date')
        record_table.heading('End Date', text='End Date')
        record_table.heading('Start Time', text='Start Time')
        record_table.heading('End Time', text='Start Time')

        record_table.column('#0', anchor=tk.W, width=0, stretch=tk.NO)
        record_table.column('ID', anchor=tk.W, width=20)
        record_table.column('Course ID', anchor=tk.W, width=60)
        record_table.column('Course Name', anchor="center")
        record_table.column('Subject Area', anchor="center")
        record_table.column('Organization Name', anchor="center")
        record_table.column('Day', anchor="center", width=110)
        record_table.column('Start Date', anchor="center")
        record_table.column('End Date', anchor="center")
        record_table.column('Start Time', anchor="center", width=90)
        record_table.column('End Time', anchor="center", width=90)

        self.load_data(record_table)

        return head_frame

    def load_data(self, record_table):
        programs = self.model.select_all()
        self.populate_record_table(record_table, programs)

    def put_into_entries(self, record_table, course_id_entry, course_name_entry,
                        subject_area_entry, start_date_entry, end_date_entry,
                        start_time_entry, end_time_entry, day,
                        start_time_type, end_time_type, op_menu_value):
        curItem = record_table.focus()
        values = record_table.item(curItem)['values']
        program_id = values[0]

        program = self.model.select_program_by_id(program_id)[0]

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
        stat_date = self.time_con.unixtimestamp_to_date(program[4])
        end_date = self.time_con.unixtimestamp_to_date(program[5])
        day_value = program[6]
        start_time = self.time_con.format_humanreadable(program[7], False)
        start_t_type = program[8]
        end_time = self.time_con.format_humanreadable(program[9], False)
        end_t_type = program[10]
        org_name = program[-1]

        course_id_entry.insert(0, course_id)
        course_name_entry.insert(0, course_name)
        subject_area_entry.insert(0, sub_area)
        start_date_entry.insert(0, stat_date)
        end_date_entry.insert(0, end_date)
        start_time_entry.insert(0, start_time)
        day.set(day_value)
        start_time_type.set(start_t_type)
        end_time_entry.insert(0, end_time)
        end_time_type.set(end_t_type)
        op_menu_value.set(org_name)

    def clear_inputs(self, entries, day, start_time_type, end_time_type, org_option):
        for element in entries:
            element.delete(0, tk.END)
        day.set("Monday")
        start_time_type.set("AM")
        end_time_type.set('AM')
        org_option.set("Choose an organization")

    def add_program(self, record_table, elements, day, time_types, org_option):
        values = []
        organization_id = self.org_model.select_by_name(org_option.get())[0][0]

        start_date = self.time_con.date_to_unixtimestamp(elements[3].get())
        end_date = self.time_con.date_to_unixtimestamp(elements[4].get())
        start_time = self.time_con.format_unixtimestamp(elements[5].get(), time_types[0].get())
        end_time = self.time_con.format_unixtimestamp(elements[6].get(), time_types[1].get())

        values.append(elements[0].get())
        values.append(elements[1].get())
        values.append(elements[2].get())
        values.append(start_date)
        values.append(end_date)
        values.append(day.get())
        values.append(start_time)
        values.append(time_types[0].get())
        values.append(end_time)
        values.append(time_types[1].get())
        values.append(organization_id)
        print(values)

        id = self.model.add_trainingProgram(tuple(values))
        self.clear_inputs(elements, day, time_types[0], time_types[1], org_option)
        self.load_data(record_table)

    def update_program(self, record_table, course_id_entry, course_name_entry, 
                        subject_area_entry, start_date_entry, end_date_entry,
                        start_time_entry, end_time_entry,
                        day,
                        start_time_type, end_time_type, op_menu_value):
        cur_item = record_table.focus()
        program_id = record_table.item(cur_item)['values'][0]
        organization_id = self.org_model.select_by_name(op_menu_value.get())[0][0]
        start_date = self.time_con.date_to_unixtimestamp(start_date_entry.get())
        end_date = self.time_con.date_to_unixtimestamp(end_date_entry.get())
        start_time = self.time_con.format_unixtimestamp(start_time_entry.get(), start_time_type.get())
        end_time = self.time_con.format_unixtimestamp(end_time_entry.get(), end_time_type.get())
        values = []
        values.append(course_id_entry.get())
        values.append(course_name_entry.get())
        values.append(subject_area_entry.get())
        values.append(start_date)
        values.append(end_date)
        values.append(day.get())
        values.append(start_time)
        values.append(start_time_type.get())
        values.append(end_time)
        values.append(end_time_type.get())
        values.append(organization_id)
        values.append(program_id)

        self.model.update_trainingProgram(tuple(values))

        self.load_data(record_table)
        self.clear_inputs([course_id_entry, course_name_entry, 
                        subject_area_entry, start_date_entry, end_date_entry,
                        start_time_entry, end_time_entry], day,
                        start_time_type, end_time_type, op_menu_value)

    def delete_program(self, record_table, elements, day, start_time_type, end_time_type, op_menu_value):
        cur_item = record_table.focus()
        values = record_table.item(cur_item)['values']
        program_id = values[0]
        print(program_id)
        self.model.delete_trainingProgram(program_id)
        self.load_data(record_table)
        self.clear_inputs(elements, day, start_time_type, end_time_type, op_menu_value)

    def populate_record_table(self, record_table, programs):
        for item in record_table.get_children():
            record_table.delete(item)

        for r in range(len(programs)):
            program_copy = list(programs[r]).copy()
            program_copy.pop(-1) # remove end time type
            program_copy.pop(-2) # remove start time type
            print(program_copy)
            start_day = self.time_con.unixtimestamp_to_date(program_copy[-5]) # start date
            end_day = self.time_con.unixtimestamp_to_date(program_copy[-4]) # end date
            start_time = self.time_con.format_humanreadable(program_copy[-2]) # start time
            end_time = self.time_con.format_humanreadable(program_copy[-1]) #end time
            program_copy[-5] = start_day
            program_copy[-4] = end_day
            program_copy[-2] = start_time
            program_copy[-1] = end_time
            record_table.insert(parent='', index='end', text='',
                                iid=r, values=tuple(program_copy))

    def find_program_by_org(self, record_table, org_name):
        if org_name != "":
            programs = self.model.select_program_by_org_name(org_name)
            self.populate_record_table(record_table, programs)
        else:
            self.load_data(record_table)

    def find_program_by_time(self, record_table, start_time, start_type, end_time, end_type):
        if len(start_time) > 4 or len(end_time) > 4:
            start_formatted = self.time_con.format_unixtimestamp('08:00', 'AM') # 08:00AM - minimum starting time
            end_formatted = self.time_con.format_unixtimestamp('09:00', 'PM') # 09:00PM - maximum ending time
            if len(start_time) > 4: # use passed start time if entered fully - e.x. 10:45,
                start_formatted = self.time_con.format_unixtimestamp(start_time, start_type)
            if len(end_time) > 4: # use passed end time if entered fully - e.x. 10:45,
                end_formatted = self.time_con.format_unixtimestamp(end_time, end_type)
            programs = self.model.select_program_by_time(start_formatted, end_formatted)
            self.populate_record_table(record_table, programs)
        else:
            self.load_data(record_table)