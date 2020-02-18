from PyQt5 import QtWidgets
# PYQT5 QTextEdit, QDialog, QPushButton, QRadioButton, QGridLayout

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt

import re


class Find(QtWidgets.QDialog):
    
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)

        self.parent = parent

        self.lastStart = 0

        self.initUI()

    def initUI(self):
        # Button to search the document for something
        findButton = QtWidgets.QPushButton('Find', self)
        findButton.clicked.connect(self.find)

        # Button to replace the last finding
        replaceButton = QtWidgets.QPushButton('Replace', self)
        replaceButton.clicked.connect(self.replace)

        # Button to remove all findings
        allButton = QtWidgets.QPushButton('Replace all', self)
        allButton.clicked.connect(self.replaceAll)

        # Normal mode - radio button
        self.normalRadio = QtWidgets.QRadioButton('Normal', self)
        self.normalRadio.toggled.connect(self.normalMode)

        # Regular Expression Mode - radio button
        self.regexRadio = QtWidgets.QRadioButton('RegEx', self)
        self.regexRadio.toggled.connect(self.regexMode)

        # The field into which to type the query
        self.findField = QtWidgets.QTextEdit(self)
        self.findField.resize(250, 50)

        # The field into which to type the text to replace the
        # queried text
        self.replaceField = QtWidgets.QTextEdit(self)
        self.replaceField.resize(250, 50)

        optionsLabel = QtWidgets.QLabel('Options: ', self)

        # Case Sensitivity option
        self.caseSens = QtWidgets.QCheckBox('Case sensitive', self)

        # Whole Words option
        self.wholeWords = QtWidgets.QCheckBox('Whole words', self)

        # Layout the objects on the screen
        layout = QtWidgets.QGridLayout()

        # layout (widget, x, y, rows, columns)
        layout.addWidget(self.findField, 1, 0, 1, 4)
        layout.addWidget(self.normalRadio, 2, 2)
        layout.addWidget(self.regexRadio, 2, 3)
        layout.addWidget(findButton, 2, 0, 1, 2)

        layout.addWidget(self.replaceField, 3, 0, 1, 4)
        layout.addWidget(replaceButton, 4, 0, 1, 2)
        layout.addWidget(allButton, 4, 2, 1, 2)

        # Add some spacing
        spacer = QtWidgets.QWidget(self)

        spacer.setFixedSize(0, 10)

        layout.addWidget(spacer, 5, 0)

        layout.addWidget(optionsLabel, 6, 0)
        layout.addWidget(self.caseSens, 6, 1)
        layout.addWidget(self.wholeWords, 6, 2)

        self.setGeometry(300, 300, 360, 250)
        self.setWindowTitle('Find and Replace')
        self.setLayout(layout)

        # By default the normal mode is activated
        self.normalRadio.setChecked(True)

    def find(self):
        pass

    def replace(self):
        pass

    def replaceAll(self):
        pass

    def normalMode(self):
        pass

    def regexMode(self):
        pass