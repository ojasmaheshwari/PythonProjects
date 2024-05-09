import tkinter as tk
from tkinter import ttk

class TextAreaFrame(ttk.Frame):
    def __init__(self):
        super().__init__()
        self.add_widgets()
    
    def add_widgets(self):
        self.textarea = tk.Text(self, background="white", width=1, state="normal", font=("Courier", 12))
        self.textarea.pack(fill="both", expand=True)

