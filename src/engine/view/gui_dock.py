from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pyqtgraph
from model.engine import *
import pandas

class finance_graph_widget_day(QWidget):
    def __init__(self, parent, str_stock_name):
        super().__init__(parent)
        self.graph_widget = pyqtgraph.PlotWidget(self)
        self.graph_widget.setMinimumSize(parent.width() / 2, parent.height() / 2)
        self.graph_widget.show()

        self._history = engine.portfolio.yfinance_wrapper.today(str_stock_name)

        # settings
        #Add Background colour to white
        self.graph_widget.setBackground('w')
        # Add Title
        self.graph_widget.setTitle("Today", color="b", size="30pt")
        # Add Axis Labels
        styles = {"color": "#f00", "font-size": "20px"}
        self.graph_widget.setLabel("left", "Price", **styles)
        self.graph_widget.setLabel("bottom", "5 min intervals", **styles)
        #Add legend
        self.graph_widget.addLegend()
        #Add grid
        self.graph_widget.showGrid(x=True, y=True)

        # todo: support different views
        x_axis_high = []
        x_axis_low = []

        y_axis_high = self._history['High']
        y_axis_low = self._history['Low']

        counter_high = 1
        for date in y_axis_high:
            counter_high +=1
            x_axis_high.append(counter_high)
        counter_low = 1
        for date in y_axis_low:
            counter_low +=1
            x_axis_low.append(counter_low)

        self.plot(x_axis_high, y_axis_high, 'High', 'r')
        self.plot(x_axis_low, y_axis_low, 'Low', 'b')

    def plot(self, x, y, plotname, color):
        pen = pyqtgraph.mkPen(color=color)
        self.graph_widget.plot(x, y, name=plotname, pen=pen)

class finance_graph_widget_hist(QWidget):
    def __init__(self, parent, str_stock_name):
        super().__init__(parent)
        self.graph_widget = pyqtgraph.PlotWidget(self)
        self.graph_widget.setMinimumSize(parent.width() / 2, parent.height() / 2)
        self.graph_widget.show()

        self._history = engine.portfolio.yfinance_wrapper.history(str_stock_name)
       
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
        x_axis_high = []
        x_axis_low = []

        y_axis_high = self._history['High']
        y_axis_low = self._history['Low']

        counter_high = 1
        for date in y_axis_high:
            counter_high +=1
            x_axis_high.append(counter_high)
        counter_low = 1
        for date in y_axis_low:
            counter_low +=1
            x_axis_low.append(counter_low)

        self.plot(x_axis_high, y_axis_high, 'High', 'r')
        self.plot(x_axis_low, y_axis_low, 'Low', 'b')

    def plot(self, x, y, plotname, color):
        pen = pyqtgraph.mkPen(color=color)
        self.graph_widget.plot(x, y, name=plotname, pen=pen)

class finance_tab_widget(QTabWidget):
    def __init__(self, str_stock_name):
        super().__init__()
        # today
        self.grid_day = QVBoxLayout(self)
        self.graph_day = finance_graph_widget_day(self, str_stock_name)
        self.grid_day.addWidget(self.graph_day)

        # todo add this as part of a data layout class!
        self.price_label = QLabel()
        self.price_label.setText(str(engine.portfolio.yfinance_wrapper.price(str_stock_name)))
        font = QFont("Ariel", 34, QFont.Bold)
        self.price_label.setFont(font)
        self.price_label.setStyleSheet("QLabel { background-color : white; color : blue; }")
        self.price_label.setSizePolicy(QSizePolicy.Minimum,
                                       QSizePolicy.Minimum)
        self.grid_day.addWidget(self.price_label)

        self.container_widget_day = QWidget()
        self.container_widget_day.setLayout(self.grid_day)
        self.addTab(self.container_widget_day, 'Today')
        self.tabBar().setTabTextColor(0, Qt.black)

        # historical
        self.grid_hist = QGridLayout(self)
        self.graph_hist = finance_graph_widget_hist(self, str_stock_name)
        self.grid_hist.addWidget(self.graph_hist)
        self.container_widget_hist = QWidget()
        self.container_widget_hist.setLayout(self.grid_hist)
        self.addTab(self.container_widget_hist, 'Historical')
        self.tabBar().setTabTextColor(1, Qt.black)

        #self.grid = QGridLayout(self)
        #self.graph = finance_graph_widget(self, str_stock_name)
        #self.grid.addWidget(self.graph)

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