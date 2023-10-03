#!/usr/bin/python3
# main.py
from controller import controller
from model import model
from view import view
import tkinter as tk

class App():
    def __init__(self):
        """Initialize the app"""
        main_model = model.TimerModel()
        main_controller = controller.TimerController(main_model, None)
        main_view = view.TimerView(main_controller)
        main_controller.view = main_view

        """Save time when closing the app"""
        main_controller.view.protocol("WM_DELETE_WINDOW", main_controller.stop_timer)

        """Start the app"""
        main_controller.view.mainloop()

if __name__ == "__main__":
    app = App()
