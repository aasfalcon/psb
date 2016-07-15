#!/usr/bin/python

import sys
import os.path
import subprocess

from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon

from main.settings import config
from main.player import Player
from main.window import Window


class Application(QApplication):
    __player = None
    __window = None


    def __init__(self):
        super(Application, self).__init__(sys.argv)
        self.__fixIconTheme()
        self.__player = Player(config['main']['client_name'])

        directory = os.path.expanduser('~')

        if len(sys.argv) > 1:
           directory = sys.argv[1]

        self.__window = Window(directory, self.__player)


    def __fixIconTheme(self):
        name = QIcon.themeName()

        if name == 'hicolor':
            command = ['gsettings',
                'get',
                'org.gnome.desktop.interface',
                'icon-theme'
            ]

            try:
                process = subprocess.Popen(command,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)
                name = process.stdout.readline().decode('utf-8').strip(" \n'")
            except Exception:
                name = config['main']['fallback_icon_theme']

        QIcon.setThemeName(name)


    def exec_(self):
        try:
            self.__player.connect(['system:playback_1', 'system:playback_2'])
            self.__player.start()
            self.__window.exec_()
        finally:
            self.__player.stop()
            self.__player.disconnect()

        return 0


if __name__ == "__main__":
    app = Application()
    sys.exit(app.exec_())
