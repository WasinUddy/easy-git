from tkinter import *
import os

class GUI():

    def __init__(self):
        self.window = Tk()
        self.title = "Easy Git"

        # Set windows title name
        self.window.title(self.title)

    def __login_page(self):
        # Welcome text at the head of the program
        greeting_label = Label(self.window, text="Welcome to Easy Git please login")
        greeting_label.grid(row=0, columnspan=2)

        # Username Input 
        username_label = Label(self.window, text="Username   : ")
        self.username_input = Entry(self.window, width=30)
        username_label.grid(column=0, row=1, sticky="W")
        self.username_input.grid(column=1, row=1, sticky="W")

        # Email Input
        email_label = Label(self.window, text="Email           :")
        self.email_input = Entry(self.window, width=30)
        email_label.grid(column=0, row=2, sticky="W")
        self.email_input.grid(column=1, row=2, sticky="W")

        # Password Input
        password_label = Label(self.window, text="Password    :")
        self.password_input = Entry(self.window, width=30, show="*")
        password_label.grid(column=0, row=3, sticky="W")
        self.password_input.grid(column=1, row=3, sticky="W")
        
        # user account configuration submit button
        submit_button = Button(self.window, text="Submit", command=self.__login_action)
        submit_button.grid(column=1, row=4, sticky="E")

    def __login_action(self):
        # Get User Input
        username = self.username_input.get()
        email = self.email_input.get()
        password = self.password_input.get()
        

    def run(self):
        self.__login_page
        self.window.mainloop()

a = GUI()
a.login_page()
a.run()