from build import gui
import tkinter.messagebox as msgbox
from tkinter import END
from hashlib import sha256

def fetchFields():
    return (gui.entry_1.get(), gui.entry_2.get())

def emptyFields():
    gui.entry_1.delete(0, END)
    gui.entry_2.delete(0, END)

def encrypt(data: str):
    return sha256(data.encode('utf-8')).hexdigest()

def saveToFile(data: str, file: str):
    file = open(file, 'a')
    file.write(data+"\n")
    file.close()

def onCreateAccount():
    username, password = fetchFields()
    if len(username) == 0 or len(password) == 0:
        msgbox.showerror("Empty fields", "Username or password is empty")
        return
    en_username = encrypt(username)
    en_password = encrypt(password)

    saveToFile(f"{en_username} {en_password}", 'database.txt')
    emptyFields()
    msgbox.showinfo("Registration complete", "You have been safely registered!")

def fetchData():
    file = open('database.txt', 'r')
    data = {}
    for line in file:
        data[line.split()[0]] = line.split()[1]
    file.close()
    return data

def onLogin():
    username, password = fetchFields()
    if len(username) == 0 or len(password) == 0:
        msgbox.showerror("Empty fields", "Username or password is empty")
        return
    data = fetchData()
    usernames = data.keys()
    en_username = encrypt(username)
    en_password = encrypt(password)
    if en_username in usernames:
        if en_password == data[en_username]:
            msgbox.showinfo("Success", f"Logged in as {username}")
        else:
            msgbox.showerror("Error", "Password is not correct")
    else:
        msgbox.showerror("Does not exist", "User does not exist")

def main():
    gui.window.mainloop()

if __name__ == '__main__':
    main()
