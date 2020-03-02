# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'configDialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(450, 200)
        Dialog.setMinimumSize(QtCore.QSize(450, 200))
        Dialog.setMaximumSize(QtCore.QSize(450, 200))
        Dialog.setFocusPolicy(QtCore.Qt.NoFocus)
        self.labelHeading = QtWidgets.QLabel(Dialog)
        self.labelHeading.setGeometry(QtCore.QRect(30, 20, 211, 41))
        self.labelHeading.setObjectName("labelHeading")
        self.pushButtonSave = QtWidgets.QPushButton(Dialog)
        self.pushButtonSave.setGeometry(QtCore.QRect(200, 140, 101, 31))
        self.pushButtonSave.setBaseSize(QtCore.QSize(60, 30))
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.pushButtonClose = QtWidgets.QPushButton(Dialog)
        self.pushButtonClose.setGeometry(QtCore.QRect(320, 140, 91, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonClose.sizePolicy().hasHeightForWidth())
        self.pushButtonClose.setSizePolicy(sizePolicy)
        self.pushButtonClose.setObjectName("pushButtonClose")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(60, 80, 339, 27))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelCurrency = QtWidgets.QLabel(self.widget)
        self.labelCurrency.setObjectName("labelCurrency")
        self.horizontalLayout.addWidget(self.labelCurrency)
        self.comboBoxCurrency = QtWidgets.QComboBox(self.widget)
        self.comboBoxCurrency.setObjectName("comboBoxCurrency")
        self.comboBoxCurrency.addItem("")
        self.comboBoxCurrency.addItem("")
        self.comboBoxCurrency.addItem("")
        self.horizontalLayout.addWidget(self.comboBoxCurrency)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelHeading.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Configure Settings</span></p></body></html>"))
        self.pushButtonSave.setText(_translate("Dialog", "Save"))
        self.pushButtonClose.setText(_translate("Dialog", "Close"))
        self.labelCurrency.setText(_translate("Dialog", "Default Reference Currency  "))
        self.comboBoxCurrency.setItemText(0, _translate("Dialog", "USD"))
        self.comboBoxCurrency.setItemText(1, _translate("Dialog", "PHP"))
        self.comboBoxCurrency.setItemText(2, _translate("Dialog", "IDR"))
