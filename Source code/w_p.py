# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'w_p.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DC_anz(object):
    def setupUi(self, DC_anz):
        DC_anz.setObjectName("DC_anz")
        DC_anz.resize(728, 565)
        self.groupBox = QtWidgets.QGroupBox(DC_anz)
        self.groupBox.setGeometry(QtCore.QRect(480, 150, 231, 141))
        self.groupBox.setObjectName("groupBox")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(120, 30, 93, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 30, 93, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(70, 80, 93, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.groupBox_2 = QtWidgets.QGroupBox(DC_anz)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 20, 441, 261))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 421, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_3 = QtWidgets.QGroupBox(DC_anz)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 280, 441, 261))
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_6.setGeometry(QtCore.QRect(0, 0, 441, 261))
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.groupBox_6)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 20, 421, 231))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_5 = QtWidgets.QGroupBox(DC_anz)
        self.groupBox_5.setGeometry(QtCore.QRect(480, 30, 111, 71))
        self.groupBox_5.setObjectName("groupBox_5")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 91, 22))
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(DC_anz)
        self.label.setGeometry(QtCore.QRect(490, 300, 211, 16))
        self.label.setObjectName("label")

        self.retranslateUi(DC_anz)
        QtCore.QMetaObject.connectSlotsByName(DC_anz)

    def retranslateUi(self, DC_anz):
        _translate = QtCore.QCoreApplication.translate
        DC_anz.setWindowTitle(_translate("DC_anz", "DC_anz"))
        self.groupBox.setTitle(_translate("DC_anz", "DC_anz"))
        self.pushButton.setText(_translate("DC_anz", "Mapping"))
        self.pushButton_2.setText(_translate("DC_anz", "Reset"))
        self.pushButton_3.setText(_translate("DC_anz", "Stop_scan"))
        self.groupBox_2.setTitle(_translate("DC_anz", "Wave"))
        self.groupBox_3.setTitle(_translate("DC_anz", "DC of time interval"))
        self.groupBox_6.setTitle(_translate("DC_anz", "DC of time interval"))
        self.groupBox_5.setTitle(_translate("DC_anz", "Time interval"))
        self.lineEdit.setText(_translate("DC_anz", "1"))
        self.label.setText(_translate("DC_anz", "Please press Reset before mapping"))