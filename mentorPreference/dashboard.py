import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from programs.tpm import TrainingProgramModel
from mentorPreference.model import MentorPreferenceModel
import mentorPreference.fonts
from timeconverter.converter import TimeConverter

class MentorDashboard(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.pack(side = "top", fill = "both", expand = True)
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)
        self.parent_controller = parent
        self.time_con = TimeConverter()
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

        heading_lb = tk.Label(head_frame, text='Mentor Preference & Availability',
                     font=mentorPreference.fonts.main,
                     bg='pink')
        heading_lb.grid(row = 0, column = 0)

        menu_frame = tk.Label(head_frame)
        menu_frame.grid(row = 1, column = 0)

        ## SEARCH section start ------------------------------------------------------------------
        search_frame = ttk.LabelFrame(menu_frame, text="Search for courses")
        search_frame.grid(row = 0, column = 0, sticky="NSEW")
        search_frame_row = 0

        tk.Label(search_frame, text='Choose course days', font=mentorPreference.fonts.sub).grid(row = search_frame_row, column = 0, sticky="W")
        search_frame_row += 1
        
        # Days selection -------------------------------------------------------------------------------------
        days_container = tk.Label(search_frame)
        days_container.grid(row = search_frame_row, column = 0)
        search_frame_row += 1

        day_list = []
        var1 = tk.IntVar()
        search_chec_1 = tk.Checkbutton(days_container, text="Mon", variable=var1, command=lambda: self.addToDaysList(var1, "Monday", day_list))
        search_chec_1.grid(row=0, column = 0, sticky="W")

        var2 = tk.IntVar()        
        search_chec_2 = tk.Checkbutton(days_container, text="Tue", variable=var2, command=lambda: self.addToDaysList(var2, "Tuesday", day_list))
        search_chec_2.grid(row=0, column = 1, sticky="W")

        var3 = tk.IntVar()
        search_chec_3 = tk.Checkbutton(days_container, text="Wed", variable=var3, command=lambda: self.addToDaysList(var3, "Wednesday", day_list))
        search_chec_3.grid(row=0, column = 2, sticky="W")

        var4 = tk.IntVar()
        search_chec_4 = tk.Checkbutton(days_container, text="Thu", variable=var4, command=lambda: self.addToDaysList(var4, "Thursday", day_list))
        search_chec_4.grid(row=0, column = 3, sticky="W")
        
        var5 = tk.IntVar()
        search_chec_5 = tk.Checkbutton(days_container, text="Fri", variable=var5, command=lambda: self.addToDaysList(var5, "Friday", day_list))
        search_chec_5.grid(row=0, column = 4, sticky="W")
        # Days selection end----------------------------------------------------------------------------------------

        # Section to enter starting time of a course -------------------------------------------------------
        search_from_lb = tk.Label(search_frame, text='From (e.g 10:45):', font=mentorPreference.fonts.sub)
        search_from_lb.grid(row = search_frame_row, column = 0, pady=10)

        start_time_entry = tk.Entry(search_frame, font=mentorPreference.fonts.sub)
        start_time_entry.grid(row = search_frame_row, column = 1)

        from_meridiem = tk.StringVar()
        from_meridiem.set(time_types[0]) # set 'AM' by default 
        from_ops = tk.OptionMenu(search_frame, from_meridiem, *time_types)
        from_ops.grid(row=search_frame_row, column=2, padx=5)
        search_frame_row += 1
        # starting time of a course-------------------------------------------------------

        # Section to enter ending time of a course -------------------------------------------------------
        time_to_lb = tk.Label(search_frame, text='To (e.g 12:45):', font=mentorPreference.fonts.sub)
        time_to_lb.grid(row = search_frame_row, column = 0)

        end_time_entry = tk.Entry(search_frame, font=mentorPreference.fonts.sub)
        end_time_entry.grid(row = search_frame_row, column = 1)

        to_meridiem = tk.StringVar()
        to_meridiem.set(time_types[1]) # set 'PM' by default 
        to_ops = tk.OptionMenu(search_frame, to_meridiem, *time_types)
        to_ops.grid(row = search_frame_row, column=2, padx=5)
        search_frame_row += 1
        # ending time of a course----------------------------------------------------------------------------------------

        # Section to enter the first day of a course -------------------------------------------------------
        tk.Label(search_frame,
                text='Enter the first day of a course (mm/dd/yyyy):',
                font=mentorPreference.fonts.sub).grid(row = search_frame_row, column = 0)
        start_date = tk.Entry(search_frame, font=mentorPreference.fonts.sub)
        start_date.grid(row = search_frame_row, column = 1, pady=10)
        search_frame_row += 1
        # the first day of a course ---------------------------------------------------------------------------------------

        # Section to enter the last day of a course -------------------------------------------------------
        tk.Label(search_frame,
                text='Enter the last day of a course (mm/dd/yyyy):',
                font=mentorPreference.fonts.sub).grid(row = search_frame_row, column = 0)
        end_date = tk.Entry(search_frame, font=mentorPreference.fonts.sub)
        end_date.grid(row = search_frame_row, column = 1, pady=10)
        search_frame_row += 1
        # the last day of a course ---------------------------------------------------------------------------------------

        # search button section ---------------------------------------
        search_btn_lb = tk.Label(search_frame)
        search_btn_lb.grid(row = 10, column = 0)
        search_button = tk.Button(search_btn_lb,
                                text='Search', font=mentorPreference.fonts.sub,
                                command=lambda: self.search_for_courses(record_table,
                                                                        {
                                                                            'selected_days': day_list,
                                                                            'start_time': start_time_entry.get(),
                                                                            'start_type': from_meridiem.get(),
                                                                            'end_time': end_time_entry.get(),
                                                                            'end_type': to_meridiem.get(),
                                                                            'start_date': start_date.get(),
                                                                            'end_date': end_date.get()
                                                                        },
                                                                        self.parent_controller.get_credentials()[-2] # mentor's subject area
                                                                        ))
        search_button.grid(row = 0, column = 0)
        #end of search button section ---------------------------------------
        ## SEARCH Section End --------------------------------------------------------------------------

        ## TABLE FOR SEARCH RESULTS start -------------------------------------
        tk.Label(head_frame,
                text= 'Select which course(s) you wish to mentor',
                bg='pink',
                font=mentorPreference.fonts.main).grid(row = 2, column = 0, pady=25)

        record_frame = tk.Frame(head_frame)
        record_frame.grid(row = 3, column = 0, sticky="NSEW")

        record_table = ttk.Treeview(record_frame,
                                    columns=['ID', 'Course ID', 'Course Name', 'Subject Area', 'Organization Name', 
                                            'Start Date', 'End Date', 'Day', 'Start Time', 'End Time'])
        table_style = ttk.Style(record_table)
        table_style.configure('TreeView', rowheight=1)
        record_table.grid(row = 0, column = 0, sticky="NSEW")

        record_table.heading('#0', text='Select')
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

        record_table.column('#0', anchor="center", width=110)
        record_table.column('ID', anchor="center", width=40)
        record_table.column('Course ID', anchor="center", width=60)
        record_table.column('Course Name', anchor="center")
        record_table.column('Subject Area', anchor="center")
        record_table.column('Organization Name', anchor="center")
        record_table.column('Day', anchor="center", width=110)
        record_table.column('Start Date', anchor="center", width=110)
        record_table.column('End Date', anchor="center", width=110)
        record_table.column('Start Time', anchor="center", width=90)
        record_table.column('End Time', anchor="center", width=90)

        selected_course_ids = []
        record_table.bind('<ButtonRelease-1>', lambda e: self.handle_click(e, record_table, selected_course_ids))
        ## TABLE FOR SEARCH RESULTS end--------------------------------------------------------------

        submit_selection_lb = tk.Label(head_frame)
        submit_selection_lb.grid(row = 4, column = 0)
        submit_btn = tk.Button(submit_selection_lb,
                                text='Submit',
                                font=mentorPreference.fonts.sub,
                                command=lambda: self.submit_selections(selected_course_ids,
                                                                        self.parent_controller.get_credentials()[0]))
        submit_btn.grid(row = 1, column = 0)

        return head_frame
        # end of construct_frame method ---------

    def clear_inputs(self, entries, start_time_type, end_time_type):
        for element in entries:
            element.config(state= "normal")
            element.delete(0, tk.END)
        # day.set("Monday")
        start_time_type.set("AM")
        end_time_type.set('AM')
        # org_option.set("Choose an organization")

        for element in entries:
            element.config(state= "disable")

    def populate_record_table(self, record_table, programs):
        for item in record_table.get_children():
            record_table.delete(item)

        for r in range(len(programs)):
            program_copy = list(programs[r]).copy()
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
            record_table.insert(parent='', index='end',
                                iid=r, values=tuple(program_copy), image=self.im_unchecked, tags="unchecked")

    def search_for_courses(self, record_table, time_info, subject_area):
        selected_days = time_info['selected_days']
        start_date = time_info['start_date'].strip()
        end_date = time_info['end_date'].strip()
        start_time = time_info['start_time']
        end_time = time_info['end_time']
        start_type = time_info['start_type']
        end_type = time_info['end_type']

        # if a date or time is invalid, use a default value or ignore it
        courses = [] # by default found courses are empty
        if len(start_time) == 5 or len(end_time) == 5:
            start_formatted = self.time_con.format_unixtimestamp('08:00', 'AM') # 08:00AM - minimum starting time
            end_formatted = self.time_con.format_unixtimestamp('09:00', 'PM') # 09:00PM - maximum ending time
            if len(start_time) == 5: # use passed start time if entered fully - e.x. 10:45,
                start_formatted = self.time_con.format_unixtimestamp(start_time, start_type)
            if len(end_time) == 5: # use passed end time if entered fully - e.x. 10:45,
                end_formatted = self.time_con.format_unixtimestamp(end_time, end_type)
            if len(start_date) == 10: # mm/dd/yyyy <--- has ten characters
                start_date = str(self.time_con.date_to_unixtimestamp(start_date))
            else: #if not ten characters, assign an empty str
                start_date = ''
            if len(end_date) == 10: # mm/dd/yyyy <--- has ten characters
                end_date = str(self.time_con.date_to_unixtimestamp(end_date))
            else: #if not ten characters, assign an empty str
                end_date = ''

            # get matched courses from the db
            courses = self.program_model.select_by_time_sub_area({'selected_days': selected_days,
                                                                'start_date': start_date,
                                                                'end_date': end_date,
                                                                'start_time': start_formatted,
                                                                'end_time': end_formatted}
                                                                ,subject_area)
        # populate the record table with the courses
        self.populate_record_table(record_table, courses)

    def addToDaysList(self, cbox_state, value, day_list):
        """ add/remove value to a list of days
        """
        if(cbox_state.get() == 1): # checkbox is checked
            if value in day_list:
                #do nothing, already added
                print("exists")
            else:
                day_list.append(value)
        elif(cbox_state.get() == 0): # checkbox is not checked
            if value in day_list:
                day_list.remove(value)

    def handle_click(self, event, record_table, selected_course_ids):
        cur_row = record_table.identify_row(event.y)
        self.toggle_row_tag(record_table, cur_row)
        values = record_table.item(cur_row)['values']
        course_id = values[0]
        self.toggle_selected_course_ids(course_id, selected_course_ids)

    def toggle_selected_course_ids(self, course_id, courses):
        if course_id in courses: courses.remove(course_id)
        else: courses.append(course_id)

    def toggle_row_tag(self, record_table, row):
        row_tag = record_table.item(row, "tags")[0]
        if row_tag == 'checked':
            record_table.item(row, tags='unchecked')
            record_table.item(row, image=self.im_unchecked)
        else:
            record_table.item(row, tags='checked')
            record_table.item(row, image=self.im_checked)

    def submit_selections(self, course_ids, mentor_id):
        self.mentor_prf_model.add(course_ids, mentor_id)