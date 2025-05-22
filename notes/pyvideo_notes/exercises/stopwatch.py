import sys 
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QPushButton, QVBoxLayout, QHBoxLayout)

from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QFont, QFontDatabase


class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0)
        self.time_label = QLabel("00:00:00.00", self)
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)
        self.timer = QTimer(self)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("IKdigital Stopwatch")
        self.setGeometry(100, 100, 300, 100)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label, alignment=Qt.AlignCenter)

        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)

        hbox = QHBoxLayout()

        
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        vbox.addLayout(hbox)

        self.setStyleSheet("background-color: #1a7689;")
        self.time_label.setStyleSheet(
            "font-size: 50px; background-color: #155e6b;"
            "border-radius: 10px; padding: 10px;"
        )
        self.start_button.setStyleSheet(
            "background-color: #155e6b; color: white;"
            "border-radius: 10px; padding: 10px;"
            "border-color: #ffcc00; border-width: 2px;"
            "border-style: solid;"
        )
        self.stop_button.setStyleSheet(
            "background-color: #155e6b; color: white;"
            "border-radius: 10px; padding: 10px;"
            "border-color: #ffcc00; border-width: 2px;"
            "border-style: solid;"
        )
        self.reset_button.setStyleSheet(
            "background-color: #155e6b; color: white;"
            "border-radius: 10px; padding: 10px;"
            "border-color: #ffcc00; border-width: 2px;"
            "border-style: solid;"
        )

        font_id = QFontDatabase.addApplicationFont("DS-DIGIT.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family, 150)

        self.time_label.setFont(my_font)

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)

        self.time_label.setFixedHeight(100)
        self.time_label.setMinimumWidth(self.width())
        self.time_label.setMaximumWidth(self.width())
        self.time_label.setSizePolicy(self.time_label.sizePolicy().horizontalPolicy(), self.time_label.sizePolicy().verticalPolicy())


        
    def start(self):
        self.timer.start(10)
    
    def stop(self):
        self.timer.stop()
        
    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.format_time(self.time))
        

    def format_time(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"

    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))

    



if __name__ == '__main__':
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())