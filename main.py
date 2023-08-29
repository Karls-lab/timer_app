# main.py
from controller import controller
from model import model
from view import view
import tkinter as tk

class App():
    def __init__(self):
        main_model = model.TimerModel()
        main_controller = controller.TimerController(main_model, None)
        main_view = view.TimerView(main_controller)
        main_controller.view = main_view

        main_controller.view.mainloop()

if __name__ == "__main__":
    app = App()
