from model.finance_wrapper import yfinance_module
from util.logger import *
from threading import *

class TimedEvent():
    def __init__(self, event_name, interval, function, *args, **kwargs):
        self.event_name = event_name
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()
        self.debug_log_functions = {}

    def _run(self):
        self.is_running = False
        if self.event_name in self.debug_log_functions:
            logger.Log("Starting " + self.function.__name__ + " after " + str(self.interval) + " seconds")
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False