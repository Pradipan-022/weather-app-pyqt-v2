import sys
from PyQt5.QtWidgets import QApplication
from weather_app.ui.main_window import MainWindow
import os


import sys
from PyQt5.QtWidgets import QApplication
from weather_app.ui.main_window import MainWindow


def load_styles(app):
    with open("weather_app/ui/styles/base.qss") as f:
        app.setStyleSheet(f.read())

    with open("weather_app/ui/styles/main.qss") as f:
        app.setStyleSheet(app.styleSheet() + f.read())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    load_styles(app)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

