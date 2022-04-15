# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ayz.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt,QAbstractTableModel
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QApplication, qApp, QTableView

from finalPCui import Ui_pant_coat_form
from FinalSk import Ui_ShalwarQameez
from orderslist import Ui_OrdersEntry
import pandas as pd
import sys
import subprocess
from listdel import Ui_Dialog
import time


class Ui_MainWindow(object):

    def open_pant_coat(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_pant_coat_form()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()


    def open_suit(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ShalwarQameez()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()

    def actionAdd(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_OrdersEntry()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()

    def actiondelete(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(486, 240)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(24)
        sizePolicy.setVerticalStretch(24)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(486, 0))
        MainWindow.setMaximumSize(QtCore.QSize(486, 16777215))
        MainWindow.setMouseTracking(True)
        MainWindow.setTabletTracking(True)
        MainWindow.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        MainWindow.setAcceptDrops(True)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("image: url(:/test/Downloads/WhatsApp Image 2021-08-15 at 13.22.07.jpeg);")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        MainWindow.setAnimated(False)
        MainWindow.setDocumentMode(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        MainWindow.setWindowIcon(QtGui.QIcon("icon.jpg"))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("color: rgb(255, 255, 255);")
        self.centralwidget.setObjectName("centralwidget")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setEnabled(True)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 486, 22))
        self.menuBar.setTabletTracking(True)
        self.menuBar.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.menuBar.setAutoFillBackground(False)
        self.menuBar.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.menuBar.setDefaultUp(False)
        self.menuBar.setNativeMenuBar(False)
        self.menuBar.setObjectName("menuBar")
        self.menuNew = QtWidgets.QMenu(self.menuBar)
        self.menuNew.setAutoFillBackground(False)
        self.menuNew.setStyleSheet("image: url(:/test/Downloads/11qnZ2RCZML._SX331_BO1,204,203,200_.jpg);\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"background-color: rgb(255, 255, 255);")
        self.menuNew.setSeparatorsCollapsible(True)
        self.menuNew.setToolTipsVisible(True)
        self.menuNew.setObjectName("menuNew")
        self.menuNew_Entry = QtWidgets.QMenu(self.menuNew)
        self.menuNew_Entry.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menuNew_Entry.setAutoFillBackground(False)
        self.menuNew_Entry.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"color: rgb(0, 0, 0);")
        self.menuNew_Entry.setTearOffEnabled(False)
        self.menuNew_Entry.setObjectName("menuNew_Entry")
        self.menuSearch = QtWidgets.QMenu(self.menuNew)
        self.menuSearch.setObjectName("menuSearch")
        self.menuOrders_List = QtWidgets.QMenu(self.menuNew)
        self.menuOrders_List.setObjectName("menuOrders_List")
        self.menuDelete = QtWidgets.QMenu(self.menuNew)
        self.menuDelete.setObjectName("menuDelete")

        MainWindow.setMenuBar(self.menuBar)
        self.actionSearch = QtWidgets.QAction(MainWindow)
        self.actionSearch.setObjectName("actionSearch")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionPant_Coat = QtWidgets.QAction(MainWindow)
        self.actionPant_Coat.setObjectName("actionPant_Coat")
        self.actionSuit = QtWidgets.QAction(MainWindow)
        self.actionSuit.setObjectName("actionSuit")
        self.actionPant_Coat_2 = QtWidgets.QAction(MainWindow)
        self.actionPant_Coat_2.setCheckable(False)
        self.actionPant_Coat_2.setObjectName("actionPant_Coat_2")
        self.actionPant_Coat_Size_Sheet = QtWidgets.QAction(MainWindow)
        self.actionPant_Coat_Size_Sheet.setObjectName("actionPant_Coat_Size_Sheet")
        self.actionSuit_Size_Sheet = QtWidgets.QAction(MainWindow)
        self.actionSuit_Size_Sheet.setObjectName("actionSuit_Size_Sheet")
        self.exit_btn = QtWidgets.QAction(MainWindow)
        self.exit_btn.setCheckable(False)
        self.exit_btn.setObjectName("exit_btn")



        self.menuNew.addAction(self.menuOrders_List.menuAction())
        self.actionOrders_List = QtWidgets.QAction(MainWindow)
        self.actionOrders_List.setObjectName("actionOrders_List")
        self.menuOrders_List.addAction("&Add", self.actionAdd)

        self.menuOrders_List.addAction("&Delete", self.actiondelete)
        self.menuOrders_List.addAction("&Show", self.actionshow)
        
        #backendFunction
        action = QAction("&Pant Coat", self.actionPant_Coat_2)
        action.triggered.connect(self.open_pant_coat)
        self.menuNew_Entry.addAction(action)
        #backendFunction
        acti = QAction('&Suit', self.actionSuit)
        acti.triggered.connect(self.open_suit)
        self.menuNew_Entry.addAction(acti)
        #backendFunction
        size_act = QAction('&Pant Coat Sizes', self.actionPant_Coat_Size_Sheet)
        size_act.triggered.connect(self.pantcoatsize)
        self.menuSearch.addAction(size_act)
        #backendFunction
        size_act1 = QAction('&Suit Sizes', self.actionPant_Coat_Size_Sheet)
        size_act1.triggered.connect(self.suitsize)
        self.menuSearch.addAction(size_act1)
        #backendFunction
        self.menuNew.addAction(self.menuNew_Entry.menuAction())
        self.menuNew.addSeparator()
        self.menuNew.addAction(self.menuSearch.menuAction())

        self.menuNew.addSeparator()
       # self.menuNew.addAction(self.actionOrders_List)
        self.menuNew.addSeparator()
        ##backendFunction
        exit_action = QAction("&Exit",self.exit_btn)
        exit_action.triggered.connect(self.ex)
        self.menuNew.addAction(exit_action)
        ##backendFunction
        self.menuNew.addSeparator()
        ##backendFunction
        self.menuBar.addAction(self.menuNew.menuAction())


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AYZ"))
        self.menuNew.setTitle(_translate("MainWindow", "Menu"))
        self.menuNew_Entry.setTitle(_translate("MainWindow", "New Entry"))
        self.menuSearch.setTitle(_translate("MainWindow", "Search"))
        self.menuDelete.setTitle(_translate("MainWindow", "Delete"))
        self.actionSearch.setText(_translate("MainWindow", "Search "))
        self.actionDelete.setText(_translate("MainWindow", "Delete"))
        self.actionPant_Coat.setText(_translate("MainWindow", "Pant Coat"))
        self.actionSuit.setText(_translate("MainWindow", "Suit"))
        self.actionPant_Coat_2.setText(_translate("MainWindow", "Pant Coat"))
        #self.actionPant_Coat_Size_Sheet.setText(_translate("MainWindow", "Pant Coat Size Sheet"))
        self.actionSuit_Size_Sheet.setText(_translate("MainWindow", "Suit Size Sheet"))
        #self.actionPant_Coat_Size_Sheet_2.setText(_translate("MainWindow", "Pant Coat Size Sheet"))
        self.exit_btn.setText(_translate("MainWindow", "Exit"))
        #self.actionSuit_Size_Sheet_2.setText(_translate("MainWindow", "Suit Size Sheet"))
        #self.actionOrders_List.setText(_translate("MainWindow", "Orders List"))
        self.menuOrders_List.setTitle(_translate("MainWindow", "Orders List"))


    def ex(self):
        qApp.quit()

    def pantcoatsize(self):
        path = r'E:\Pant Coat Sizes'
        sys.path.append(path)
        subprocess.Popen('explorer "E:\Pant Coat Sizes"')


    def suitsize(self):
        path = r'E:\Shalwar Qamez Sizes'
        sys.path.append(path)
        subprocess.Popen('explorer "E:\Shalwar Qamez Sizes"')



    def actionshow(self):
        import HalaTable as HT







if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())