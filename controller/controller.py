# calculator_controller.py
from model import model 
from view import view 

class TimerController():
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def get_saved_time(self):
        self.model.get_saved_time()
        self.view.display.delete("1.0", "end")
        self.view.display.insert("1.0", self.model.get_time(), "center")
     
    def set_30_min(self):
        self.model.set_30_min()
        self.view.display.delete("1.0", "end")
        self.view.display.insert("1.0", self.model.get_time(), "center") 

    def start_timer(self):
        self.model.start_timer()
        self.view.display.delete("1.0", "end")
        self.view.display.insert("5.0", self.model.get_time(), "center")

    def get_time(self):
        return self.model.get_time()
    
    def calculate_time_left(self):
        return self.model.calculate_time_left()
    
    def check_time(self):
        return self.model.check_time()
    
    def stop_timer(self):
        self.model.stop_timer()

    def reset_timer(self):
        self.model.reset_timer()
        self.view.display.delete("1.0", "end")
        self.view.display.insert("1.0", self.model.get_time(), "center")