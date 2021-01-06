from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pyqtgraph
from model.engine import *
import pandas

class finance_graph_widget(QWidget):
    def __init__(self, parent, str_stock_name):
        super().__init__(parent)
        self.graph_widget = pyqtgraph.PlotWidget(self)
        self.graph_widget.setMinimumSize(parent.width() / 2, parent.height() / 2)
        self.graph_widget.show()

        self._history = engine.portfolio.yfinance_wrapper.history(str_stock_name)
        print(self._history)
        print(type(self._history))
        print(self._history.columns)
        x_axis = self._history['High']
        y_axis = self._history['Low']

        print("X AXIS::")
        print(x_axis)
        print("Y AXIS::")
        print(y_axis)

        #x_axis = [1,2,3]
        #y_axis = [1,2,3]
        self.graph_widget.plot(x_axis, y_axis)

class finance_tab_widget(QWidget):
    def __init__(self, str_stock_name):
        super().__init__()
        self.grid = QGridLayout(self)
        self.graph = finance_graph_widget(self, str_stock_name)
        self.grid.addWidget(self.graph)
        ##self.setCentralWidget(graph)

class finance_tab_container(QTabWidget):
    def __init__(self):
        super().__init__()
        self.tab_to_index_map = {}
        index = 0
        for stock in engine.portfolio.stocks():
            self.create_tab(index, stock)
            index += 1

    def create_tab(self, index, stock):
        self.tab_to_index_map[stock] = index
        tab = finance_tab_widget(stock)
        self.addTab(tab, stock)
        self.tabBar().setTabTextColor(index, Qt.black)