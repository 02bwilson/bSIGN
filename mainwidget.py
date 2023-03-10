from PyQt6.QtWidgets import QWidget, QGridLayout, QFileDialog, QPushButton, QComboBox
from PyQt6.QtCore import Qt

from pathlib import Path

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa

from log import Log
from signer import bSIGN_Signer


class bSIGN_W(QWidget):

    def __init__(self):
        super().__init__()

        self.layout = None
        self.log = None
        self.file_select_button = None
        self.sign_button = None
        self.start_button = None
        self.sign_type_combobox = None
        self.cur_files = None
        self.signer = None

        self.cur_files = []

        # Setup Layout
        self.layout = QGridLayout()

        # Setup the GUI
        self.log = Log()
        self.signer = bSIGN_Signer(self)
        self.log.log("Setting up GUI...")
        self.file_select_button = QPushButton("Select File(s)")
        self.file_select_button.pressed.connect(self.file_handler)
        self.sign_type_combobox = QComboBox()
        self.sign_type_combobox.addItems(['SHA256', 'SHA384', 'SHA512'])
        self.sign_type_combobox.currentIndexChanged.connect(
            lambda: self.log.log('Changed hash type to {}'.format(self.sign_type_combobox.currentText())))
        self.start_button = QPushButton("Sign")
        self.start_button.pressed.connect(self.sign_handler)

        # Add GUI elements
        self.layout.setAlignment(Qt.AlignmentFlag.AlignBottom)
        self.layout.addWidget(self.log, 0, 0, alignment=Qt.AlignmentFlag.AlignBottom)
        self.layout.addWidget(self.file_select_button, 1, 0, alignment=Qt.AlignmentFlag.AlignBottom)
        self.layout.addWidget(self.sign_type_combobox, 2, 0, alignment=Qt.AlignmentFlag.AlignBottom)
        self.layout.addWidget(self.start_button, 3, 0, alignment=Qt.AlignmentFlag.AlignBottom)

        self.setLayout(self.layout)
        self.log.log("GUI Setup Completed!")

    def file_handler(self):
        # Handle file dialog
        dir = str(Path.home())
        dialog = QFileDialog()
        files = dialog.getOpenFileNames(self, 'Open file', dir)
        if self.cur_files not in [[''], [], None]:
            self.log.log("Removed previous files.")
        self.cur_files = files[0]
        for file in self.cur_files:
            self.log.log("Added {}".format(file))

    def sign_handler(self):
        self.log.log("Signing...")
        if self.cur_files in [[], [''], None]:
            self.log.log("No files selected.", level="ERROR")
        else:
            self.signer.cur_files = self.cur_files
            self.signer.sign_files()
