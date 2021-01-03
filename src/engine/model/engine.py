from PyQt5.QtCore import *
from PyQt5.QtGui import *

import threading

from util.logger import *

# The driver for the whole project ... this will generate
# premade script text for the input console with all the
# right imports, it also handles an event queue - which
# will take functions for the app to execute
class Engine(QObject):
    def __init__(self):
        super().__init__()
        self.event_queue = {} # this dont work yet, my python is too bad
        self.console = None
        threading.Timer(1.0, self.on_idle).start()

        self.init_strings = {"from model.engine import *"}

    def connectConsole(self, console):
        self.console = console
        if self.console == None:
            raise Exception("Engine does not have access to the console")
        # send console a bunch of imports
        for cmd in self.init_strings:
            # self.add(cmd)
            self.add_event(self.add, [cmd])

    def on_idle(self):
        for event in self.event_queue:
            logger.Log("Running function: " + event.__name__)
            event(*self.event_queue[event])
        self.event_queue = []

    def add(self, str_cmd):
        self.console.insert_input_text(str_cmd)
        logger.Log("Running code: " + str(str_cmd))
        self.console._run_source(str_cmd)
        enterEvent = QKeyEvent(QEvent.KeyPress, Qt.Key_Return, Qt.NoModifier)
        #QCoreApplication.postEvent(self.console, enterEvent)
        self.console._handle_enter_key(enterEvent)

    # does not work yet
    def add_event(self, func, args = None):
        if func in self.event_queue:
            on_idle() # clear the queue    
        self.event_queue[func] = args

engine = Engine()