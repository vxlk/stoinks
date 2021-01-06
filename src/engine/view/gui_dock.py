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

        # settings
        #Add Background colour to white
        self.graph_widget.setBackground('w')
        # Add Title
        self.graph_widget.setTitle("Historical", color="b", size="30pt")
        # Add Axis Labels
        styles = {"color": "#f00", "font-size": "20px"}
        self.graph_widget.setLabel("left", "Price", **styles)
        self.graph_widget.setLabel("bottom", "Num Days", **styles)
        #Add legend
        self.graph_widget.addLegend()
        #Add grid
        self.graph_widget.showGrid(x=True, y=True)

        # todo: support different views
        x_axis_high = self._history['High']
        x_axis_low = self._history['Low']

        y_axis_high = []
        y_axis_low = []

        counter_high = 1
        for date in x_axis_high:
            counter_high +=1
            y_axis_high.append(counter_high)
        counter_low = 1
        for date in x_axis_low:
            counter_low +=1
            y_axis_low.append(counter_low)

        self.plot(x_axis_high, y_axis_high, 'High', 'r')
        self.plot(x_axis_low, y_axis_low, 'Low', 'b')

    def plot(self, x, y, plotname, color):
        pen = pyqtgraph.mkPen(color=color)
        self.graph_widget.plot(x, y, name=plotname, pen=pen)

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