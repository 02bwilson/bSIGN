from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow
import qdarktheme

from mainwidget import bSIGN_W


class bSIGN_MW(QMainWindow):

    def __init__(self):
        super().__init__()

        # Setup the GUI
        qdarktheme.setup_theme('dark')
        self.setWindowTitle("bSIGN")
        self.setWindowIcon(QIcon('icon.png'))
        self.setFixedSize(300, 300)
        self.widget = bSIGN_W()
        self.setCentralWidget(self.widget)
