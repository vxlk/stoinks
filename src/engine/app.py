import sys
from threading import Thread

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from pyqtconsole.console import PythonConsole

from view.console import Console
from view.gui_dock import *
from util.logger import *
from model.engine import *

# clear logs
logger.ClearLogs()

# make Qapp
app = QApplication([])

app.setApplicationName("Stoinks Alpha")
window = QMainWindow()

console = PythonConsole()
logConsole = Console()
# stop debug console from resizing
logConsoleFrame = QScrollArea()
logConsoleFrame.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
logConsoleFrame.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
logConsoleFrame.setWidgetResizable(True)
logConsoleFrame.setWidget(logConsole)
#temp for now
gui = finance_tab_container()

consoleContainer = QDockWidget("Input")
consoleContainer.setAllowedAreas(Qt.LeftDockWidgetArea) 
consoleContainer.setWidget(console)

logConsoleContainer = QDockWidget("Output")
logConsoleContainer.setAllowedAreas(Qt.RightDockWidgetArea)
logConsoleContainer.setWidget(logConsoleFrame)

guiContainer = QDockWidget("GUI View")
guiContainer.setAllowedAreas(Qt.TopDockWidgetArea)
guiContainer.setWidget(gui)

window.addDockWidget(Qt.LeftDockWidgetArea, consoleContainer)
window.addDockWidget(Qt.RightDockWidgetArea, logConsoleContainer)
window.addDockWidget(Qt.TopDockWidgetArea, guiContainer)

#console.show() add dock widget calls show on its widget i think
console.eval_in_thread() # let the input terminal go

# make an engine
engine.connectConsole(console)
engine.connectDebugConsole(logConsole)

# Force the style to be the same on all OSs:
app.setStyle("Fusion")

# Now use a palette to switch to dark colors:
palette = QPalette()
palette.setColor(QPalette.Window, QColor(53, 53, 53))
palette.setColor(QPalette.WindowText, Qt.white)

app.setPalette(palette)

window.setMinimumSize(820, 800)
window.show()
app.exec_()
# sys.exit(app.exec_())

engine.stop()