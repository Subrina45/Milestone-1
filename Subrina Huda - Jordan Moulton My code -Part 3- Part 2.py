import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('800x900')
root.title('Tkinter Hub')

#NEW_________________________________________________________________________________________
mentor_data = [[1, "Jordan","MoMo","jmoulton@albany.edu",6316457598,"INF405","Ian MacDonald"],
               [2, "Jordan","MoMo","jmoulton@albany.edu",6316457598,"INF405","Ian MacDonald"],
               [3, "Jordan","MoMo","jmoulton@albany.edu",6316457598,"INF405","Ian MacDonald"],
               [4, "Jordan","MoMo","jmoulton@albany.edu",6316457598,"INF405","Ian MacDonald"],
               [5, "Jordan","MoMo","jmoulton@albany.edu",6316457598,"INF405","Ian MacDonald"]]
#____________________________________________________________________________________________

def load_mentor_data():
    for item in record_table.get_children():
        record_table.delete(item)

    for r in range(len(mentor_data)):
        record_table.insert(parent='', index='end', text='',
                            iid=r, values=mentor_data[r])

def put_mentor_in_entry(index):
    mentor_id.delete(0, tk.END)
    first_name.delete(0, tk.END)
    last_name.delete(0, tk.END)
    mentor_email.delete(0, tk.END)
    cell_phone.delete(0, tk.END)
    subject_area.delete(0, tk.END)
    current_employer.delete(0, tk.END)

    men_id = mentor_data[index][0]
    fir_name = mentor_data[index][1]
    las_name = mentor_data[index][2]
    men_email = mentor_data[index][3]
    cell_number = mentor_data[index][4]
    sub_area = mentor_data[index][5]
    curr_employer = mentor_data[index][6]
    
    mentor_id.insert(0,men_id )
    first_name.insert(0,fir_name )
    last_name.insert(0,las_name )
    mentor_email.insert(0, men_email)
    cell_phone.insert(0,cell_number)
    subject_area.insert(0,sub_area )
    current_employer.insert(0, curr_employer)
        

def clear_mentor_data():
    mentor_id.delete(0, tk.END)
    first_name.delete(0, tk.END)
    last_name.delete(0, tk.END)
    mentor_email.delete(0, tk.END)
    cell_phone.delete(0, tk.END)
    subject_area.delete(0, tk.END)
    current_employer.delete(0, tk.END)
    load_mentor_data()

    


def add_mentor_data(men_id, fir_name, las_name, men_email, cell_number, sub_area, curr_employer):
    mentor_data.append([men_id, fir_name, las_name, men_email,
                        cell_number, sub_area, curr_employer])
    load_mentor_data()
    clear_mentor_data()


def update_student_data(men_id, fir_name, las_name, men_email, cell_number, sub_area, curr_employer,
                        index):
    mentor_data[index] = [men_id, fir_name, las_name, men_email,
                        cell_number, sub_area, curr_employer]
    load_mentor_data()
    clear_mentor_data()

def delete_mentor_data(index):
    del mentor_data[index]
    load_mentor_data()
    clear_mentor_data()

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
        
    
    
head_frame = tk.Frame(root)

heading_lb = tk.Label(head_frame, text='Mentors Registration System',
                     font=('Bold', 13),
                     bg='pink')
heading_lb.pack(fill=tk.X, pady=5)

mentor_id_lb = tk.Label(head_frame, text='Mentor Id:', font=('Bold', 10))
mentor_id_lb.place(x=0, y=50)

mentor_id = tk.Entry(head_frame, font=('Bold', 10))
mentor_id.place(x=110, y=50, width=180)

first_name_lb = tk.Label(head_frame, text='First Name:', font=('Bold', 10))
first_name_lb.place(x=0, y=100)

first_name = tk.Entry(head_frame, font=('Bold', 10))
first_name.place(x=110, y=100, width=180)

last_name_lb = tk.Label(head_frame, text='Last Name:', font=('Bold', 10))
last_name_lb.place(x=0, y=150)

last_name = tk.Entry(head_frame, font=('Bold', 10))
last_name.place(x=110, y=150, width=180)

