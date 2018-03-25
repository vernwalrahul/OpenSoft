# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Interface.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(917, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.uploadButton = QtGui.QPushButton(self.centralwidget)
        self.uploadButton.setGeometry(QtCore.QRect(270, 60, 99, 27))
        self.uploadButton.setObjectName(_fromUtf8("uploadButton"))
        self.submitButton = QtGui.QPushButton(self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(400, 60, 99, 27))
        self.submitButton.setObjectName(_fromUtf8("submitButton"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 130, 68, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(62, 60, 171, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 180, 111, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.DD = QtGui.QTextBrowser(self.centralwidget)
        self.DD.setGeometry(QtCore.QRect(230, 180, 251, 31))
        self.DD.setObjectName(_fromUtf8("DD"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 230, 101, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.PD = QtGui.QTextBrowser(self.centralwidget)
        self.PD.setGeometry(QtCore.QRect(230, 220, 256, 31))
        self.PD.setObjectName(_fromUtf8("PD"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 370, 151, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.PD1 = QtGui.QTextBrowser(self.centralwidget)
        self.PD1.setGeometry(QtCore.QRect(230, 270, 256, 71))
        self.PD1.setObjectName(_fromUtf8("PD1"))
        self.PM = QtGui.QTextBrowser(self.centralwidget)
        self.PM.setGeometry(QtCore.QRect(230, 360, 256, 131))
        self.PM.setObjectName(_fromUtf8("PM"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(530, 180, 101, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.TA = QtGui.QTextBrowser(self.centralwidget)
        self.TA.setGeometry(QtCore.QRect(640, 170, 256, 181))
        self.TA.setObjectName(_fromUtf8("TA"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 917, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.uploadButton.setText(_translate("MainWindow", "Upload", None))
        self.submitButton.setText(_translate("MainWindow", "Submit", None))
        self.label.setText(_translate("MainWindow", "Output", None))
        self.label_2.setText(_translate("MainWindow", "Doctor\'s Details", None))
        self.label_3.setText(_translate("MainWindow", "Patient Details", None))
        self.label_4.setText(_translate("MainWindow", "Prescribed Medicines", None))
        self.label_5.setText(_translate("MainWindow", "Tests / Advice", None))

