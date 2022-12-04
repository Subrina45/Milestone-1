import sqlite3
from sqlite3 import Error


class OrganizationsModel:

    def __init__(self, path_to_db):
        self.path = path_to_db
        self.create_table()

    def create_connection(self):
        """ create a database connection to the SQLite database
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(self.path)
            return conn
        except Error as e:
            print(e)

        return conn

    def close_connection(self, conn):
        conn.close()

    def create_table(self):
        """ create a table from the create_table_sql statement
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        conn = self.create_connection()
        c = conn.cursor()
        c.execute(""" CREATE TABLE IF NOT EXISTS organizations (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    address TEXT NOT NULL,
                    website_url TEXT NOT NULL,
                    contact_name TEXT NOT NULL,
                    contact_email TEXT NOT NULL
                ); """)
        self.close_connection(conn)

    def add_organization(self, organization):
        """
        Create a new organization into the organizations table
        :param organization:
        :return: organization id
        """
        conn = self.create_connection()
        sql = ''' INSERT INTO organizations(name,address,website_url,contact_name,contact_email)
                VALUES(?,?,?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, organization)
        conn.commit()
        self.close_connection(conn)
        print("added a new record, ID", cur.lastrowid)
        return cur.lastrowid

    def update_organization(self, organization):
        """
        update name, address, website_url, contact_name, and contact_email of an organization
        :param organization:
        """
        conn = self.create_connection()
        sql = ''' UPDATE organizations
                SET name = ? ,
                    address = ? ,
                    website_url = ? ,
                    contact_name = ? ,
                    contact_email = ?
                WHERE id = ?'''
        cur = conn.cursor()
        cur.execute(sql, organization)
        conn.commit()
        self.close_connection(conn)
        print('Updated', organization)

    def select_all(self):
        """
        Query all rows in the organizations table
        :return:
        """
        conn = self.create_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM organizations")
        rows = cur.fetchall()
        self.close_connection(conn)
        return rows

    def delete_organization(self, id):
        print('deleted', id)
        """
        Delete an organization by organization id
        :param id: id of the organization
        :return:
        """
        conn = self.create_connection()
        sql = 'DELETE FROM organizations WHERE id=?'
        cur = conn.cursor()
        cur.execute(sql, (id,))
        conn.commit()
        self.close_connection(conn)

    def select_by_name(self, name):
        """
        Query organiations by name
        :param name:
        :return:
        """
        conn = self.create_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM organizations WHERE name=?", (name,))
        rows = cur.fetchall()
        self.close_connection(conn)
        return rows