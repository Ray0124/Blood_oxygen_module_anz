# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'power.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_power(object):
    def setupUi(self, Form_power):
        Form_power.setObjectName("Form_power")
        Form_power.resize(813, 593)
        Form_power.setFocusPolicy(QtCore.Qt.NoFocus)
        self.groupBox = QtWidgets.QGroupBox(Form_power)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 631, 541))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 611, 51))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 80, 611, 451))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(Form_power)
        self.groupBox_2.setGeometry(QtCore.QRect(650, 190, 141, 71))
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(20, 30, 113, 22))
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Form_power)
        QtCore.QMetaObject.connectSlotsByName(Form_power)

    def retranslateUi(self, Form_power):
        _translate = QtCore.QCoreApplication.translate
        Form_power.setWindowTitle(_translate("Form_power", "Power"))
        self.groupBox.setTitle(_translate("Form_power", "Spectrum power"))
        self.groupBox_2.setTitle(_translate("Form_power", "SNR(db)"))