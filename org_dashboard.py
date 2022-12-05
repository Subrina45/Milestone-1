import tkinter as tk
import os
from organizations.dashboard import OrganizationDashboard
  

class tkinterApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # When the program is started
        # StartPage handles the initial 
        # menu displayed
        script_dir = os.path.abspath( os.path.dirname( __file__ ) )
        self.db_path = script_dir + "\mentor_network.db"
        self.frame = OrganizationDashboard(self)

    # display requested menu
    def show_frame(self, class_name):
        self.frame.destroy()
        self.frame = eval(class_name)(self)

    def get_db_path(self):
        """Return path to the database
        """
        return self.db_path

# Driver Code
app = tkinterApp()
app.mainloop()
