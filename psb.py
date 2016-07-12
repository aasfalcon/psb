#!/usr/bin/python

import sys
from os.path import expanduser

from PyQt5.QtWidgets import QApplication
from lib.window import Window

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else expanduser('~')
    app = QApplication(sys.argv)
    window = Window(directory = path)
    window.open()
    sys.exit(app.exec_())
