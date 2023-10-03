import tkinter as tk
import tkinter.font as font
from controller import controller
from plyer import notification
from playsound import playsound
import os


class TimerView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Karl's Timer")
        self.geometry("600x400")
        self.larger_font = font.Font(size=20)


        """Display and Buttons"""
        self.display = tk.Text(self, height=1)
        self.display.tag_configure("center", justify='center')
        self.min_30_button = tk.Button(
            self, text='30 min', font = self.larger_font, command=lambda: self.controller.set_30_min()) 
        self.set_custom_time_button = tk.Button(
            self, text='Custom', font = self.larger_font, command=lambda: self.controller.set_custom_time())
        self.start_button = tk.Button(
            self, text='Start', font = self.larger_font, command=lambda: self.controller.start_timer()) 
        self.stop_button= tk.Button(
            self, text='Stop', font = self.larger_font, command=lambda: self.controller.stop_timer())
        self.reset_button = tk.Button(
            self, text='Reset', font = self.larger_font, command=lambda: self.controller.reset_timer())

        """Grid layout and options"""
        # Row 0
        self.display.grid(row=0, column=0, columnspan=3, padx=40, pady= 40, sticky="nsew")
        self.larger_display_font = font.Font(size=40) 
        self.display.configure(font=self.larger_display_font)

        # Row 1
        self.min_30_button.grid(row=1, column=1, columnspan=1, sticky="nsew")
        self.set_custom_time_button.grid(row=1, column=2, columnspan=1, sticky="nsew")

        # Row 2
        self.start_button.grid(row=2, column=0, sticky="nsew")
        self.stop_button.grid(row=2, column=1, sticky="nsew")
        self.reset_button.grid(row=2, column=2, sticky="nsew")
        
        # Adjust row and column weights
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.update_clock()

        
    def update_clock(self):
        self.display.delete("1.0", "end")
        self.display.insert("1.5", self.controller.get_time(), "center")
        self.display.after(1000, self.update_clock)

        # Check if timer is done, send notification and play sound
        if self.controller.check_time():
            self.controller.stop_timer()
            self.controller.reset_timer()
            notification.notify("Timer Done!")
            root_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
            playsound(os.path.join(root_path,'sounds/oversimplified-alarm-clock-113180.mp3'))


        
        

