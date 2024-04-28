import tkinter as tk
from tkinter import messagebox


class PasswordManager:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Manager")

        self.label_username = tk.Label(master, text="Username:")
        self.label_username.grid(row=0, column=0, sticky=tk.E)
        self.entry_username = tk.Entry(master)
        self.entry_username.grid(row=0, column=1)

        self.label_password = tk.Label(master, text="Password:")
        self.label_password.grid(row=1, column=0, sticky=tk.E)
        self.entry_password = tk.Entry(master, show="*")
        self.entry_password.grid(row=1, column=1)

        self.button_save = tk.Button(master, text="Save", command=self.save_password)
        self.button_save.grid(row=2, column=0, columnspan=2, pady=10)

    def save_password(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        # Here you can add code to store the username and password securely,
        # such as in a database or encrypted file.
        messagebox.showinfo("Success", "Password saved successfully!")


def main():
    root = tk.Tk()
    app = PasswordManager(root)
    root.mainloop()


if __name__ == "__main__":
    main()
