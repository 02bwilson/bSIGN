import argparse

from PyQt6.QtWidgets import QApplication

from mainwindow import bSIGN_MW

if __name__ == "__main__":
    app = QApplication([])
    window = bSIGN_MW()
    window.show()
    app.exec()