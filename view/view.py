import tkinter as tk
import tkinter.font as font
from controller import CalculatorController

class CalculatorView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Calculator")
        self.geometry("500x800")

        self.larger_font = font.Font(size=20)


        """Display and Buttons"""
        self.display = tk.Text(self, height=2)
        self.clear_button = tk.Button(self, text='Clear', font = self.larger_font, command=lambda: self.display.delete(1.0, tk.END))
        self.down_history_button = tk.Button(self, text='History', font = self.larger_font, command=lambda: self.controller.get_history(-1))
        self.times_button = tk.Button(self, text='*', font = self.larger_font, command=lambda: self.display.insert(tk.END, '*'))
        self.divide_button = tk.Button(self, text='/', font = self.larger_font, command=lambda: self.display.insert(tk.END, '/'))
        self.add_button = tk.Button(self, text='+', font = self.larger_font, command=lambda: self.display.insert(tk.END, '+'))
        self.subtract_button = tk.Button(self, text='-', font = self.larger_font, command=lambda: self.display.insert(tk.END, '-'))
        self.button7 = tk.Button(self, text='7', font= self.larger_font, command=lambda: self.display.insert(tk.END, '7'))
        self.button8 = tk.Button(self, text='8', font = self.larger_font, command=lambda: self.display.insert(tk.END, '8'))
        self.button9 = tk.Button(self, text='9', font = self.larger_font, command=lambda: self.display.insert(tk.END, '9'))
        self.button4 = tk.Button(self, text='4', font = self.larger_font, command=lambda: self.display.insert(tk.END, '4'))
        self.button5 = tk.Button(self, text='5', font = self.larger_font, command=lambda: self.display.insert(tk.END, '5'))
        self.button6 = tk.Button(self, text='6', font = self.larger_font, command=lambda: self.display.insert(tk.END, '6'))
        self.button1 = tk.Button(self, text='1', font = self.larger_font, command=lambda: self.display.insert(tk.END, '1'))
        self.button2 = tk.Button(self, text='2', font = self.larger_font, command=lambda: self.display.insert(tk.END, '2'))
        self.button3 = tk.Button(self, text='3', font = self.larger_font, command=lambda: self.display.insert(tk.END, '3'))
        self.equals_button = tk.Button(self, text='=', font = self.larger_font, command=lambda: self.calculate())

        """Grid layout and options"""
        # Row 0
        self.display.grid(row=0, column=0, columnspan=4 , sticky="nsew")
        self.larger_display_font = font.Font(size=40) 
        self.display.configure(font=self.larger_display_font)

        # Row 1
        self.clear_button.grid(row=1, column=0, columnspan=2, sticky="nsew")
        self.down_history_button.grid(row=1, column=2, columnspan=2, sticky="nsew")

        # Row 2
        self.times_button.grid(row=2, column=0, sticky="nsew")
        self.divide_button.grid(row=2, column=1, sticky="nsew")
        self.add_button.grid(row=2, column=2, sticky="nsew")
        self.subtract_button.grid(row=2, column=3, sticky="nsew")

        # Row 3
        self.button7.grid(row=3, column=0, sticky="nsew")
        self.button8.grid(row=3, column=1, sticky="nsew")
        self.button9.grid(row=3, column=2, sticky="nsew")
        self.equals_button.grid(row=3, column=3, rowspan=3, sticky="nsew")

        # Row 3
        self.button4.grid(row=4, column=0, sticky="nsew")
        self.button5.grid(row=4, column=1, sticky="nsew")
        self.button6.grid(row=4, column=2, sticky="nsew")

        # Row 4
        self.button1.grid(row=5, column=0, sticky="nsew")
        self.button2.grid(row=5, column=1, sticky="nsew")
        self.button3.grid(row=5, column=2, sticky="nsew")

        # Adjust row and column weights
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)

    def calculate(self):
        str_expression = self.display.get("1.0", "end-1c")
        self.controller.calculate_expression(str_expression)
        

# Note: We're not creating an instance of the CalculatorView class here,
# as it will be done in the main.py script.
