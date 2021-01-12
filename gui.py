from tkinter import *
import os
import json
from bananalog.banana import Banana

class GUI():

    def __init__(self):
        self.logger = Banana()
        self.logger.type_color = {
            "Error": 'Red',
            "Success":'Green'
        }

        self.window = Tk()
        self.title = "Easy Git"

        # Set windows title name
        self.window.title(self.title)

    def __login_page(self):
        # Load User.json for default input
        
        with open("git_resouces/user.json") as json_file:
            self.user_json = json.load(json_file)

        insert_default_text = lambda varname, key : varname.insert(0, self.user_json[key]) if self.user_json[key] != None else False 


        # Welcome text at the head of the program
        greeting_label = Label(self.window, text="Welcome to Easy Git please login")
        greeting_label.grid(row=0, columnspan=2)

        # Username Input 
        username_label = Label(self.window, text="Username   : ")
        self.username_input = Entry(self.window, width=30)
        insert_default_text(self.username_input, "username")
        username_label.grid(column=0, row=1, sticky="W")
        self.username_input.grid(column=1, row=1, sticky="W")

        # Email Input
        email_label = Label(self.window, text="Email           :")
        self.email_input = Entry(self.window, width=30)
        insert_default_text(self.email_input, "email")
        email_label.grid(column=0, row=2, sticky="W")
        self.email_input.grid(column=1, row=2, sticky="W")

        # Password Input
        password_label = Label(self.window, text="Password    :")
        self.password_input = Entry(self.window, width=30, show="*")
        insert_default_text(self.password_input, "password")
        password_label.grid(column=0, row=3, sticky="W")
        self.password_input.grid(column=1, row=3, sticky="W")
        
        # user account configuration submit button
        submit_button = Button(self.window, text="Submit", command=self.__login_action)
        submit_button.grid(column=1, row=4, sticky="E")

    def __login_action(self):
        # Get User Input
        self.username = self.username_input.get()
        self.email = self.email_input.get()
        password = self.password_input.get()

        # login
        os.system(f'git config --global user.name "{username}"')
        os.system(f'git config --global user.email "{email}"')
        os.system(f'git config --global user.password "{password}')

        # Edit user.json
        self.user_json["n_run"] += 1
        self.user_json["username"] = self.username
        self.user_json["email"] = self.email
        self.user_json["password"] = password

        with open("git_resouces/user.json", 'w') as fp:
            json.dump(self.user_json, fp)

        self.logger.log(f"User saved username : {self.username}, email : {self.email}", "Success")
        


    def run(self):
        self.__login_page()
        self.window.mainloop()

a = GUI()

a.run()