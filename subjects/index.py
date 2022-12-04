import tkinter as tk
from tkinter import ttk
from subjects.fms import subjectsModel
import subjects.fonts

class SubjectsForm(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.pack(side = "top", fill = "both", expand = True)
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)
        self.parent_controller = parent
        self.model = subjectsModel(r"" + parent.get_db_path())

        self.container = self.get_initial_frame(self)

    def get_initial_frame(self, parent_frame):
        head_frame = tk.Frame(parent_frame)
        head_frame.pack(pady=10)
        head_frame.pack_propagate(False)
        head_frame.configure(width=400, height=500)

        heading_lb = tk.Label(head_frame, text='Subject Area Registration',
                     font=('Bold', 13),
                     bg='pink')
        heading_lb.pack(fill=tk.X, pady=5)

        subject_area_lb = tk.Label(head_frame, text='Subject Area:', font=subjects.fonts.sub)
        subject_area_lb.place(x=0, y=100)

        subject_area_entry = tk.Entry(head_frame, font=subjects.fonts.sub)
        subject_area_entry.place(x=110, y=100, width=180)
        #______________________________Buttons____________________________________________________
        register_btn = tk.Button(head_frame, text='Submit', font=subjects.fonts.mid,
                                command=lambda: self.add_subject_data(record_table, [subject_area_entry]))
        register_btn.place(x=0, y=180)

        update_btn = tk.Button(head_frame, text='Update', font=subjects.fonts.mid,
                            command=lambda: self.update_subject_data(record_table,
                                                                    subject_area_entry))
        update_btn.place(x=85, y=180)

        delete_btn = tk.Button(head_frame, text='Delete', font=subjects.fonts.mid,
                            command=lambda: self.delete_subject_data(record_table, [subject_area_entry]))
        delete_btn.place(x=160, y=180)

        clear_btn = tk.Button(head_frame, text='Clear', font=subjects.fonts.mid,
                            command=lambda: self.clear_subject_data([subject_area_entry])
                            )
        clear_btn.place(x=230, y=180)

        back_btn = tk.Button(head_frame, text ="Back", font=subjects.fonts.mid,
                            command = lambda : self.parent_controller.show_frame('StartPage'))
        back_btn.place(x=230, y=250)
        #________________________________Buttons____________________________________________________
        #New______________________________________________________________________________
        #_________________________________________________________________________________

        # search_bar_frame = tk.Frame(parent_frame)

        # search_lb = tk.Label(search_bar_frame, text='',
        #                     font=subjects.fonts.sub)
        # search_lb.pack(anchor=tk.W)

        # search_entry = tk.Entry(search_bar_frame,
        #                     font=subjects.fonts.sub)
        # search_entry.pack(anchor=tk.W)

        # #New______________________________________________________________________________
        # search_entry.bind('<KeyRelease>', lambda e: self.find_mentor_by_subject(record_table, search_entry.get()))
        # #_________________________________________________________________________________

        # search_bar_frame.pack(pady=0)
        # search_bar_frame.pack_propagate(False)
        # search_bar_frame.configure(width=400, height=50)

        record_frame = tk.Frame(parent_frame)

        record_lb = tk.Label(record_frame, text= 'Select Record for Delete or Update',
                            bg='pink', font=subjects.fonts.main)
        record_lb.pack(fill=tk.X)

        record_table = ttk.Treeview(record_frame)
        record_table.pack(fill=tk.X, pady=5)
                            
        #New___________________________________________________________________
        record_table.bind('<ButtonRelease-1>', lambda e: self.put_subject_in_entry(record_table,
                                                                                    subject_area_entry))
        #______________________________________________________________________

        record_table['column'] = ['Subject Id', 'Subject Area']

        record_frame.pack(pady=10)
        record_frame.pack_propagate(False)
        record_frame.configure(width=900, height=700)
        #New_______________________________
        # self.load_subject_data(record_table)
        #___________________________________
                                
        record_table.heading('Subject Id', text='Subject Id')
        record_table.heading('Subject Area', text='Subject Area')

        record_table.column('#0', anchor=tk.W, width=0, stretch=tk.NO)
        record_table.column('Subject Id', anchor=tk.W, width=60)
        record_table.column('Subject Area', anchor=tk.W, width=200)

        self.load_data(record_table)

        return head_frame


    def load_data(self, record_table):
        programs = self.model.select_all()
        self.load_subject_data(record_table)
            
    def load_subject_data(self, record_table):
        subject = self.model.select_all()
        print(subject)
        for item in record_table.get_children():
            record_table.delete(item)

        for r in range(len(subject)):
            record_table.insert(parent='', index='end', text='',
                                iid=r, values=subject[r])

        # for r in range(len(programs)):
        #     program_copy = list(programs[r]).copy()
        #     record_table.insert(parent='', index='end', text='',
        #                         iid=r, values=tuple(program_copy))

    def put_subject_in_entry(self, record_table,
                            subject_area_entry):
        curItem = record_table.focus()
        values = record_table.item(curItem)['values']
        subject_id = values[0]

        subject_ = self.model.select_subject_by_id(subject_id)[0]
        print(subject_)

        # id.delete(0, tk.END)
        subject_area_entry.delete(0, tk.END)

        sub_area = subject_[1]
        subject_area_entry.insert(0,sub_area )

    def clear_subject_data(self, entries):
        for element in entries:
            element.delete(0, tk.END)

    def add_subject_data(self, record_table, elements):
        values = []

        for element in elements:
            print(element.get())
            values.append(element.get())

        id = self.model.add_subject(tuple(values))
        self.clear_subject_data(elements)
        self.load_subject_data(record_table)

    def update_subject_data(self, record_table,
                            subject_area_entry):
        curItem = record_table.focus()
        subject_id = record_table.item(curItem)['values'][0]

        values = []
        values.append(subject_area_entry.get())
        values.append(subject_id)
        print(values)
        self.model.update_subject(tuple(values))

        self.load_subject_data(record_table)
        self.clear_subject_data([subject_area_entry])

    def delete_subject_data(self, record_table, elements):
        curItem = record_table.focus()
        values = record_table.item(curItem)['values']
        subject_id = values[0]
        print(subject_id)
        self.model.delete_subject(subject_id)
        self.load_subject_data(record_table)
        self.clear_subject_data(elements)

    def find_subject_by_subject(self, record_table, subject_area_entry):
        if subject_area_entry != "":
            subject = self.model.select_subject_by_subject_area(subject_area_entry)

            for item in record_table.get_children():
                record_table.delete(item)

            for r in range(len(subject)):
                record_table.insert(parent='', index='end', text='',
                                iid=r, values=subject[r])
        else:
            self.load_subject_data(record_table)