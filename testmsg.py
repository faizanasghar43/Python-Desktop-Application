# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'listdel.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import qApp

from PyQt5.QtGui import QIntValidator
import pandas as pd

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Delete Customer")
        Dialog.resize(240, 107)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 20, 141, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(150, 20, 61, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(60, 80, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 80, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")



        self.onlyInt = QIntValidator()
        self.lineEdit.setValidator(self.onlyInt)
        var = self.lineEdit.text()
        self.onlyInt = QIntValidator()
        self.lineEdit.setValidator(self.onlyInt)
        self.pushButton.clicked.connect(lambda:self.listdel(var))
        self.pushButton_2.clicked.connect(self.ex)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enter Customer No"))
        self.pushButton.setText(_translate("Dialog", "Delete"))
        self.pushButton_2.setText(_translate("Dialog", "Quit"))

    def listdel(self, a):
        data=pd.read_csv("Dummy File XYZ 11.csv")
        a = self.lineEdit.text()
        a = int(a)

        index = data.index[data['Customer No'] == a].tolist()
        var1 = data['Customer No'].values[index]
        var2 = data['Booking'].values[index]
        var3 = data['Delivery'].values[index]
        var4 = data['Quantity'].values[index]
        var5 = data['Advance'].values[index]
        var6 = data['Total Rs'].values[index]
        var7 = data['Urgent'].values[index]
        pd.DataFrame = data.drop(data.index[index])
        pd.DataFrame.to_csv("Dummy File XYZ 11.csv", index=False)
        print(var1)
        print(var2)
        print(var3)
        print(var4)
        print(var5)
        print(var6)
        print(var7)

        addData = ({
                    "Customer No":var1,
                    "Booking": var2,
                    "Delivery":var3,
                    "Quantity":var4,
                    "Advance":var5,
                    "Total Rs":var6,
                    "Urgent":var7
        })
        data = pd.read_csv("Orders Completed.csv")
        data = pd.concat([data,addData], ignore_index = True, axis = 0)
        data.to_csv('Orders Completed.csv', mode='a', header=False)


    def ex(self):
        qApp.quit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
