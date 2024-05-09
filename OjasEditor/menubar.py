import tkinter as tk
from customtkinter import set_appearance_mode

def menubar(window, command_dict: dict):
    menubar = tk.Menu(window)
    file = tk.Menu(menubar, tearoff = 0) 
    menubar.add_cascade(label ='File', menu = file) 
    file.add_command(label ='New File', command = command_dict.get('new_file')) 
    file.add_command(label ='Open...', command = command_dict.get('open_file')) 
    file.add_command(label ='Save As', command = command_dict.get('save_as')) 
    file.add_command(label ='Save', command = command_dict.get('save')) 
    file.add_separator() 
    file.add_command(label ='Exit', command = window.destroy)

    edit = tk.Menu(menubar, tearoff = 0) 
    menubar.add_cascade(label ='Edit', menu = edit) 
    edit.add_command(label ='Cut', command = None) 
    edit.add_command(label ='Copy', command = None) 
    edit.add_command(label ='Paste', command = None) 
    edit.add_command(label ='Select All', command = None) 
    edit.add_separator() 
    edit.add_command(label ='Find...', command = None) 
    edit.add_command(label ='Find again', command = None)

    view = tk.Menu(menubar, tearoff = 0) 
    menubar.add_cascade(label ='View', menu = view) 
    view.add_command(label ='Change appearance', command = command_dict.get('change_appearance'))

    help_ = tk.Menu(menubar, tearoff = 0) 
    menubar.add_cascade(label ='Help', menu = help_) 
    help_.add_command(label ='Ojas Editor Help', command = None) 
    help_.add_command(label ='Demo', command = None) 
    help_.add_separator() 
    help_.add_command(label ='About Ojas Editor', command = None) 

    window.bind(
        '<Control-s>', lambda x : command_dict.get('save')()
    )

    window.config(menu=menubar)
