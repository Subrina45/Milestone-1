import tkinter as tk
from tkinter import ttk
from mentors.mm import MentorsModel
import mentors.fonts

class Mentors(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.pack(side = "top", fill = "both", expand = True)
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)
        self.parent_controller = parent
        self.model = MentorsModel(r"" + parent.get_db_path())
        self.container = self.get_initial_frame(self)

    def get_initial_frame(self, parent_frame):
        head_frame = tk.Frame(parent_frame)
        head_frame.pack(pady=10)
        head_frame.pack_propagate(False)
        head_frame.configure(width=400, height=500)

        heading_lb = tk.Label(head_frame, text='Mentors Registration System',
                     font=('Bold', 13),
                     bg='pink')
        heading_lb.pack(fill=tk.X, pady=5)

        first_name_lb = tk.Label(head_frame, text='First Name:', font=('Bold', 10))
        first_name_lb.place(x=0, y=100)

        first_name = tk.Entry(head_frame, font=('Bold', 10))
        first_name.place(x=110, y=100, width=180)

        last_name_lb = tk.Label(head_frame, text='Last Name:', font=mentors.fonts.sub)
        last_name_lb.place(x=0, y=150)

        last_name = tk.Entry(head_frame, font=mentors.fonts.sub)
        last_name.place(x=110, y=150, width=180)

        mentor_email_lb = tk.Label(head_frame, text='Mentor Email:', font=mentors.fonts.sub)
        mentor_email_lb.place(x=0, y=200)

        mentor_email = tk.Entry(head_frame, font=mentors.fonts.sub)
        mentor_email.place(x=110, y=200, width=180)

        cell_phone_lb = tk.Label(head_frame, text='Cell Phone:', font=mentors.fonts.sub)
        cell_phone_lb.place(x=0, y=250)

        cell_phone = tk.Entry(head_frame, font=mentors.fonts.sub)
        cell_phone.place(x=110, y=250, width=180)

        subject_area_lb = tk.Label(head_frame, text='Subject Area:', font=mentors.fonts.sub)
        subject_area_lb.place(x=0, y=300)

        subject_area = tk.Entry(head_frame, font=mentors.fonts.sub)
        subject_area.place(x=110, y=300, width=180)

        current_employer_lb = tk.Label(head_frame, text='Current Employer:', font=mentors.fonts.sub)
        current_employer_lb.place(x=0, y=350)

        current_employer = tk.Entry(head_frame, font=mentors.fonts.sub)
        current_employer.place(x=110, y=350, width=180)

        #______________________________Buttons____________________________________________________
        register_btn = tk.Button(head_frame, text='Register', font=('Bold', 12),
                                command=lambda: self.add_mentor_data(record_table, [first_name, last_name, 
                                                                    mentor_email, cell_phone,
                                                                    subject_area, current_employer]))
        register_btn.place(x=0, y=400)

        update_btn = tk.Button(head_frame, text='Update', font=('Bold', 12),
                            command=lambda: self.update_student_data(record_table, first_name, last_name, 
                                                                    mentor_email, cell_phone,
                                                                    subject_area, current_employer))
        update_btn.place(x=85, y=400)

        delete_btn = tk.Button(head_frame, text='Delete', font=('Bold', 12),
                            command=lambda: self.delete_mentor_data(record_table, [first_name, last_name,
                                                                    mentor_email, cell_phone,
                                                                    subject_area, current_employer]))
        delete_btn.place(x=160, y=400)

        clear_btn = tk.Button(head_frame, text='Clear', font=('Bold', 12),
                            command=lambda: self.clear_mentor_data([first_name, last_name,
                                                                    mentor_email, cell_phone,
                                                                    subject_area, current_employer])
                            )
        clear_btn.place(x=230, y=400)

        back_btn = tk.Button(head_frame, text ="Back", font=('Bold', 12),
                            command = lambda : self.parent_controller.show_frame('StartPage'))
        back_btn.place(x=230, y=450)
        #________________________________Buttons____________________________________________________

        search_bar_frame = tk.Frame(parent_frame)

        search_lb = tk.Label(search_bar_frame, text='Search Mentor by Id:',
                            font=mentors.fonts.sub)
        search_lb.pack(anchor=tk.W)

        search_entry = tk.Entry(search_bar_frame,
                            font=mentors.fonts.sub)
        search_entry.pack(anchor=tk.W)

        #New______________________________________________________________________________
        search_entry.bind('<KeyRelease>', lambda e: find_mentor_by_id(search_entry.get()))
        #_________________________________________________________________________________

        search_bar_frame.pack(pady=0)
        search_bar_frame.pack_propagate(False)
        search_bar_frame.configure(width=400, height=50)

        record_frame = tk.Frame(parent_frame)

        record_lb = tk.Label(record_frame, text= 'Select Record for Delete or Update',
                            bg='pink', font=mentors.fonts.main)
        record_lb.pack(fill=tk.X)

        record_table = ttk.Treeview(record_frame)
        record_table.pack(fill=tk.X, pady=5)
                            
        #New___________________________________________________________________
        record_table.bind('<ButtonRelease-1>', lambda e: self.put_mentor_in_entry(record_table, first_name, last_name,
                                                                                    mentor_email, cell_phone,
                                                                                    subject_area, current_employer))
        #______________________________________________________________________

        record_table['column'] = ['Mentor Id', 'First Name', 'Last Name', 'Mentor Email', 'Cell Phone', 'Subject Area', 'Current Employer']

        record_table.column('#0', anchor=tk.W, width=0, stretch=tk.NO)

        record_table.column('Mentor Id', anchor=tk.W, width=60)
        record_table.column('First Name', anchor=tk.W, width=100)
        record_table.column('Last Name', anchor=tk.W, width=100)
        record_table.column('Mentor Email', anchor=tk.W, width=130)
        record_table.column('Cell Phone', anchor=tk.W, width=100)
        record_table.column('Subject Area', anchor=tk.W, width=200)
        record_table.column('Current Employer', anchor=tk.W, width=200)


        record_frame.pack(pady=10)
        record_frame.pack_propagate(False)
        record_frame.configure(width=900, height=700)
        #New_______________________________
        self.load_mentor_data(record_table)
        #___________________________________
                                
        record_table.heading('Mentor Id', text='Mentor Id', anchor=tk.W)
        record_table.heading('First Name', text='First Name', anchor=tk.W)
        record_table.heading('Last Name', text='Last Name', anchor=tk.W)
        record_table.heading('Mentor Email', text='Mentor Email', anchor=tk.W)
        record_table.heading('Cell Phone', text='Cell Phone', anchor=tk.W)
        record_table.heading('Subject Area', text='Subject Area', anchor=tk.W)
        record_table.heading('Current Employer', text='Current Employer', anchor=tk.W)

        return head_frame

    def load_mentor_data(self, record_table):
        mentors = self.model.select_all()

        for item in record_table.get_children():
            record_table.delete(item)

        for r in range(len(mentors)):
            record_table.insert(parent='', index='end', text='',
                                iid=r, values=mentors[r])

    def put_mentor_in_entry(self, record_table, first_name, last_name, mentor_email,
                            cell_phone, subject_area, current_employer):
        curItem = record_table.focus()
        values = record_table.item(curItem)['values']
        mentor_id = values[0]

        mentor = self.model.select_mentor_by_id(mentor_id)[0]
        print(mentor)

        first_name.delete(0, tk.END)
        last_name.delete(0, tk.END)
        mentor_email.delete(0, tk.END)
        cell_phone.delete(0, tk.END)
        subject_area.delete(0, tk.END)
        current_employer.delete(0, tk.END)

        fir_name = mentor[1]
        las_name = mentor[2]
        men_email = mentor[3]
        cell_number = mentor[4]
        sub_area = mentor[5]
        curr_employer = mentor[6]
        
        first_name.insert(0,fir_name )
        last_name.insert(0,las_name )
        mentor_email.insert(0, men_email)
        cell_phone.insert(0,cell_number)
        subject_area.insert(0,sub_area )
        current_employer.insert(0, curr_employer)

    def clear_mentor_data(self, entries):
        for element in entries:
            element.delete(0, tk.END)

    def add_mentor_data(self, record_table, elements):
        values = []

        for element in elements:
            print(element.get())
            values.append(element.get())

        id = self.model.add_mentor(tuple(values))
        self.clear_mentor_data(elements)
        self.load_mentor_data(record_table)

    def update_student_data(self, record_table, first_name, last_name, 
                            mentor_email, cell_phone,
                            subject_area, current_employer):
        curItem = record_table.focus()
        mentor_id = record_table.item(curItem)['values'][0]

        values = []
        values.append(first_name.get())
        values.append(last_name.get())
        values.append(mentor_email.get())
        values.append(cell_phone.get())
        values.append(subject_area.get())
        values.append(current_employer.get())
        values.append(mentor_id)
        print(values)
        self.model.update_mentor(tuple(values))

        self.load_mentor_data(record_table)
        self.clear_mentor_data([first_name, last_name, 
                            mentor_email, cell_phone,
                            subject_area, current_employer])

    def delete_mentor_data(self, record_table, elements):
        curItem = record_table.focus()
        values = record_table.item(curItem)['values']
        mentor_id = values[0]
        print(mentor_id)
        self.model.delete_mentor(mentor_id)
        self.load_mentor_data(record_table)
        self.clear_mentor_data(elements)

    def find_mentor_by_id(men_id):
        if men_id != "":
            mentor_data_index = []

            for data in mentor_data:
                
                if str(men_id) in str(data[0]):
                    mentor_data_index.append(mentor_data.index(data))
                    

            for item in record_table.get_children():
                record_table.delete(item)

            for r in mentor_data_index:
                record_table.insert(parent='', index='end', text='',
                                    iid=r, values=mentor_data[r])
        else:
            load_mentor_data()