import datetime
import os

from PyQt6.QtWidgets import QPlainTextEdit


class Log(QPlainTextEdit):

    def __init__(self, use_log_file=True):
        super().__init__()

        self.ulf = use_log_file

        self.level_colors = {'DEBUG': 'Green',
                             'ERROR': 'Red',
                             'INFO': 'Gray'}

        if self.ulf:
            if not os.path.exists('logs/'):
                os.mkdir('logs/')
            now = datetime.datetime.now().strftime("./logs/bSIGN-%y_%m_%d-%H-%M-%S")
            self.log_file = os.path.join(os.getcwd(), '{}.log'.format(now))

        self.setReadOnly(True)

    def log(self, msg, level='DEBUG'):
        if self.ulf:
            with open(self.log_file, 'a+') as f:
                f.write('{} :: {} :: {}\n'.format(datetime.datetime.now(), level, msg))
        font_color = self.level_colors.get(level, '')
        self.appendHtml('<font color={}>{} ></font> {}\n'.format(font_color, level, msg))
        self.verticalScrollBar().setValue(self.verticalScrollBar().maximum())
