from tkinter import *
from tkinter import filedialog
import os
import json
from bananalog.banana import Banana
import numpy as np

class GUI():

    def __init__(self):
        self.logger = Banana()
        self.logger.type_color = {
            "Error": 'Red',
            "Success":'Green',
            "Warning": 'Yellow'
        }

        self.window = Tk()
        self.title = "Easy Git"

        # Set windows title name
        self.window.title(self.title)
        self.logger.log("GUI Initalize", "Success")
        self.working_dir = None
        self.is_git_dir = False
        self.sync = False
        self.repo_name = None
        
    def __login_page(self):
        self.logger.log("Starting...Login Page", "Success")
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
        self.window.mainloop()

    def __login_action(self):
        # Get User Input
        self.username = self.username_input.get()
        self.email = self.email_input.get()
        password = self.password_input.get()

        # login
        os.system(f'git config --global user.name "{self.username}"')
        os.system(f'git config --global user.email "{self.email}"')
        os.system(f'git config --global user.password "{password}')

        # Edit user.json
        self.user_json["n_run"] += 1
        self.user_json["username"] = self.username
        self.user_json["email"] = self.email
        self.user_json["password"] = password

        with open("git_resouces/user.json", 'w') as fp:
            json.dump(self.user_json, fp)

        self.logger.log(f"User saved username : {self.username}, email : {self.email}", "Success")
        self.window.destroy()
    def __repo_config_page(self):
        select_working_dir_text = Label(self.window, text="Please select working directory")
        select_working_dir_text.grid(row=0, columnspan=3, sticky="W")
        
        # Folder Selection
        working_dir_text = Label(self.window, text="Working Directory : ")
        working_dir_text.grid(row=1, column=0, sticky="W")
        self.working_dir_entry = Entry(self.window, width=40)
        self.working_dir_entry.grid(row=1, column=1, sticky="W")
        select_dir_button = Button(self.window, text="select directory", command=self.__get_folder)
        select_dir_button.grid(row=1, column=2)

        # Git repo
        git_repo_text = Label(self.window, text="Working Git Repo  :")
        git_repo_text.grid(row=2, column=0, sticky="W")
        self.git_repo_entry = Entry(self.window, width=40)
        
            
        self.git_repo_entry.grid(row=2, column=1, sticky="W")
        self.git_repo_clone = Button(self.window, text="Clone", command=self.__git_clone)
        self.git_repo_clone.grid(row=2, column=2, sticky="nswe")

        self.commit_entry = Entry(self.window, width=30)
        self.commit_entry.insert(0, 'Commit Message...')
        self.commit_entry.bind('<FocusIn>', self.__commit_focus_IN)
        self.commit_entry.bind('<FocusOut>', self.__commit_focus_OUT)
        self.commit_entry.config(fg='grey')
        self.commit_entry.grid(row=3, columnspan=2, sticky="nswe")
        
        self.sync_button = Button(self.window, text="Sync", command=self.__sync)
        self.sync_button.grid(row=3, column=2, sticky="nswe")
        
        

        self.window.mainloop()

    def __get_folder(self):
        self.working_dir = filedialog.askdirectory()
        self.working_dir_entry.insert(0, self.working_dir)
        
        # Change Dir
        os.chdir(self.working_dir_entry.get())

        self.is_git_dir = self.__git_check()
        if self.is_git_dir is True:
            self.git_repo_entry.insert(0, os.popen('git remote get-url origin').read())
            # self.git_repo_clone.config(state="disable")
            self.repo_url = self.git_repo_entry.get()[0:-1]
            self.logger.log(f"Found Git Repository : {self.repo_url}", "Success")
            self.logger.log("Disabling Clone function", "Warning")
            self.repo_name = self.repo_url.split('/')[-1].split('.')[0]

        
    
    def __git_check(self):
        if os.popen('git status').read() == 'fatal: not a git repository (or any of the parent directories): .git':
            return False
        else:
            return True

    def __git_clone(self):
        self.repo_url = self.git_repo_entry.get()
        self.logger.log(f"Start Cloning repository {self.repo_url}")
        cloning_message = os.popen(f"git clone {self.repo_url} .").read()
        if "fetal" in cloning_message:
            self.logger.log("Cloning Failed", "Error")
        else:
            self.logger.log("Cloning Success", "Success")
        self.repo_name = self.repo_url.split('/')[-1].split('.')[0]

    def __sync(self):
        self.commit_message = self.commit_entry.get()
        print(self.commit_message)
        if self.commit_message == 'Commit Message...':
            self.commit_message = "add commited file"
        self.logger.log(f"Syncing commit  : {self.commit_message}")
        os.popen('git add .')
        
        self.commit_run_console = os.popen(f'git commit -a -m "{self.commit_message}"').read().splitlines()
        for action in self.commit_run_console[1:]:
            self.logger.log(f"changed {action}", "Warning")
        self.logger.log("start pushing")
        os.system('del .git\index.lock')
        push_run_console = os.popen(f'git push').read()
        '''
        if 'done' in push_run_console:
            self.logger.log("Pushed Complete", "Success")
        else:
            self.logger.log("Pushed Failed", "Error")
        '''

        self.commit_entry.delete(0, "end")
        self.commit_entry.insert(0, '')

    def __commit_focus_IN(self, event):
        if self.commit_entry.get() == 'Commit Message...':
            self.commit_entry.delete(0, "end")
            self.commit_entry.insert(0, '')
            self.commit_entry.config(fg='black')
           
    
    def __commit_focus_OUT(self, event):
        if self.commit_entry.get() == '':
            self.commit_entry.insert(0, 'Commit Message...')
            self.commit_entry.config(fg='grey')
            
        

    def run(self):
        self.__login_page()
        self.__init__()
        self.__repo_config_page()
        
