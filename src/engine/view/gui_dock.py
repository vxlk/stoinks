from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from model.engine import *

class finance_tab_widget(QWidget):
    def __init__(self):
        super().__init__()

class finance_tab_container(QTabWidget):
    def __init__(self):
        super().__init__()
        tab_to_index_map = {}
        index = 0
        for stock in engine.portfolio.stocks():
            tab_to_index_map[stock] = index
            tab = finance_tab_widget()
            self.addTab(tab, stock)
            self.tabBar().setTabTextColor(index, Qt.black)
            index += 1