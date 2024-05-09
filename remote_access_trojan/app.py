import tkinter as tk
from tkinter import ttk

from frames.MainFrame import MainFrame
from frames.TargetListFrame import TargetListFrame
from frames.TextAreaFrame import TextAreaFrame

class App(tk.Tk):
    def __init__(self, title, size):
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(*size)

        self.add_heading()
        self.mainframe = MainFrame()
        self.mainframe.pack(expand=True, fill="both")

        # self.mainloop()
    def add_heading(self):
        heading = ttk.Label(self, text="Epic Server Handler", font=("Courier", 35), background="antiquewhite4", justify=tk.CENTER, anchor="center")
        heading.pack(fill="both", ipady=10)
    
    def updateTextArea(self, text):
        textarea = self.mainframe.textarea
        textarea.insert(tk.END, text)
    
    def updateTargetList(self, target_num, address, name, conn, addr):
        self.targetList = self.mainframe.getTargetListFrame()
        self.targetList.add_client(
            {
                "num": target_num,
                "addr": address,
                "name": name,
                "conn-object": conn,
                "addr-object": addr
            }
        )