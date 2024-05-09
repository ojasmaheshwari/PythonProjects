import tkinter as tk
from tkinter import ttk

class TargetListFrame(ttk.Frame):
    def __init__(self):
        super().__init__()
        self.clients = []
        self.add_widgets()
    
    def add_widgets(self):
        label = ttk.Label(self, text="Connected targets will appear here", background="antiquewhite")
        label.pack(fill="both", padx=10, pady=10)
    
    def add_client(self, client):
        clientButton = ttk.Button(self, text=f"Client #{client['num']}: {client['addr']}, {client['name']}", command=lambda: IndividualTargetWorker(client))
        clientButton.pack(fill="both", padx=10, pady=5)