# UI of the App

import tkinter as tk
from tkinter import ttk
from logic_app import CalculatorLogic
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

        buttons = [
            ("C", 1, 0), ("±", 1, 1), ("%", 1, 2), ("÷", 1, 3),
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("×", 2, 3),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
            ("0", 5, 0, 2), (".", 5, 2), ("=", 5, 3)
        ]

        for button_info in buttons:
            text, row, col = button_info[:3]
            colspan = button_info[3] if len(button_info) > 3 else 1
            button = ttk.Button(
                self.root,
                text=text,
                command=lambda t=text: self.handle_button_click(t),
                style="TButton"
            )
            button.grid(row=row, column=col, columnspan=colspan, sticky="nsew", ipadx=10, ipady=4, padx=5, pady=5)

    
    def setup_grid(self):
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
    
    def bind_keys(self):
        self.root.bind("<Return>", lambda event: self.handle_button_click("="))
        self.root.bind("<BackSpace>", lambda event: self.handle_button_click("C"))
    
    def handle_button_click(self, button_text):
        current = self.result_var.get()
        new_value = self.logic.process_input(current, button_text)
        self.result_var.set(new_value)