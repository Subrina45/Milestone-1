import tkinter as tk
import sqlite3
from sqlite3 import Error
import os

script_dir = os.path.abspath( os.path.dirname( __file__ ) )

print( script_dir )

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

sql_create_organizations_table = """ CREATE TABLE IF NOT EXISTS organizations (
                                        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                        name TEXT NOT NULL,
                                        address TEXT NOT NULL,
                                        website_url TEXT NOT NULL,
                                        contact_name TEXT NOT NULL,
                                        contact_email TEXT NOT NULL
                                    ); """

conn = create_connection(r"" + script_dir +"\mentor_network.db")

# create tables
if conn is not None:
    # create organizations table
    create_table(conn, sql_create_organizations_table)
else:
    print("Error! cannot create the database connection.")

# Form ====================================================================================

window = tk.Tk()
window.title('My example')
window.geometry("700x250")

title_text = tk.Label(master=window,text="Admin Dashboard for adding, deleting, and modifying Universities or Training Organizations")
title_text.grid(column=0, row=0)

org_name_label = tk.Label(master=window,text="Organization Name")
org_name_label.grid(column=0, row=1)
org_name_entry = tk.Entry(master=window,width=50)
org_name_entry.grid(column=1, row=1)

address_label = tk.Label(master=window,text="Address")
address_label.grid(column=0, row=2)
address_entry = tk.Entry(master=window,width=50)
address_entry.grid(column=1, row=2)

url_label = tk.Label(master=window,text="Website URL")
url_label.grid(column=0, row=3)
url_entry = tk.Entry(master=window,width=50)
url_entry.grid(column=1, row=3)

cont_name_label = tk.Label(master=window,text="Contact Name")
cont_name_label.grid(column=0, row=5)
cont_name_entry = tk.Entry(master=window,width=50)
cont_name_entry.grid(column=1, row=5)

cont_email_label = tk.Label(master=window,text="Contact e-mail")
cont_email_label.grid(column=0, row=4)
cont_email_entry = tk.Entry(master=window,width=50)
cont_email_entry.grid(column=1, row=4)

def add_organization(conn, organization):
    """
    Create a new organization into the organizations table
    :param conn:
    :param organization:
    :return: organization id
    """
    sql = ''' INSERT INTO organizations(name,address,website_url,contact_name,contact_email)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, organization)
    conn.commit()
    return cur.lastrowid

def submitData():
    org_name_value = org_name_entry.get()
    address_entry = org_name_entry.get()
    url_entry = org_name_entry.get()
    cont_name_entry = org_name_entry.get()
    cont_email_entry = org_name_entry.get()

    organization_info = (org_name_value, address_entry, url_entry, cont_name_entry, cont_email_entry)
    organization_id = add_organization(conn, organization_info)

    output_text = tk.Text(master=window, height=2, spacing1=10)
    output_text.grid(column=0, row=41)
    output_text.insert(tk.END, "Organization ID: " + str(organization_id) + " you entered <=== " + org_name_value + " ===> as an organization name")

submit_button = tk.Button(text="Submit", command=submitData).grid(column=0, row=39)
quit_button = tk.Button(text="Quit", command=window.destroy).grid(column=0, row=40)

window.mainloop()
