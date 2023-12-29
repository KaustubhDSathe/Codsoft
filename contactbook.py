import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self):
        self.contacts = []
        self.current_index = -1

    def add_contact(self, name, phone, email, address):
        contact = {'Name': name, 'Phone': phone, 'Email': email, 'Address': address}
        self.contacts.append(contact)
        messagebox.showinfo('Success', 'Contact added successfully!')

    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo('Info', 'No contacts available.')
            return

        contact_list = ''
        for index, contact in enumerate(self.contacts, start=1):
            contact_list += f"{index}. Name: {contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}, Address: {contact['Address']}\n"
        
        messagebox.showinfo('Contacts', contact_list)

    def search_contact(self, name):
        for index, contact in enumerate(self.contacts):
            if contact['Name'].lower() == name.lower():
                self.current_index = index
                return contact
        return None

    def update_contact(self, phone, email, address):
        if self.current_index != -1:
            self.contacts[self.current_index]['Phone'] = phone
            self.contacts[self.current_index]['Email'] = email
            self.contacts[self.current_index]['Address'] = address
            messagebox.showinfo('Success', 'Contact updated successfully!')
        else:
            messagebox.showinfo('Error', 'No contact selected for update.')

    def delete_contact(self):
        if self.current_index != -1:
            del self.contacts[self.current_index]
            self.current_index = -1
            messagebox.showinfo('Success', 'Contact deleted successfully!')
        else:
            messagebox.showinfo('Error', 'No contact selected for deletion.')

class ContactBookGUI:
    def __init__(self, master):
        self.master = master
        self.master.title('Contact Book')

        self.contact_book = ContactBook()

        self.name_label = tk.Label(master, text='Name:')
        self.name_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)

        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)

        self.phone_label = tk.Label(master, text='Phone:')
        self.phone_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)

        self.phone_entry = tk.Entry(master)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

        self.email_label = tk.Label(master, text='Email:')
        self.email_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)

        self.email_entry = tk.Entry(master)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)

        self.address_label = tk.Label(master, text='Address:')
        self.address_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.E)

        self.address_entry = tk.Entry(master)
        self.address_entry.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)

        self.add_button = tk.Button(master, text='Add Contact', command=self.add_contact)
        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.view_button = tk.Button(master, text='View Contacts', command=self.view_contacts)
        self.view_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.search_label = tk.Label(master, text='Search by Name:')
        self.search_label.grid(row=6, column=0, padx=10, pady=5, sticky=tk.E)

        self.search_entry = tk.Entry(master)
        self.search_entry.grid(row=6, column=1, padx=10, pady=5, sticky=tk.W)

        self.search_button = tk.Button(master, text='Search Contact', command=self.search_contact)
        self.search_button.grid(row=7, column=0, columnspan=2, pady=10)

        self.update_button = tk.Button(master, text='Update Contact', command=self.update_contact)
        self.update_button.grid(row=8, column=0, columnspan=2, pady=10)

        self.delete_button = tk.Button(master, text='Delete Contact', command=self.delete_contact)
        self.delete_button.grid(row=9, column=0, columnspan=2, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone and email and address:
            self.contact_book.add_contact(name, phone, email, address)
            self.clear_entries()
        else:
            messagebox.showinfo('Error', 'Please fill in all fields.')

    def view_contacts(self):
        self.contact_book.view_contacts()

    def search_contact(self):
        name = self.search_entry.get()
        if name:
            contact = self.contact_book.search_contact(name)
            if contact:
                messagebox.showinfo('Contact', f"Name: {contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}, Address: {contact['Address']}")
            else:
                messagebox.showinfo('Error', 'Contact not found.')
        else:
            messagebox.showinfo('Error', 'Please enter a name for search.')

    def update_contact(self):
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        self.contact_book.update_contact(phone, email, address)
        self.clear_entries()

    def delete_contact(self):
        self.contact_book.delete_contact()
        self.clear_entries()

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

if __name__ == '__main__':
    root = tk.Tk()
    app = ContactBookGUI(root)
    root.mainloop()
