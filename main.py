# Main file
from ui_app import CalculatorApp
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()