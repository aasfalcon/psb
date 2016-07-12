#!/usr/bin/python

from PySide import QtGui
from PySide.QtGui import QFileDialog, QDialogButtonBox, QApplication
import os.path
import sys
from lib.player import Player

class Dialog(QFileDialog):
	def __init__(self, parent = None):
		super(Dialog, self).__init__(parent, 'Preview sounds')
		
		self.player = Player("psb")
		self.player.connect(['system:playback_1', 'system:playback_2'])
		self.player.start()
		
		if self.acceptMode() == QFileDialog.AcceptOpen:
			button_box = self.findChildren(QDialogButtonBox)[0]
			
		if button_box:
			self.copyButton = button_box.button(QDialogButtonBox.Open)
			self.copyButton.setText('C&opy path')
			closeButton = button_box.button(QDialogButtonBox.Cancel)
			closeButton.setText("Close")
			closeButton.setVisible(False)
			
		self.setFilters([
			'All supported (*.wav *.aif *.aiff *.snd)',
			'Wave files (*.wav)',
			'AIFF files (*.aif *.aiff)',
			'SND files (*.snd)',
		])

		self.currentChanged.connect(self.fileSelectionChanged)
		
		
	def accept(self):
		path = str(self.selectedFiles()[0])
		clipboard = QApplication.clipboard()
		clipboard.setText(path)
		self.copyButton.setEnabled(False)

		
	def fileSelectionChanged(self, filename):
		path = str(filename)
		
		if os.path.isfile(path):
			self.player.play(path)


if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	dialog = Dialog()
	dialog.open()
	sys.exit(app.exec_())
