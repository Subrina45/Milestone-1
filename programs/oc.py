import tkinter as tk
from tkinter import ttk
from organizations.om import OrganizationsModel


class OrganizationsController:

    def __init__(self, path_to_db):
        self.fields = ['ID','Organization Name', 'Address', 'Website URL', 'Contact e-mail', 'Contact Name']
        self.model = OrganizationsModel(r"" + path_to_db)

    def construct_add_frame(self, parent_frame):
        fields_copy = self.fields.copy()
        fields_copy.pop(0) # remove id from the fields. Don't want users to enter their own ids
        entries = []

        row_value = 0
        for field in fields_copy:
            label = tk.Label(parent_frame, text=field)
            label.grid(column=0, row=row_value)
            entry = tk.Entry(parent_frame, width=50)
            entry.grid(column=1, row=row_value)
            entries.append(entry)
            row_value += 1

        label = tk.Label(parent_frame)
        label.grid(column = 1, row=row_value)
        row_value += 1

        submit_button = tk.Button(parent_frame, text="Submit", command = lambda : self.submit_data(entries, label))
        submit_button.grid(column=1, row=row_value)
        row_value += 1

    def construct_delete_frame(self, parent_frame):
        records = self.model.select_all()
        frame_row = 0

        main_frame = tk.Label(parent_frame)
        main_frame.grid(column = 0, row = 0, ipadx=7, sticky = "NSEW")
        main_frame.grid_columnconfigure(0, weight = 1)

        fields_frame = tk.Label(main_frame)
        fields_frame.grid(column = 0, row = frame_row, sticky = "NSEW")
        frame_row += 1

        column_value = 0
        for field in self.fields:
            fields_frame.grid_columnconfigure(column_value, weight = 1)
            label_frame = tk.LabelFrame(fields_frame)
            label_frame.grid(column = column_value, row = frame_row, sticky = "NSWE")
            tk.Label(label_frame,text = field).grid(column = 0, row = 0)
            column_value += 1

        frame_row += 1

        for record in records:
            records_frame = tk.Label(main_frame)
            records_frame.grid(column = 0, row = frame_row, sticky="NSEW")
            column_value = 0
            id = None
            is_id_found = False
            for value in record:
                if is_id_found == False:
                    id = int(value)
                    is_id_found = True
                records_frame.grid_columnconfigure(column_value, weight = 1)
                label_frame = tk.LabelFrame(records_frame)
                label_frame.grid(column = column_value, row = frame_row, sticky="NSW")
                tk.Label(label_frame, text = value).grid(column = 0, row = 0)
                column_value += 1
            # every time a record is deleted
            # need to update the frame to show the most up-to-date data
            delete_button = ttk.Button(main_frame, text = "Delete")
            delete_button.configure(command = lambda id=id, delete_button=delete_button, records_frame=records_frame: self.delete_record(id, records_frame,delete_button))
            delete_button.grid(row = frame_row, column = 1)
            is_id_found = False
            frame_row += 1

    def construct_modify_frame(self, parent_frame):
        records = self.model.select_all()
        frame_row = 0

        column_value = 0
        for field in self.fields:
            label_frame = tk.LabelFrame(parent_frame)
            label_frame.grid(column = column_value, row = frame_row, sticky = "NSEW")
            tk.Label(label_frame,text = field).grid(column = 0, row = 0, sticky = "NSEW")
            column_value += 1

        frame_row += 1

        for record in records:
            column_value = 0
            id = None
            is_id_found = False
            entries = []
            for value in record:
                label_frame = tk.LabelFrame(parent_frame)
                label_frame.grid(column = column_value, row = frame_row, sticky="NSEW")
                if is_id_found == False:
                    id = int(value)
                    is_id_found = True
                    tk.Label(label_frame,text = id).grid(column = 0, row = 0, sticky="NSEW")
                else:
                    entry = tk.Entry(label_frame)
                    entry.grid(column = column_value, row = 0, sticky="NSEW")
                    entry.insert(0, value)
                    entries.append(entry)
                column_value += 1
            update_button = ttk.Button(parent_frame, text = "Update", command = lambda id=id, entries=entries : self.update_record(id, entries))
            update_button.grid(row = frame_row, column = column_value)
            is_id_found = False
            frame_row += 1

    def submit_data(self, elements, label):
        values = []

        for element in elements:
            values.append(element.get())

        id = self.model.add_organization(tuple(values))

        for element in elements:
            element.delete(0, tk.END)

        label.config(text = "Added successfully")

        return id

    def update_record(self, id, elements):
        values = []
        for element in elements:
            values.append(element.get())

        values.append(id)
        record = tuple(values)
        self.model.update_organization(record)

    def delete_record(self, id, frame, button):
        self.model.delete_organization(id)
        frame.destroy()
        button.destroy()