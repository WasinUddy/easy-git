from tkinter import *

class GUI():

    def __init__(self):
        self.window = Tk()
        self.title = "Easy Git"

        # Set windows title name
        self.window.title(self.title)

    def login(self):
        # greeting_label = Label(self.window, text="Welcome to Easy Git please login")
        # greeting_label.grid(column=0, row=0)


        username_label = Label(self.window, text="Username   : ")
        username_input = Entry(self.window, width=30)
        username_label.grid(column=0, row=1)
        username_input.grid(column=1, row=1)

        email_label = Label(self.window, text="Email          :")
        email_input = Entry(self.window, width=30)
        email_label.grid(column=0, row=2)
        email_input.grid(column=1, row=2)

        password_label = Label(self.window, text="Password   :")
        password_input = Entry(self.window, width=30, show="*")
        password_label.grid(column=0, row=3)
        password_input.grid(column=1, row=3)

    def run(self):
        self.window.mainloop()

a = GUI()
a.login()
a.run()