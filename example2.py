import tkinter as tk
from tkinter import ttk
import os
from om import OrganizationsModel
from oc import OrganizationsController

LARGEFONT =("Verdana", 35)
  
class tkinterApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.frame = StartPage(self, self)
        script_dir = os.path.abspath( os.path.dirname( __file__ ) )
        self.db_path = script_dir + "\mentor_network.db"

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        self.frame.destroy()
        self.frame = cont(self, self)

    def get_db_path(self):
        return self.db_path

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.pack(side = "top", fill = "both", expand = True)
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)

        label = ttk.Label(self, text ="SP", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        button1 = ttk.Button(self, text ="Organizations", command = lambda : controller.show_frame(Organizations))
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        button2 = ttk.Button(self, text ="Courses", command = lambda : controller.show_frame(Courses))
        button2.grid(row = 1, column = 2, padx = 10, pady = 10)

class Organizations(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.pack(side = "top", fill = "both", expand = True)
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)
        self.container = self.get_initial_frame(self)
        self.parent_controller = controller
        self.controller = OrganizationsController(OrganizationsModel(r"" + controller.get_db_path()))

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        self.container.destroy()
        if cont == 'initial':
            self.container = self.get_initial_frame(self)
        if cont == 'add':
            self.container = self.get_add_frame(self)
        if cont == 'delete':
            self.container = self.get_delete_frame(self)
        if cont == 'modify':
            self.container = self.construct_modify_frame(self)

    def get_initial_frame(self, parent):
        frame = tk.Frame(master=parent)
        frame.pack(side = "top", fill = "both", expand = True)
  
        frame.grid_rowconfigure(0, weight = 1)
        frame.grid_columnconfigure(0, weight = 1)

        label = ttk.Label(frame, text ="Org", font = LARGEFONT)
        label.grid(row = 0, column = 1, padx = 10, pady = 10)

        button1 = ttk.Button(frame, text ="Add", command = lambda : self.show_frame('add'))
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        button2 = ttk.Button(frame, text ="modify", command = lambda : self.show_frame('modify'))
        button2.grid(row = 1, column = 2, padx = 10, pady = 10)

        button3 = ttk.Button(frame, text ="Delete", command = lambda : self.show_frame('delete'))
        button3.grid(row = 1, column = 3, padx = 10, pady = 10)

        back_button = ttk.Button(frame, text ="Back", command = lambda : self.parent_controller.show_frame(StartPage))
        back_button.grid(row = 2, column = 2, padx = 10, pady = 10)

        return frame

    def get_add_frame(self,parent):
        row_value = 0

        frame = tk.Frame(master=parent)
        frame.pack(side = "top", fill = "both", expand = True)
  
        frame.grid_rowconfigure(0, weight = 1)
        frame.grid_columnconfigure(0, weight = 1)

        label = ttk.Label(frame, text ="Add an organization", font = LARGEFONT)
        label.grid(row = row_value, column = 0)
        row_value += 1

        org_name_label = tk.Label(frame,text="Organization Name")
        org_name_label.grid(column=0, row=row_value)
        org_name_entry = tk.Entry(frame,width=50)
        org_name_entry.grid(column=1, row=row_value)
        row_value += 1

        address_label = tk.Label(frame,text="Address")
        address_label.grid(column=0, row= row_value)
        address_entry = tk.Entry(frame, width=50)
        address_entry.grid(column=1, row= row_value)
        row_value += 1

        url_label = tk.Label(frame,text="Website URL")
        url_label.grid(column=0, row=row_value)
        url_entry = tk.Entry(frame, width=50)
        url_entry.grid(column=1, row=row_value)
        row_value += 1

        cont_email_label = tk.Label(frame,text="Contact e-mail")
        cont_email_label.grid(column=0, row=row_value)
        cont_email_entry = tk.Entry(frame, width=50)
        cont_email_entry.grid(column=1, row=row_value)
        row_value += 1

        cont_name_label = tk.Label(frame,text="Contact Name")
        cont_name_label.grid(column=0, row=row_value)
        cont_name_entry = tk.Entry(frame, width=50)
        cont_name_entry.grid(column=1, row=row_value)
        row_value += 1

        self.controller.change_frame(frame)
        self.controller.change_row(row_value)
        row_value += 1

        submit_button = tk.Button(frame,
                                text="Submit", 
                                command = lambda : self.controller.submit_data(org_name_entry, address_entry,
                                                                            url_entry,cont_name_entry,cont_email_entry))
        submit_button.grid(column=0, row=row_value)
        row_value += 1

        back_button = ttk.Button(frame, text ="Back", command = lambda : self.show_frame('initial'))
        back_button.grid(row = row_value, column = 0)

        return frame

    def get_delete_frame(self, parent):
        frame = tk.Frame(master=parent)
        frame.pack(side = "top", fill = "both", expand = True)
  
        frame.grid_rowconfigure(0, weight = 1)
        frame.grid_columnconfigure(0, weight = 1)

        label = ttk.Label(frame, text ="Delete", font = LARGEFONT)
        label.grid(row = 0, column = 0)
        return frame

    def construct_modify_frame(self, parent):
        frame = tk.Frame(master=parent)
        frame.pack(side = "top", fill = "both", expand = True)
  
        frame.grid_rowconfigure(0, weight = 1)
        frame.grid_columnconfigure(0, weight = 1)

        label = ttk.Label(frame, text ="Modify", font = LARGEFONT)
        label.grid(row = 0, column = 0)
        return frame

# second window frame Courses
class Courses(tk.Frame):
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="p1", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Organizations",
                            command = lambda : controller.show_frame(Organizations))
     
        # putting the button in its place
        # by using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button2 = ttk.Button(self, text ="Page 2",
                            command = lambda : controller.show_frame(Page2))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)
  
  
  
  
# third window frame page2
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="p2", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Page 1",
                            command = lambda : controller.show_frame(Courses))
     
        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text ="Organizations",
                            command = lambda : controller.show_frame(Organizations))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)
  
  
# Driver Code
app = tkinterApp()
app.mainloop()