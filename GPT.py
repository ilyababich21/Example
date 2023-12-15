import sys

from PyQt6.QtCharts import QLineSeries, QChartView, QChart, QAbstractAxis
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QMainWindow, QPushButton, QLineEdit, QLabel, QWidget, QGridLayout, QVBoxLayout, QApplication
from pymodbus.client import ModbusTcpClient
QAbstractAxis
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.client = ModbusTcpClient(host='127.0.0.1', port=502)

        self.label_temperature = QLabel()
        self.label_humidity = QLabel()

        self.button_read = QPushButton('Read')
        self.button_clear = QPushButton('Clear')

        self.line_edit_temperature = QLineEdit()
        self.line_edit_humidity = QLineEdit()

        self.chart = QChart()
        self.chart_view = QChartView(self.chart)

        self.grid_layout = QGridLayout()
        self.vertical_layout = QVBoxLayout()

        self.grid_layout.addWidget(self.label_temperature, 0, 0)
        self.grid_layout.addWidget(self.line_edit_temperature, 0, 1)
        self.grid_layout.addWidget(self.label_humidity, 1, 0)
        self.grid_layout.addWidget(self.line_edit_humidity, 1, 1)
        self.grid_layout.addWidget(self.button_read, 2, 0)
        self.grid_layout.addWidget(self.button_clear, 2, 1)
        self.vertical_layout.addLayout(self.grid_layout)
        self.vertical_layout.addWidget(self.chart_view)

        self.setCentralWidget(QWidget(self))
        self.centralWidget().setLayout(self.vertical_layout)

        self.button_read.clicked.connect(self.read_data)
        self.button_clear.clicked.connect(self.clear_data)

        self.chart.addSeries(QLineSeries())
        self.chart.setTitle('Temperature and Humidity')
        self.chart.createDefaultAxes()
        self.chart.setAxisX('Time')
        self.chart.setyAxisTitle('Value')
        self.chart.setAutoFillBackground(True)
        self.chart.setBackgroundBrush(QColor(255, 255, 255))
        self.chart.setAutoRefresh(True)

        self.chart.xAxis().setRange(0, 100)
        self.chart.yAxis().setRange(0, 100)

        self.start_reading()

        self.show()

    def read_data(self):
        try:
            temperature = self.client.read_holding_registers(0, 1)
            humidity = self.client.read_holding_registers(1, 1)

            self.line_edit_temperature.setText(str(temperature[0]))
            self.line_edit_humidity.setText(str(humidity[0]))

            self.chart.series()[0].append(self.chart.series()[0].count(), temperature[0])
            self.chart.series()[0].append(self.chart.series()[0].count(), humidity[0])
        except Exception as e:
            print(e)

    def clear_data(self):
        self.chart.series()[0].clear()

    def start_reading(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.read_data)
        self.timer.start(1000)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_window = MainWindow()

    sys.exit(app.exec_())