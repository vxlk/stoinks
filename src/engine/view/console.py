from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from util.settings import *
from util.logger import *
from model.timed_event import TimedEvent

# a simple debugging console for now, eventually i wanna do some kind of intellisense
# or something more useful, for now this will prove invaulable for debugging speeds

class Console(QLabel):
    def __init__(self):
        super().__init__()
        self.text = ""
        self.printQueue = []
        
        self.setStyleSheet("QLabel { background-color : black; color : green; }")

        #one thread will be adding to the print queue, 
        #and another will be iterating through it.
        #better make sure one doesn't interfere with the other.
        # TODO: REDO THIS LATER ... WERE GONNA NEED LOCKS ON THIS THREAD IDK IF THIS IS RIGHT
        # self.printQueueLock = threading.Lock()
        

   #check for new messages every five milliseconds
    def on_idle(self):
        #with self.printQueueLock:
        # check settings file
        log_file = open(logger.FilePath(), "r")
        text = log_file.read()
        self.printQueue.append(text)
        for msg in self.printQueue:
            self.text += msg
        self.printQueue = []
        log_file.close()
        # todo: not running on gui thread and Qt is FURIOUS ...
        # self.moveToThread(QThread.currentThread())
        self.setText(self.text)
        self.text = ""
    #print msg to the console
    def show(self, msg, sep="\n"):
        #with self.printQueueLock:
        self.printQueue.append(str(msg) + sep)