from Controller import Controller
from View import View

"""
The main function, from here all the program stars.
Initializing the controller object
Initializing the view object
Inserting to the view the controller and then starting the view.
"""


def main():
    c = Controller()
    v = View(c)
    v.start()


"""
If running this file the main function will be executed.
"""
if __name__ == '__main__':
    main()
