import tkinter as tk
from tkinter import ttk

class OrganizationsController:
    def __init__(self, model, frame = None, row = None):
        self.model = model
        self.frame = frame
        self.row = row

    def change_frame(self, frame):
        self.frame = frame
    
    def change_row(self, row):
        self.row = row

    def submit_data(self, org_name_entry, address_entry, url_entry, cont_name_entry, cont_email_entry):
        org_name_value = org_name_entry.get()
        address_value = address_entry.get()
        url_value = url_entry.get()
        cont_name_value = cont_name_entry.get()
        cont_email_value = cont_email_entry.get()

        organization_info = (org_name_value, address_value, url_value, cont_name_value, cont_email_value)
        id = self.model.add_organization(organization_info)

        cont_email_entry.delete(0, tk.END)
        org_name_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)
        url_entry.delete(0, tk.END)
        cont_name_entry.delete(0, tk.END)

        output_text = tk.Text(self.frame, height=2, spacing1=10)
        output_text.grid(column=0, row = self.row)
        output_text.insert(tk.END, "Added successfully")

        return id