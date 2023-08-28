# main.py
from controller import CalculatorController
from model import model
from view import view
import tkinter as tk

class App():
    def __init__(self):
        main_model = model.CalculatorModel()
        main_controller = CalculatorController.CalculatorController(main_model, None)
        main_view = view.CalculatorView(main_controller)
        main_controller.view = main_view

        main_controller.view.mainloop()

if __name__ == "__main__":
    app = App()
