from PyQt5.QtCore import *

# The driver for the whole project ... this will generate
# premade script text for the input console with all the
# right imports, it also handles an event queue - which
# will take functions for the app to execute
class Engine(QObject):
    __init__(self):
    eventQueue = []