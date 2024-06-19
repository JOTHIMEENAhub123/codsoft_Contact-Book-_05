import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self, root):
        self.root = root
        self.contacts = []
        self.create_widgets()

    def create_widgets(self):
        # Create frames
        self.frame1 = tk.Frame(self.root)
        self.frame1.pack(fill="x")
        self.frame2 = tk.Frame(self.root)
        self.frame2.pack(fill="x")
        self.frame3 = tk.Frame(self.root)
        self.frame3.pack(fill="x")

        # Create labels and entries
        tk.Label(self.frame1, text="Name:").pack(side="left")
        self.name_entry = tk.Entry(self.frame1)
        self.name_entry.pack(side="left")
        tk.Label(self.frame1, text="Phone Number:").pack(side="left")
        self.phone_number_entry = tk.Entry(self.frame1)
        self.phone_number_entry.pack(side="left")

        tk.Label(self.frame2, text="Email:").pack(side="left")
        self.email_entry = tk.Entry(self.frame2)
        self.email_entry.pack(side="left")
        tk.Label(self.frame2, text="Address:").pack(side="left")
        self.address_entry = tk.Entry(self.frame2)
        self.address_entry.pack(side="left")

        # Create buttons
        tk.Button(self.frame3, text="Add Contact", command=self.add_contact).pack(side="left")
        tk.Button(self.frame3, text="View Contacts", command=self.view_contacts).pack(side="left")
        tk.Button(self.frame3, text="Search Contact", command=self.search_contact).pack(side="left")
        tk.Button(self.frame3, text="Update Contact", command=self.update_contact).pack(side="left")
        tk.Button(self.frame3, text="Delete Contact", command=self.delete_contact).pack(side="left")

        # Create listbox
        self.listbox = tk.Listbox(self.root)
        self.listbox.pack(fill="both", expand=True)

    def add_contact(self):
        name = self.name_entry.get()
        phone_number = self.phone_number_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        if name and phone_number:
            contact = Contact(name, phone_number, email, address)
            self.contacts.append(contact)
            self.listbox.insert("end", f"{name} - {phone_number}")
            self.name_entry.delete(0, "end")
            self.phone_number_entry.delete(0, "end")
            self.email_entry.delete(0, "end")
            self.address_entry.delete(0, "end")
        else:
            messagebox.showerror("Error", "Name and phone number are required!")

    def view_contacts(self):
        self.listbox.delete(0, "end")
        for contact in self.contacts:
            self.listbox.insert("end", f"{contact.name} - {contact.phone_number}")

    def search_contact(self):
        search_term = tk.simpledialog.askstring("Search Contact", "Enter name or phone number to search:")
        if search_term:
            found_contacts = [contact for contact in self.contacts if search_term in contact.name or search_term in contact.phone_number]
            if found_contacts:
                self.listbox.delete(0, "end")
                for contact in found_contacts:
                    self.listbox.insert("end", f"{contact.name} - {contact.phone_number}")
            else:
                messagebox.showinfo("Search Result", "No contacts found!")

    def update_contact(self):
        search_term = tk.simpledialog.askstring("Update Contact", "Enter name or phone number to update:")
        if search_term:
            found_contacts = [contact for contact in self.contacts if search_term in contact.name or search_term in contact.phone_number]
            if found_contacts:
                contact = found_contacts[0]
                name = tk.simpledialog.askstring("Update Contact", "Enter new name:", initialvalue=contact.name)
                phone_number = tk.simpledialog.askstring("Update Contact", "Enter new phone number:", initialvalue=contact.phone_number)
                email = tk.simpledialog.ask