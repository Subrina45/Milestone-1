from datetime import datetime
from time import mktime
import tkinter as tk
from tkinter import ttk
import mentorPreference.fonts
from programs.index import TrainingProgram
from programs.tpm import TrainingProgramModel


class MentorDashboard(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.pack(side = "top", fill = "both", expand = True)
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)
        self.parent_controller = parent
        self.program_model = TrainingProgramModel(r"" + parent.get_db_path())
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

        heading_lb = tk.Label(head_frame, text='Mentor Preference & Availability',
                     font=mentorPreference.fonts.main,
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

        course_id_lb = tk.Label(entries_container, text='Course ID:', font=mentorPreference.fonts.sub)
        course_id_lb.grid(row = 0, column = 0)
        course_id_entry = tk.Entry(entries_container, font=mentorPreference.fonts.sub)
        course_id_entry.grid(row = 0, column = 1, pady = 10)
        course_id_entry.config(state= "disabled")

        course_name_lb = tk.Label(entries_container, text='Course Name:', font=mentorPreference.fonts.sub)
        course_name_lb.grid(row = 1, column = 0)
        course_name_entry = tk.Entry(entries_container, font=mentorPreference.fonts.sub)
        course_name_entry.grid(row = 1, column = 1, pady = 10)
        course_name_entry.config(state= "disabled")
        

        subject_area_lb = tk.Label(entries_container, text='Subject Area:', font=mentorPreference.fonts.sub)
        subject_area_lb.grid(row = 2, column = 0)
        subject_area_entry = tk.Entry(entries_container, font=mentorPreference.fonts.sub)
        subject_area_entry.grid(row = 2, column = 1, pady = 10)
        subject_area_entry.config(state= "disabled")

        organizations_lb = tk.Label(entries_container, text='Organization:', font=mentorPreference.fonts.sub)
        organizations_lb.grid(row = 2, column = 0)
        organizations_entry = tk.Entry(entries_container, font=mentorPreference.fonts.sub)
        organizations_entry.grid(row = 2, column = 1, pady = 10)
        organizations_entry.config(state= "disabled")

        start_date_lb = tk.Label(entries_container, text='Start Date:', font=mentorPreference.fonts.sub)
        start_date_lb.grid(row = 4, column = 0)
        start_date_entry = tk.Entry(entries_container, font=mentorPreference.fonts.sub)
        start_date_entry.grid(row = 4, column = 1, pady = 10)
        start_date_entry.config(state= "disabled")

        end_date_lb = tk.Label(entries_container, text='End Date:', font=mentorPreference.fonts.sub)
        end_date_lb.grid(row = 5, column = 0)
        end_date_entry = tk.Entry(entries_container, font=mentorPreference.fonts.sub)
        end_date_entry.grid(row = 5, column = 1, pady = 10)
        end_date_entry.config(state= "disabled")


        day_choice = tk.Label(entries_container, text='Day:', font=mentorPreference.fonts.sub)
        day_choice.grid(row = 6, column = 0)
        day_choice_entry = tk.Entry(entries_container, font=mentorPreference.fonts.sub)
        day_choice_entry.grid(row = 6, column = 1, pady = 10)
        day_choice_entry.config(state= "disabled")

        start_time_lb = tk.Label(entries_container, text='Start Time(e.g 10:45):', font=mentorPreference.fonts.sub)
        start_time_lb.grid(row = 7, column = 0)
        start_time_entry = tk.Entry(entries_container, font=mentorPreference.fonts.sub)
        start_time_entry.grid(row = 7, column = 1, pady = 10)
        start_time_entry.config(state= "disabled")

        start_time_type = tk.StringVar()
        start_time_type.set(time_types[0]) # default value
        start_time_ops = tk.OptionMenu(entries_container, start_time_type, *time_types)
        start_time_ops.grid(row = 7, column = 2)
        start_time_ops.config(state= "disabled")

        end_time_lb = tk.Label(entries_container, text='End Time(e.g 11:45):', font=mentorPreference.fonts.sub)
        end_time_lb.grid(row = 8, column = 0)
        end_time_entry = tk.Entry(entries_container, font=mentorPreference.fonts.sub)
        end_time_entry.grid(row = 8, column = 1)
        end_time_entry.config(state= "disabled")

        end_time_type = tk.StringVar()
        end_time_type.set(time_types[0]) # default value
        end_time_ops = tk.OptionMenu(entries_container, end_time_type, *time_types)
        end_time_ops.grid(row = 8, column = 2)
        end_time_ops.config(state= "disabled")

        # #______________________________Buttons____________________________________________________
        buttons_frame = tk.Label(entries_frame)
        buttons_frame.grid(row = 9, column = 0, pady = 15)

        #change add's argument
        register_btn = tk.Button(buttons_frame, text='Register', font=mentorPreference.fonts.mid,
                                command=lambda: self.add(record_table, op_menu_value.get(), [course_id_entry, course_name_entry, 
                                                                subject_area_entry, start_date_entry, end_date_entry,
                                                                start_time_entry, end_time_entry],
                                                                day_choice_entry,
                                                                [start_time_type, end_time_type], op_menu_value))
        register_btn.grid(row = 0, column = 0, padx = 10)

        clear_btn = tk.Button(buttons_frame, text='Clear', font=mentorPreference.fonts.mid,
                            command=lambda: self.clear_inputs([course_id_entry, course_name_entry, 
                                                                subject_area_entry, organizations_entry, day_choice_entry, start_date_entry, end_date_entry,
                                                                start_time_entry, end_time_entry],
                                                                start_time_type, end_time_type)
                            )
        clear_btn.grid(row = 0, column = 3, padx = 10)

        back_btn = tk.Button(buttons_frame, text ="Back", font=mentorPreference.fonts.mid,
                            command = lambda : self.parent_controller.show_frame('StartPage'))
        back_btn.grid(row = 1, column = 3, pady = 5)
        # #________________________________Buttons____________________________________________________


        # # Search Section --------------------------------------------------------------------------

        search_frame = ttk.LabelFrame(menu_frame, text="Search")
        search_frame.grid(row = 1, column = 1, sticky="NSEW")

        time_search_container = tk.Label(search_frame)
        time_search_container.grid(row = 7, column = 0)

        mentors = self.mentor_model.select_all() #change select all query
        mentors_lb = tk.Label(search_frame, text='Select Mentor ID:', font=mentorPreference.fonts.sub)
        mentors_lb.grid(row = 0, column = 0, sticky="w")
        options = [
        "Choose a Mentor",
        ]

        for mentor in mentors:
            options.append(mentor[1] + " " + mentor[2] )

        op_menu_value = tk.StringVar()
        op_menu_value.set(options[0]) # default value
        tk.OptionMenu(search_frame, op_menu_value, *options).grid(row = 0)

        error_message_no_mentor = tk.Label(search_frame, text='', fg='red')
        error_message_no_mentor.grid(row = 1, column = 0)
        
        search_subj_lb = tk.Label(search_frame,
                            text='Search a Subject area',
                            font=mentorPreference.fonts.sub)
        search_subj_lb.grid(row = 2, column = 0)
        search_by_subj_entry = tk.Entry(search_frame, font=mentorPreference.fonts.sub)
        search_by_subj_entry.grid(row = 3, column = 0, sticky="w")
        # search_by_subj_entry.bind('<KeyRelease>', lambda e: self.find_program_by_org(record_table, search_by_subj_entry.get()))

        tk.Label(search_frame, text='', font=('Bold', 15)).grid(row = 3, column = 0)
        search_time_lb = tk.Label(search_frame,
                            text='Search a course/program for a given time window',
                            font=mentorPreference.fonts.sub)
        search_time_lb.grid(row = 4, column = 0, sticky="w")

        day_list = []
        var1 = tk.IntVar()
        search_chec_1 = tk.Checkbutton(time_search_container, text="Mon", variable=var1, command=lambda: self.getCheckboxValue(var1, "Monday", day_list))
        search_chec_1.grid(row=5, column = 0, sticky="w")

        var2 = tk.IntVar()        
        search_chec_2 = tk.Checkbutton(time_search_container, text="Tue", variable=var2, command=lambda: self.getCheckboxValue(var2, "Tuesday", day_list))
        search_chec_2.grid(row=5, column = 1, sticky="w")

        var3 = tk.IntVar()
        search_chec_3 = tk.Checkbutton(time_search_container, text="Wed", variable=var3, command=lambda: self.getCheckboxValue(var3, "Wednesday", day_list))
        search_chec_3.grid(row=5, column = 2, sticky="w")

        var4 = tk.IntVar()
        search_chec_4 = tk.Checkbutton(time_search_container, text="Thu", variable=var4, command=lambda: self.getCheckboxValue(var4, "Thursday", day_list))
        search_chec_4.grid(row=5, column = 3, sticky="w")
        
        var5 = tk.IntVar()
        search_chec_5 = tk.Checkbutton(time_search_container, text="Fri", variable=var5, command=lambda: self.getCheckboxValue(var5, "Friday", day_list))
        search_chec_5.grid(row=5, column = 4, sticky="w")

        tk.Label(time_search_container, text='').grid(row = 6, column = 0)

        search_from_lb = tk.Label(time_search_container, text='From (e.g 10:45):', font=mentorPreference.fonts.sub)
        search_from_lb.grid(row = 7, column = 0)

        search_start_time = tk.Entry(time_search_container, font=mentorPreference.fonts.sub)
        search_start_time.grid(row = 7, column = 1)

        from_meridiem = tk.StringVar()
        from_meridiem.set(time_types[0]) # default value
        from_ops = tk.OptionMenu(time_search_container, from_meridiem, *time_types)
        from_ops.grid(row =7, column = 2)

        search_to_lb = tk.Label(time_search_container, text='To (e.g 12:45):', font=mentorPreference.fonts.sub)
        search_to_lb.grid(row = 8, column = 0)
        search_end_time = tk.Entry(time_search_container, font=mentorPreference.fonts.sub)
        search_end_time.grid(row = 8, column = 1)
        to_meridiem = tk.StringVar()
        to_meridiem.set(time_types[1]) # default value
        to_ops = tk.OptionMenu(time_search_container, to_meridiem, *time_types)
        to_ops.grid(row = 8, column = 2)

        search_button = tk.Button(time_search_container, text='Search', font=mentorPreference.fonts.sub, command=lambda: self.findSearch(
                                                                                record_table, 
                                                                                op_menu_value.get(),
                                                                                search_start_time.get(),
                                                                                from_meridiem.get(),
                                                                                search_end_time.get(),
                                                                                to_meridiem.get(),
                                                                                search_by_subj_entry.get(),
                                                                                day_list,
                                                                                error_message_no_mentor
                                                                                ))
        search_button.grid(row = 9, column = 4)

        # Search Section End --------------------------------------------------------------------------

        tk.Label(head_frame,
                text= 'Select a Course you wish to mentor',
                bg='pink', font=mentorPreference.fonts.main).grid(row = 2, column = 0, pady=25)

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

        self.load_data(record_table)

        return head_frame

    def load_data(self, record_table):
        programs = self.model.select_all()
        self.populate_record_table(record_table, programs)

    def put_into_entries(self, record_table, course_id_entry, course_name_entry,
                        subject_area_entry, organizations_entry, start_date_entry, end_date_entry,
                        start_time_entry, end_time_entry, 
                        day,
                        start_time_type, end_time_type):
        curItem = record_table.focus()
        values = record_table.item(curItem)['values']
        program_id = values[0]

        program = self.model.select_program_by_id(program_id)[0]
        print('put_into_entries', program)

        # set fields' state to normal to set values
        course_id_entry.config(state= "normal")
        course_name_entry.config(state= "normal")
        subject_area_entry.config(state= "normal")
        organizations_entry.config(state= "normal")
        day.config(state= "normal")
        start_date_entry.config(state= "normal")
        end_date_entry.config(state= "normal")
        start_time_entry.config(state= "normal")
        end_time_entry.config(state= "normal")

        course_id_entry.delete(0, tk.END)
        course_name_entry.delete(0, tk.END)
        subject_area_entry.delete(0, tk.END)
        organizations_entry.delete(0, tk.END)
        start_date_entry.delete(0, tk.END)
        end_date_entry.delete(0, tk.END)
        start_time_entry.delete(0, tk.END)
        end_time_entry.delete(0, tk.END)

        course_id = program[1]
        course_name = program[2]
        sub_area = program[3]
        stat_date = program[4]
        end_date = program[5]
        day_value = program[6]
        start_time = self.format_humanreadable(program[7], False)
        start_t_type = program[8]
        end_time = self.format_humanreadable(program[9], False)
        end_t_type = program[10]
        org_name = program[-1]

        course_id_entry.insert(0, course_id)
        course_name_entry.insert(0, course_name)
        subject_area_entry.insert(0, sub_area)
        organizations_entry.insert(0, org_name)
        start_date_entry.insert(0, stat_date)
        end_date_entry.insert(0, end_date)
        start_time_entry.insert(0, start_time)
        day.insert(0, day_value)
        start_time_type.set(start_t_type)
        end_time_entry.insert(0, end_time)
        end_time_type.set(end_t_type)
        # op_menu_value.set(org_name)

        # disable fields
        course_id_entry.config(state= "disable")
        course_name_entry.config(state= "disable")
        subject_area_entry.config(state= "disable")
        organizations_entry.config(state= "disable")
        day.config(state= "disable")
        start_date_entry.config(state= "disable")
        end_date_entry.config(state= "disable")
        start_time_entry.config(state= "disable")
        end_time_entry.config(state= "disable")

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
    
    def findSearch(self, record_table, mentor_id, start_time, start_type, end_time, end_type, subj_area, day, error_message_no_mentor):
        if(mentor_id == "Choose a Mentor"):
            # if no selected mentor, display error message
            error_message_no_mentor.config(text="Select a mentor first to search Preference & Availability")
        else:
            # following are the values passed to this function from search fields
            print(mentor_id)
            print(start_time)
            print(start_type)
            print(end_time)
            print(end_type)
            print(subj_area)
            print(day)
            
            error_message_no_mentor.config(text="")

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
                self.populate_record_table(record_table,[])

    def getCheckboxValue(self, list, value, day_list):
        """
            get/remove values of checkboxes
            [Monday, Tuesday, Wednesday, Thursday. Friday]
        """
        if(list.get() == 1):
            if value in day_list:
                #do nothing, already added
                print("exists")
            else:
                day_list.append(value)
        elif(list.get() == 0):
            if value in day_list:
                day_list.remove(value)
        
        return day_list