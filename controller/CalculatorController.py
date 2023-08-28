# calculator_controller.py
from model import model 
from view import view 

class CalculatorController():
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.history_index = -1

     
    def calculate_expression(self, expression):
        """Clear the display, calculate the expression, and display the result"""
        self.view.display.delete(1.0, "end-1c")
        self.model.calculate(expression)
        self.view.display.insert("end-1c", self.model.result)


    def get_history(self, index):
        """Get the history of expressions"""
        try:
            display_expression = self.model.expression_history[self.history_index]
            self.history_index += index
        except IndexError:
            display_expression = ""
        self.view.display.delete(1.0, "end-1c")
        self.view.display.insert("end-1c", display_expression)
