import tkinter as tk
from tkinter import ttk

from frames.TargetListFrame import TargetListFrame
from frames.TextAreaFrame import TextAreaFrame

class MainFrame(ttk.Frame):
    def __init__(self):
        super().__init__()
        self.targetListFrame = TargetListFrame()
        self.targetListFrame.pack(side="left", expand=True, fill="both")
        
        self.textAreaFrame = TextAreaFrame()
        self.textAreaFrame.pack(side="left", expand=True, fill="both")
        self.textarea = self.textAreaFrame.textarea

    def getTargetListFrame(self):
        return self.targetListFrame
    
    def getChildren(self):
        self.winfo_children