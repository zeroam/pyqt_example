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
        fontBox = QtWidgets.QFontComboBox(self)
        fontBox.setEditable(False)
        fontBox.currentFontChanged.connect(self.fontFamily)

        fontSize = QtWidgets.QComboBox(self)
        fontSize.setEditable(True)

        # Minimum number of chars displayed
        fontSize.setMinimumContentsLength(3)

        fontSize.activated.connect(self.fontSize)

        # Typical font sizes
        fontSizes = ['6', '7', '8', '9', '10', '11', '12', '13', '14',
                     '15', '16', '18', '20', '22', '24', '26', '28',
                     '32', '36', '40', '44', '48', '54', '60', '66',
                     '72', '80', '88', '96']

        for i in fontSizes:
            fontSize.addItem(i)

        fontColor = QtWidgets.QAction(QtGui.QIcon('icons/font-color.png'), 'Change font color', self)
        fontColor.triggered.connect(self.fontColor)

        backColor = QtWidgets.QAction(QtGui.QIcon('icons/highlight.png'), 'Change background color', self)
        backColor.triggered.connect(self.highlight)

        boldAction = QtWidgets.QAction(QtGui.QIcon('icons/bold.png'), 'Bold', self)
        boldAction.triggered.connect(self.bold)

        italicAction = QtWidgets.QAction(QtGui.QIcon('icons/italic.png'), 'Italic', self)
        italicAction.triggered.connect(self.italic)

        underlAction = QtWidgets.QAction(QtGui.QIcon('icons/underline.png'), 'Underline', self)
        underlAction.triggered.connect(self.underline)

        strikeAction = QtWidgets.QAction(QtGui.QIcon('icons/strike.png'), 'Strike-out', self)
        strikeAction.triggered.connect(self.strike)

        superAction = QtWidgets.QAction(QtGui.QIcon('icons/superscript.png'), 'Superscript', self)
        superAction.triggered.connect(self.superScript)

        subAction = QtWidgets.QAction(QtGui.QIcon('icons/subscript.png'), 'Subscript', self)
        subAction.triggered.connect(self.subScript)

        alignLeft = QtWidgets.QAction(QtGui.QIcon('icons/align-left.png'), 'Align left', self)
        alignLeft.triggered.connect(self.alignLeft)

        alignCenter = QtWidgets.QAction(QtGui.QIcon('icons/align-center.png'), 'Align center', self)
        alignCenter.triggered.connect(self.alignCenter)

        alignRight = QtWidgets.QAction(QtGui.QIcon('icons/align-right.png'), 'Align right', self)
        alignRight.triggered.connect(self.alignRight)

        alignJustify = QtWidgets.QAction(QtGui.QIcon('icons/align-justify.png'), 'Align justify', self)
        alignJustify.triggered.connect(self.alignJustify)

        indentAction = QtWidgets.QAction(QtGui.QIcon('icons/indent.png'), 'Index Area', self)
        indentAction.setShortcut('Ctrl+Tab')
        indentAction.triggered.connect(self.indent)

        dedentAction = QtWidgets.QAction(QtGui.QIcon('icons/dedent.png'), 'Dedent Area', self)
        dedentAction.setShortcut('Shift+Tab')
        dedentAction.triggered.connect(self.dedent)

        self.formatbar = self.addToolBar('Format')

        self.formatbar.addWidget(fontBox)
        self.formatbar.addWidget(fontSize)

        self.formatbar.addSeparator()

        self.formatbar.addAction(fontColor)
        self.formatbar.addAction(backColor)

        self.formatbar.addSeparator()

        self.formatbar.addAction(boldAction)
        self.formatbar.addAction(italicAction)
        self.formatbar.addAction(underlAction)
        self.formatbar.addAction(strikeAction)
        self.formatbar.addAction(superAction)
        self.formatbar.addAction(subAction)

        self.formatbar.addSeparator()

        self.formatbar.addAction(alignLeft)
        self.formatbar.addAction(alignCenter)
        self.formatbar.addAction(alignRight)
        self.formatbar.addAction(alignJustify)

        self.formatbar.addSeparator()

        self.formatbar.addAction(indentAction)
        self.formatbar.addAction(dedentAction)

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

        # Toggling actions for the various bars
        toolbarAction = QtWidgets.QAction('Toggle Toolbar', self)
        toolbarAction.triggered.connect(self.toggleToolbar)

        formatbarAction = QtWidgets.QAction('Toggle Formatbar', self)
        formatbarAction.triggered.connect(self.toggleFormatbar)

        statusbarAction = QtWidgets.QAction('Toggle Statusbar', self)
        statusbarAction.triggered.connect(self.toggleStatusbar)

        view.addAction(toolbarAction)
        view.addAction(formatbarAction)
        view.addAction(statusbarAction)


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

    def fontFamily(self, font):
        self.text.setCurrentFont(font)

    def fontSize(self, fontsize):
        self.text.setFontPointSize(int(fontsize))

    def fontColor(self):
        # Get a color from the text dialog
        color = QtWidgets.QColorDialog.getColor()

        # Set it as the new text color
        self.text.setTextColor(color)

    def highlight(self):
        color = QtWidgets.QColorDialog.getColor()

        self.text.setTextBackgroundColor(color)

    def bold(self):
        if self.text.fontWeight() == QtGui.QFont.Bold:
            self.text.setFontWeight(QtGui.QFont.Normal)
        else:
            self.text.setFontWeight(QtGui.QFont.Bold)

    def italic(self):
        state = self.text.fontItalic()
        
        self.text.setFontItalic(not state)

    def underline(self):
        state = self.text.fontUnderline()

        self.text.setFontUnderline(not state)

    def strike(self):
        # Grab the text's format
        fmt = self.text.currentCharFormat()

        # Set the fontStrkieOut property to its opposite
        fmt.setFontStrikeOut(not fmt.fontStrikeOut())

        # And set the next char format
        self.text.setCurrentCharFormat(fmt)

    def superScript(self):
        # Grab the current format
        fmt = self.text.currentCharFormat()

        # And get the vertical alignment property
        align = fmt.verticalAlignment()

        # Toggle the state
        if align == QtGui.QTextCharFormat.AlignNormal:
            fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignSuperScript)
        else:
            fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignNormal)

        # Set the new format
        self.text.setCurrentCharFormat(fmt)

    def subScript(self):
        # Grab the current format
        fmt = self.text.currentCharFormat()

        # And get the vertical alignment property
        align = fmt.verticalAlignment()

        # Toggle the state
        if align == QtGui.QTextCharFormat.AlignNormal:
            fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignSubScript)
        else:
            fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignNormal)

        # Set the new format
        self.text.setCurrentCharFormat(fmt)

    def alignLeft(self):
        self.text.setAlignment(Qt.AlignLeft)

    def alignRight(self):
        self.text.setAlignment(Qt.AlignRight)

    def alignCenter(self):
        self.text.setAlignment(Qt.AlignCenter)

    def alignJustify(self):
        self.text.setAlignment(Qt.AlignJustify)

    def indent(self):
        # Grab the cursor
        cursor = self.text.textCursor()

        if cursor.hasSelection():
            # Store the current line/block number
            temp = cursor.blockNumber()

            # Move to the selection's last line
            cursor.setPosition(cursor.selectionEnd())

            # Calculate range of selection
            diff = cursor.blockNumber() - temp

            # Iterative over lines
            for n in range(diff + 1):
                # Move to start of each line
                cursor.movePosition(QtGui.QTextCursor.StartOfLine)

                # Insert tabbing
                cursor.insertText('\t')

                # And move back up
                cursor.movePosition(QtGui.QTextCursor.Up)
            
        # If there is no selection, just indent a tab
        else:
            cursor.insertText('\t')

    def dedent(self):
        cursor = self.text.textCursor()

        if cursor.hasSelection():
            # Store the current line/block number
            temp = cursor.blockNumber()

            # Move to the selection's last line
            cursor.setPosition(cursor.selectionEnd())

            # Calculate range of selection
            diff = cursor.blockNumber() - temp

            # Iterate over lines
            for n in range(diff + 1):
                self.handleDedent(cursor)

                # Move up
                cursor.movePosition(QtGui.QTextCursor.Up)

        else:
            self.handleDedent(cursor)

    def handleDedent(self, cursor):
        cursor.movePosition(QtGui.QTextCursor.StartOfLine)

        # Grab the current line
        line = cursor.block().text()

        # If the line starts with a tab character, delete it
        if line.startswith('\t'):
            # Delete next character
            cursor.deleteChar()

        # Otherwise, delete all spaces until a non-space character is met
        else:
            for char in line[:8]:
                if char != ' ':
                    break
                cursor.deleteChar()

    def toggleToolbar(self):
        state = self.toolbar.isVisible()

        # Set the visibility to its inverse
        self.toolbar.setVisible(not state)

    def toggleFormatbar(self):
        state = self.formatbar.isVisible()

        # Set the visibility to its inverse
        self.formatbar.setVisible(not state)

    def toggleStatusbar(self):
        state = self.statusbar.isVisible()

        # Set the visibility to its inverse
        self.statusbar.setVisible(not state)


def main():
    app = QtWidgets.QApplication(sys.argv)

    main = Main()
    main.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