mentor_email_lb = tk.Label(head_frame, text='Mentor Email:', font=('Bold', 10))
mentor_email_lb.place(x=0, y=200)

mentor_email = tk.Entry(head_frame, font=('Bold', 10))
mentor_email.place(x=110, y=200, width=180)

cell_phone_lb = tk.Label(head_frame, text='Cell Phone:', font=('Bold', 10))
cell_phone_lb.place(x=0, y=250)

cell_phone = tk.Entry(head_frame, font=('Bold', 10))
cell_phone.place(x=110, y=250, width=180)

subject_area_lb = tk.Label(head_frame, text='Subject Area:', font=('Bold', 10))
subject_area_lb.place(x=0, y=300)

subject_area = tk.Entry(head_frame, font=('Bold', 10))
subject_area.place(x=110, y=300, width=180)

current_employer_lb = tk.Label(head_frame, text='Current Employer:', font=('Bold', 10))
current_employer_lb.place(x=0, y=350)

current_employer = tk.Entry(head_frame, font=('Bold', 10))
current_employer.place(x=110, y=350, width=180)

#______________________________Buttons____________________________________________________
register_btn = tk.Button(head_frame, text='Register', font=('Bold', 12),
                         command=lambda: add_mentor_data(mentor_id.get(), first_name.get(),
                                                         last_name.get(), mentor_email.get(),
                                                         cell_phone.get(),subject_area.get(),
                                                         current_employer.get()))
register_btn.place(x=0, y=400)

update_btn = tk.Button(head_frame, text='Update', font=('Bold', 12),
                       command=lambda: update_student_data(mentor_id.get(), first_name.get(),
                                                           last_name.get(),mentor_email.get(),
                                                           cell_phone.get(),subject_area.get(),
                                                           current_employer.get(),
                                                           index=int(record_table.selection()[0])))
update_btn.place(x=85, y=400)

delete_btn = tk.Button(head_frame, text='Delete', font=('Bold', 12),
                       command=lambda: delete_mentor_data(index=int(record_table.selection()[0])))
delete_btn.place(x=160, y=400)

clear_btn = tk.Button(head_frame, text='Clear', font=('Bold', 12),
                      command=lambda: clear_mentor_data())
clear_btn.place(x=230, y=400)
#________________________________Buttons____________________________________________________                               
head_frame.pack(pady=10)
head_frame.pack_propagate(False)
head_frame.configure(width=400, height=500)

search_bar_frame = tk.Frame(root)

search_lb = tk.Label(search_bar_frame, text='Search Mentor by Id:',
                     font=('Bold', 10))
search_lb.pack(anchor=tk.W)

search_entry = tk.Entry(search_bar_frame,
                    font=('Bold', 10))
search_entry.pack(anchor=tk.W)

#New______________________________________________________________________________
search_entry.bind('<KeyRelease>', lambda e: find_mentor_by_id(search_entry.get()))
#_________________________________________________________________________________

search_bar_frame.pack(pady=0)
search_bar_frame.pack_propagate(False)
search_bar_frame.configure(width=400, height=50)

record_frame = tk.Frame(root)

record_lb = tk.Label(record_frame, text= 'Select Record for Delete or Update',
                    bg='pink', font=('Bold', 13))
record_lb.pack(fill=tk.X)

record_table = ttk.Treeview(record_frame)
record_table.pack(fill=tk.X, pady=5)
                       
#New___________________________________________________________________
record_table.bind('<<TreeviewSelect>>', lambda e: put_mentor_in_entry(
    int(record_table.selection()[0])))
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
load_mentor_data()
#___________________________________
                           
record_table.heading('Mentor Id', text='Mentor Id', anchor=tk.W)
record_table.heading('First Name', text='First Name', anchor=tk.W)
record_table.heading('Last Name', text='Last Name', anchor=tk.W)
record_table.heading('Mentor Email', text='Mentor Email', anchor=tk.W)
record_table.heading('Cell Phone', text='Cell Phone', anchor=tk.W)
record_table.heading('Subject Area', text='Subject Area', anchor=tk.W)
record_table.heading('Current Employer', text='Current Employer', anchor=tk.W)

root.mainloop()




