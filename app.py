'''
DQ1 Battle Simulator - App
'''

from view import View
from controller import Controller
from model import model


if __name__ == "__main__":
    view = View()
    controller = Controller(model, view)
    controller.view.mainloop()
