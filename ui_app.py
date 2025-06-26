# UI of the App

import tkinter as tk
from tkinter import ttk

class CalculatorApp:
    def __init__(self):
        self.root = root
        self.root.title("Calculator")

        self.logic = CalculatorLogic()
        self.result_var = tk.StringVar

        self.create_widgets()
        self.setup_grid()
        self.bind_keys()

        self.root.resizable(False, False)

    def create_widgets(self):
        self.result_entry = ttk.Entry(self.root, 
        textvariable=self.result_var, font=("Helvetica", 24), justify="right")

        self.result_entry.grid(row = 0, column = 0, columnspan = 4, sticky ="nsew")

        style = ttk.Style()
        style.theme_use("default")
        style.configure("TButton", font =("Helvetica", 16), width=10, height=4)

    
    def setup_grid(self):
    
    def bind_keys(self):