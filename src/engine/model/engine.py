from PyQt5.QtCore import *
from PyQt5.QtGui import *

import threading

from util.logger import *
from view.console import *
from model.timed_event import TimedEvent
from model.portfolio import *

# The driver for the whole project ... this will generate
# premade script text for the input console with all the
# right imports, it also handles an event queue - which
# will take functions for the app to execute
class Engine(QObject):
    def __init__(self):
        super().__init__()
        self.event_queue = {} # this dont work yet, my python is too bad
        self.console = None
        self.debug_console = None
        self.portfolio = Portfolio()

        #my design decision here is to decouple gui elements, but couple the finance element
        self.finance_scrape_event = TimedEvent("Scrape Yahoo", 5.0, self.portfolio.update)
        self.code_runner = TimedEvent("Run Python", 1.0, self.on_idle)
        self.debug_console_update = None # can be added later if the user wants this

        self.init_strings = {"from model.engine import *"}

    def connectConsole(self, console):
        self.console = console
        if self.console == None:
            raise Exception("Engine does not have access to the console")
        # send console a bunch of imports
        for cmd in self.init_strings:
            # self.add(cmd)
            self.add_event(self.add, [cmd])

    def connectDebugConsole(self, console):
        self.debug_console = console
        if self.debug_console == None:
            raise Exception("Engine does not have access to the debug console")
        self.debug_console_update = TimedEvent("Update Debug Console", 1.0, self.debug_console.on_idle)

    def on_idle(self):
        for event in self.event_queue:
            event(*self.event_queue[event])
        self.event_queue = []

    def add(self, str_cmd):
        self.console.insert_input_text(str_cmd)
        self.console._run_source(str_cmd)
        enterEvent = QKeyEvent(QEvent.KeyPress, Qt.Key_Return, Qt.NoModifier)
        #QCoreApplication.postEvent(self.console, enterEvent)
        self.console._handle_enter_key(enterEvent)

    # does not work yet
    def add_event(self, func, args = None):
        if func in self.event_queue:
            on_idle() # clear the queue    
        self.event_queue[func] = args

    def stop(self):
        self.finance_scrape_event.stop()
        self.code_runner.stop()
        self.debug_console_update.stop()

engine = Engine()