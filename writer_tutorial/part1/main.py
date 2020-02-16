import sys
from PyQt5 import QtWidgets
from PyQt5 import QtPrintSupport
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt


class Main(QtWidgets.QMainWindow):

    def __init__(self, parent = None):
        QtWidgets.QMainWindow.__init__(self, parent)

        self.filename = ''

        self.initUI()

    def initToolbar(self):

        self.newAction = QtWidgets.QAction(QtGui.QIcon('icons/new.png'), 'New', self)
        self.newAction.setStatusTip('Create a new document from scratch')
        self.newAction.setShortcut('Ctrl+N')
        self.newAction.triggered.connect(self.new)

        self.openAction = QtWidgets.QAction(QtGui.QIcon('icons/open.png'), 'Open file', self)
        self.openAction.setStatusTip('Open existing document')
        self.openAction.setShortcut('Ctrl+O')
        self.openAction.triggered.connect(self.open)

        self.saveAction = QtWidgets.QAction(QtGui.QIcon('icons/save.png'), 'Save', self)
        self.saveAction.setStatusTip('Save document')
        self.saveAction.setShortcut('Ctrl+S')
        self.saveAction.triggered.connect(self.save)

        self.printAction = QtWidgets.QAction(QtGui.QIcon('icons/print.png'), 'Print document', self)
        self.printAction.setStatusTip('Print docuement')
        self.printAction.setShortcut('Ctrl+P')
        self.printAction.triggered.connect(self.printHandler)

        self.previewAction = QtWidgets.QAction(QtGui.QIcon('icons/preview.png'), 'Page view', self)
        self.previewAction.setStatusTip('Preview page before printing')
        self.previewAction.setShortcut('Ctrl+Shift+P')
        self.previewAction.triggered.connect(self.preview)

        self.cutAction = QtWidgets.QAction(QtGui.QIcon('icons/cut.png'), 'Cut to clipboard', self)
        self.cutAction.setStatusTip('Delete and copy text to clipboard')
        self.cutAction.setShortcut('Ctrl+X')
        self.cutAction.triggered.connect(self.text.cut)

        self.copyAction = QtWidgets.QAction(QtGui.QIcon('icons/copy.png'), 'Copy to clipboard', self)
        self.copyAction.setStatusTip('Copy text to clipboard')
        self.copyAction.setShortcut('Ctrl+C')
        self.copyAction.triggered.connect(self.text.copy)

        self.pasteAction = QtWidgets.QAction(QtGui.QIcon('icons/paste.png'), 'Paste from clipboard', self)
        self.pasteAction.setStatusTip('Paste text from clipboard')
        self.pasteAction.setShortcut('Ctrl+V')
        self.pasteAction.triggered.connect(self.text.paste)

        self.undoAction = QtWidgets.QAction(QtGui.QIcon('icons/undo.png'), 'Undo last action', self)
        self.undoAction.setStatusTip('Undo last action')
        self.undoAction.setShortcut('Ctrl+Z')
        self.undoAction.triggered.connect(self.text.undo)

        self.redoAction = QtWidgets.QAction(QtGui.QIcon('icons/redo.png'), 'Redo last undone thing', self)
        self.redoAction.setStatusTip('Redo last undone thing')
        self.redoAction.setShortcut('Ctrl+Y')
        self.redoAction.triggered.connect(self.text.redo)

        bulletAction = QtWidgets.QAction(QtGui.QIcon('icons/bullet.png'), 'Insert bullet List', self)
        bulletAction.setStatusTip('Insert bullet list')
        bulletAction.setShortcut('Ctrl+Shift+B')
        bulletAction.triggered.connect(self.bulletList)

        numberedAction = QtWidgets.QAction(QtGui.QIcon('icons/number.png'), 'Insert numbered List', self)
        numberedAction.setStatusTip('Insert numbered list')
        numberedAction.setShortcut('Ctrl+Shift+L')
        numberedAction.triggered.connect(self.numberList)

        self.toolbar = self.addToolBar('Options')

        self.toolbar.addAction(self.newAction)
        self.toolbar.addAction(self.openAction)
        self.toolbar.addAction(self.saveAction)

        self.toolbar.addSeparator()

        self.toolbar.addAction(self.printAction)
        self.toolbar.addAction(self.previewAction)

        self.toolbar.addSeparator()

        self.toolbar.addAction(self.cutAction)
        self.toolbar.addAction(self.copyAction)
        self.toolbar.addAction(self.pasteAction)
        self.toolbar.addAction(self.undoAction)
        self.toolbar.addAction(self.redoAction)

        self.toolbar.addSeparator()

        self.toolbar.addAction(bulletAction)
        self.toolbar.addAction(numberedAction)

        # Makes the next toolbar appear underneath this one
        self.addToolBarBreak()

    def initFormatbar(self):
        self.formatbar = self.addToolBar('Format')

    def initMenubar(self):
        menubar = self.menuBar()

        file = menubar.addMenu('File')
        edit = menubar.addMenu('Edit')
        view = menubar.addMenu('View')

        file.addAction(self.newAction)
        file.addAction(self.openAction)
        file.addAction(self.saveAction)
        file.addAction(self.printAction)
        file.addAction(self.previewAction)

        edit.addAction(self.undoAction)
        edit.addAction(self.redoAction)
        edit.addAction(self.cutAction)
        edit.addAction(self.copyAction)
        edit.addAction(self.pasteAction)


    def initUI(self):
        self.text = QtWidgets.QTextEdit(self)
        self.setCentralWidget(self.text)

        self.initToolbar()
        self.initFormatbar()
        self.initMenubar()

        # Set the tab stop width to around 33 pixels which is
        # about 8 spaces
        self.text.setTabStopWidth(33)

        # Initialize a statusbar for the window
        self.statusbar = self.statusBar()

        # x and y coordinates on the screen, width, height
        self.setGeometry(100, 100, 1030, 800)

        self.setWindowTitle('Writer')

        self.setWindowIcon(QtGui.QIcon('icons/icon.png'))

    def new(self):
        spawn = Main(self)
        spawn.show()

    def open(self):
        # Get filename and show only .writer files
        # PyQt5 Returns a tuple in PyQt5, we only need the fileanme
        self.filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', '.', '(*.writer)')[0]

        if self.filename:
            with open(self.filename, 'rt') as file:
                self.text.setText(file.read())

    def save(self):
        # Only open dialog if there is no filename yet
        # PyQt5 Returns a tuple in PyQt5, we only need filename
        if not self.filename:
            self.filename = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File')[0]
        
        if self.filename:
            # Append extension if not there yet
            if not self.filename.endswith('.writer'):
                self.filename += '.writer'

            # We just store the contents of the text file along with the
            # format in html, which Qt does in a very nice way for us
            with open(self.filename, 'wt') as file:
                file.write(self.text.toHtml())

            self.changeSaved = True

    def printHandler(self):
        # Open printintg dialog
        dialog = QtPrintSupport.QPrintDialog()

        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.text.document().print_(dialog.printer())

    def preview(self):
        # Open printintg dialog
        preview = QtPrintSupport.QPrintPreviewDialog()

        # If a print is requested, open print dialog
        preview.paintRequested.connect(lambda p: self.text.print_(p))

        preview.exec_()

    def bulletList(self):
        cursor = self.text.textCursor()

        # Insert bulleted list
        cursor.insertList(QtGui.QTextListFormat.ListDisc)

    def numberList(self):
        cursor = self.text.textCursor()

        # Insert list with numbers
        cursor.insertList(QtGui.QTextListFormat.ListDecimal)


def main():
    app = QtWidgets.QApplication(sys.argv)

    main = Main()
    main.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
