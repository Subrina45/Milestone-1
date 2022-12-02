from datetime import datetime
from time import mktime
import tkinter as tk
from tkinter import ttk
import mentorPreference.fonts
from programs.tpm import TrainingProgramModel


class MentorDashboard(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.pack(side = "top", fill = "both", expand = True)
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)
        self.parent_controller = parent
        self.program_model = TrainingProgramModel(r"" + parent.get_db_path())
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

        # Section to enter the last day of a course -------------------------------------------------------
        date_range_lb =  tk.Label(search_frame, text='Enter the last day of a course (mm/dd/yyyy):', font=mentorPreference.fonts.sub)
        date_range_lb.grid(row = search_frame_row, column = 0)
        date_range_entry = tk.Entry(search_frame, font=mentorPreference.fonts.sub)
        date_range_entry.grid(row = search_frame_row, column = 1, pady=10)
        search_frame_row += 1
        # the last day of a course ---------------------------------------------------------------------------------------

        time_settings = dict()
        time_settings['start_time'] = start_time_entry.get()
        time_settings['start_type'] = from_meridiem.get()
        time_settings['end_time'] = end_time_entry.get()
        time_settings['end_type'] = to_meridiem.get()
        time_settings['end_date'] = date_range_entry.get()
        submit_btn_label = tk.Label(search_frame)
        submit_btn_label.grid(row = 10, column = 0)
        search_button = tk.Button(submit_btn_label,
                                text='Search', font=mentorPreference.fonts.sub,
                                command=lambda: self.search_courses(record_table,
                                                                    time_settings,
                                                                    self.parent_controller.get_credentials()
                                                                    )
                                )
        search_button.grid(row = 0, column = 0)
        ## SEARCH Section End --------------------------------------------------------------------------

        ## SEARCH RESULT section start -------------------------------------
        tk.Label(head_frame,
                text= 'Select which course(s) you wish to mentor',
                bg='pink',
                font=mentorPreference.fonts.main).grid(row = 2, column = 0, pady=25)

        record_frame = tk.Frame(head_frame)
        record_frame.grid(row = 3, column = 0, sticky="NSEW")

        record_table = ttk.Treeview(record_frame)
        record_table.grid(row = 0, column = 0, sticky="NSEW")
                            
        ##delete this code.   START
        # no data for first load. 
        # record_table.bind('<ButtonRelease-1>', lambda e: self.put_into_entries(record_table, course_id_entry, course_name_entry, 
        #                                                                     subject_area_entry, organizations_entry, start_date_entry, end_date_entry,
        #                                                                     start_time_entry, end_time_entry, day_choice_entry, 
        #                                                                     start_time_type, end_time_type))
        ##delete this code.   END

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

        return head_frame

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

    def add(self, record_table, mentor_id, elements, day, time_types, org_option):
        """
            add function
        """
        print(mentor_id)
        # add code here to register chosen course
        # please edit/change arguments according to the new table's structure

    def format_unixtimestamp(self, time, time_type):
        dt = datetime.strptime(time + ' ' + time_type, "%I:%M %p")
        dt = dt.replace(1970, 1, 1)
        return int(mktime(dt.timetuple()))

    def format_humanreadable(self, timestamp, include_type = True):
        return datetime.fromtimestamp(int(timestamp)).strftime('%I:%M %p' if include_type else '%I:%M')

    def populate_record_table(self, record_table, programs):
        for item in record_table.get_children():
            record_table.delete(item)

        for r in range(len(programs)):
            program_copy = list(programs[r]).copy()
            program_copy.pop(-1) # remove end time type
            program_copy.pop(-2) # remove start time type
            start_time = self.format_humanreadable(program_copy[-2])
            end_time = self.format_humanreadable(program_copy[-1])
            program_copy[-2] = start_time
            program_copy[-1] = end_time
            record_table.insert(parent='', index='end', text='',
                                iid=r, values=tuple(program_copy))
    
    def search_courses(self, record_table, time_info, mentor_info):
        # following are the values passed to this function from search fields
        print('time_info', time_info)
        print(mentor_info)

        if len(start_time) > 4 or len(end_time) > 4:
            start_formatted = self.format_unixtimestamp('08:00', 'AM') # 08:00AM - minimum starting time
            end_formatted = self.format_unixtimestamp('09:00', 'PM') # 09:00PM - maximum ending time
            if len(start_time) > 4: # use passed start time if entered fully - e.x. 10:45,
                start_formatted = self.format_unixtimestamp(start_time, start_type)
            if len(end_time) > 4: # use passed end time if entered fully - e.x. 10:45,
                end_formatted = self.format_unixtimestamp(end_time, end_type)

            #add code here for search query  
            # programs = self.model.select_program_by_time(start_formatted, end_formatted)      
        else:
            # display no records
            self.populate_record_table(record_table, [])

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