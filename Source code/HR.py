# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HR.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_HR(object):
    def setupUi(self, Form_HR):
        Form_HR.setObjectName("Form_HR")
        Form_HR.resize(781, 593)
        Form_HR.setFocusPolicy(QtCore.Qt.NoFocus)
        self.groupBox = QtWidgets.QGroupBox(Form_HR)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 571, 541))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 551, 511))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(Form_HR)
        self.groupBox_2.setGeometry(QtCore.QRect(610, 190, 141, 71))
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(20, 30, 113, 22))
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Form_HR)
        QtCore.QMetaObject.connectSlotsByName(Form_HR)

    def retranslateUi(self, Form_HR):
        _translate = QtCore.QCoreApplication.translate
        Form_HR.setWindowTitle(_translate("Form_HR", "Heart Rate"))
        self.groupBox.setTitle(_translate("Form_HR", "Peaks"))
        self.groupBox_2.setTitle(_translate("Form_HR", "Heart Rate(times/min)"))
