from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 500)
        MainWindow.setMinimumSize(QtCore.QSize(400, 500))
        MainWindow.setMaximumSize(QtCore.QSize(400, 500))
        MainWindow.setStyleSheet("background-color: rgb(235, 235, 117);\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 210, 381, 271))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 45))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
                                        "border:0px solid rgb(12, 40, 71);\n"
                                        "    background-color: rgb(2, 173, 225);\n"
                                        "border-radius:10px;\n"
                                        "    color: rgb(227, 227, 227);\n"
                                        "    font: 16pt \"MS Shell Dlg 2\";\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "border:3px solid white;\n"
                                        "\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "background-color: rgb(229, 76, 229);\n"
                                        "}\n"
                                        "")
        self.pushButton_4.setFlat(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 2, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_8.setMinimumSize(QtCore.QSize(0, 45))
        self.pushButton_8.setStyleSheet("QPushButton{\n"
                                        "border:0px solid rgb(12, 40, 71);\n"
                                        "    background-color: rgb(2, 173, 225);\n"
                                        "border-radius:10px;\n"
                                        "    color: rgb(227, 227, 227);\n"
                                        "    font: 16pt \"MS Shell Dlg 2\";\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "border:3px solid white;\n"
                                        "\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "background-color: rgb(229, 76, 229);\n"
                                        "}\n"
                                        "")
        self.pushButton_8.setFlat(False)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 1, 0, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_9.setMinimumSize(QtCore.QSize(0, 45))
        self.pushButton_9.setStyleSheet("QPushButton{\n"
                                        "border:0px solid rgb(12, 40, 71);\n"
                                        "    background-color: rgb(2, 173, 225);\n"
                                        "border-radius:10px;\n"
                                        "    color: rgb(227, 227, 227);\n"
                                        "    font: 16pt \"MS Shell Dlg 2\";\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "border:3px solid white;\n"
                                        "\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "background-color: rgb(229, 76, 229);\n"
                                        "}\n"
                                        "")
        self.pushButton_9.setFlat(False)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 1, 1, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_10.setMinimumSize(QtCore.QSize(0, 45))
        self.pushButton_10.setStyleSheet("QPushButton{\n"
                                         "border:0px solid rgb(12, 40, 71);\n"
                                         "    background-color: rgb(2, 173, 225);\n"
                                         "border-radius:10px;\n"
                                         "    color: rgb(227, 227, 227);\n"
                                         "    font: 16pt \"MS Shell Dlg 2\";\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "border:3px solid white;\n"
                                         "\n"
                                         "}\n"
                                         "QPushButton:pressed{\n"
                                         "background-color: rgb(229, 76, 229);\n"
                                         "}\n"
                                         "")
        self.pushButton_10.setFlat(False)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_10, 0, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 45))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
                                        "border:0px solid rgb(12, 40, 71);\n"
                                        "    background-color: rgb(2, 173, 225);\n"
                                        "border-radius:10px;\n"
                                        "    color: rgb(227, 227, 227);\n"
                                        "    font: 16pt \"MS Shell Dlg 2\";\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "border:3px solid white;\n"
                                        "\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "background-color: rgb(229, 76, 229);\n"
                                        "}\n"
                                        "")
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 3, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setMinimumSize(QtCore.QSize(0, 45))
        self.pushButton_6.setStyleSheet("QPushButton{\n"
                                        "border:0px solid rgb(12, 40, 71);\n"
                                        "    background-color: rgb(2, 173, 225);\n"
                                        "border-radius:10px;\n"
                                        "    color: rgb(227, 227, 227);\n"
                                        "    font: 16pt \"MS Shell Dlg 2\";\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "border:3px solid white;\n"
                                        "\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "background-color: rgb(229, 76, 229);\n"
                                        "}\n"
                                        "")
        self.pushButton_6.setFlat(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 2, 2, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_11.setMinimumSize(QtCore.QSize(0, 45))
        self.pushButton_11.setStyleSheet("QPushButton{\n"
                                         "border:0px solid rgb(12, 40, 71);\n"
                                         "    background-color: rgb(2, 173, 225);\n"
                                         "border-radius:10px;\n"
                                         "    color: rgb(227, 227, 227);\n"
                                         "    font: 16pt \"MS Shell Dlg 2\";\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "border:3px solid white;\n"
                                         "\n"
                                         "}\n"
                                         "QPushButton:pressed{\n"
                                         "background-color: rgb(229, 76, 229);\n"
                                         "}\n"
                                         "")
        self.pushButton_11.setFlat(False)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_11, 2, 3, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_12.setMinimumSize(QtCore.QSize(0, 45))
        self.pushButton_12.setStyleSheet("QPushButton{\n"
                                         "border:0px solid rgb(12, 40, 71);\n"
                                         "    background-color: rgb(2, 173, 225);\n"
                                         "border-radius:10px;\n"
                                         "    color: rgb(227, 227, 227);\n"
                                         "    font: 16pt \"MS Shell Dlg 2\";\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "border:3px solid white;\n"
                                         "\n"
                                         "}\n"
                                         "QPushButton:pressed{\n"
                                         "background-color: rgb(229, 76, 229);\n"
                                         "}\n"
                                         "")
        self.pushButton_12.setFlat(False)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout.addWidget(self.pushButton_12, 3, 3, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_13.setMinimumSize(QtCore.QSize(0, 45))
        self.pushButton_13.setStyleSheet("QPushButton{\n"
                                         "border:0px solid rgb(12, 40, 71);\n"
                                         "    background-color: rgb(2, 173, 225);\n"
                                         "border-radius:10px;\n"
                                         "    color: rgb(227, 227, 227);\n"
                                         "    font: 16pt \"MS Shell Dlg 2\";\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "border:3px solid white;\n"
                                         "\n"
                                         "}\n"
                                         "QPushButton:pressed{\n"
                                         "background-color: rgb(229, 76, 229);\n"
                                         "}\n"
                                         "")
        self.pushButton_13.setFlat(False)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout.addWidget(self.pushButton_13, 2, 1, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setMinimumSize(QtCore.QSize(0, 45))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
                                        "border:0px solid rgb(12, 40, 71);\n"
                                        "    background-color: rgb(2, 173, 225);\n"
                                        "border-radius:10px;\n"
                                        "    color: rgb(227, 227, 227);\n"
                                        "    font: 16pt \"MS Shell Dlg 2\";\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "border:3px solid white;\n"
                                        "\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "background-color: rgb(229, 76, 229);\n"
                                        "}\n"
                                        "")
        self.pushButton_5.setFlat(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 3, 2, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_14.setMinimumSize(QtCore.QSize(0, 45))
        self.pushButton_14.setStyleSheet("QPushButton{\n"
                                         "border:0px solid rgb(12, 40, 71);\n"
                                         "    background-color: rgb(2, 173, 225);\n"
                                         "border-radius:10px;\n"
                                         "    color: rgb(227, 227, 227);\n"
                                         "    font: 16pt \"MS Shell Dlg 2\";\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "border:3px solid white;\n"
                                         "\n"
                                         "}\n"
                                         "QPushButton:pressed{\n"
                                         "background-color: rgb(229, 76, 229);\n"
                                         "}\n"
                                         "")
        self.pushButton_14.setFlat(False)
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout.addWidget(self.pushButton_14, 1, 3, 1, 1)
        self.pushButton_18 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_18.setMinimumSize(QtCore.QSize(0, 45))
        self.pushButton_18.setStyleSheet("QPushButton{\n"
                                         "border:0px solid rgb(12, 40, 71);\n"
                                         "    background-color: rgb(2, 173, 225);\n"
                                         "border-radius:10px;\n"
                                         "    color: rgb(227, 227, 227);\n"
                                         "    font: 16pt \"MS Shell Dlg 2\";\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "border:3px solid white;\n"
                                         "\n"
                                         "}\n"
                                         "QPushButton:pressed{\n"
                                         "background-color: rgb(229, 76, 229);\n"
                                         "}\n"
                                         "")
        self.pushButton_18.setFlat(False)
        self.pushButton_18.setObjectName("pushButton_18")
        self.gridLayout.addWidget(self.pushButton_18, 2, 0, 1, 1)
        self.pushButton_17 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_17.setMinimumSize(QtCore.QSize(0, 45))
        self.pushButton_17.setStyleSheet("QPushButton{\n"
                                         "border:0px solid rgb(12, 40, 71);\n"
                                         "    background-color: rgb(2, 173, 225);\n"
                                         "border-radius:10px;\n"
                                         "    color: rgb(227, 227, 227);\n"
                                         "    font: 16pt \"MS Shell Dlg 2\";\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "border:3px solid white;\n"
                                         "\n"
                                         "}\n"
                                         "QPushButton:pressed{\n"
                                         "background-color: rgb(229, 76, 229);\n"
                                         "}\n"
                                         "")
        self.pushButton_17.setFlat(False)
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout.addWidget(self.pushButton_17, 0, 0, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_16.setMinimumSize(QtCore.QSize(0, 45))
        self.pushButton_16.setStyleSheet("QPushButton{\n"
                                         "border:0px solid rgb(12, 40, 71);\n"
                                         "    background-color: rgb(2, 173, 225);\n"
                                         "border-radius:10px;\n"
                                         "    color: rgb(227, 227, 227);\n"
                                         "    font: 16pt \"MS Shell Dlg 2\";\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "border:3px solid white;\n"
                                         "\n"
                                         "}\n"
                                         "QPushButton:pressed{\n"
                                         "background-color: rgb(229, 76, 229);\n"
                                         "}\n"
                                         "")
        self.pushButton_16.setFlat(False)
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout.addWidget(self.pushButton_16, 0, 2, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_15.setMinimumSize(QtCore.QSize(0, 45))
        self.pushButton_15.setStyleSheet("QPushButton{\n"
                                         "border:0px solid rgb(12, 40, 71);\n"
                                         "    background-color: rgb(2, 173, 225);\n"
                                         "border-radius:10px;\n"
                                         "    color: rgb(227, 227, 227);\n"
                                         "    font: 16pt \"MS Shell Dlg 2\";\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "border:3px solid white;\n"
                                         "\n"
                                         "}\n"
                                         "QPushButton:pressed{\n"
                                         "background-color: rgb(229, 76, 229);\n"
                                         "}\n"
                                         "")
        self.pushButton_15.setFlat(False)
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout.addWidget(self.pushButton_15, 0, 3, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setMinimumSize(QtCore.QSize(0, 45))
        self.pushButton_7.setStyleSheet("QPushButton{\n"
                                        "border:0px solid rgb(12, 40, 71);\n"
                                        "    background-color: rgb(2, 173, 225);\n"
                                        "border-radius:10px;\n"
                                        "    color: rgb(227, 227, 227);\n"
                                        "    font: 16pt \"MS Shell Dlg 2\";\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "border:3px solid white;\n"
                                        "\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "background-color: rgb(229, 76, 229);\n"
                                        "}\n"
                                        "")
        self.pushButton_7.setFlat(False)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 3, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 381, 81))
        self.lineEdit.setStyleSheet("font: 30px \"MS Shell Dlg 2\";\n"
                                    "background-color: rgb(255, 255, 255);\n"
                                    "border-radius:30px;\n"
                                    "border:3px solid rgb(2, 173, 225);\n"
                                    "\n"
                                    "")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор от Юрчика"))
        self.pushButton_4.setText(_translate("MainWindow", "6"))
        self.pushButton_8.setText(_translate("MainWindow", "4"))
        self.pushButton_9.setText(_translate("MainWindow", "5"))
        self.pushButton_10.setText(_translate("MainWindow", "8"))
        self.pushButton_3.setText(_translate("MainWindow", "0"))
        self.pushButton_6.setText(_translate("MainWindow", "3"))
        self.pushButton_11.setText(_translate("MainWindow", "-"))
        self.pushButton_12.setText(_translate("MainWindow", "CLEAR"))
        self.pushButton_13.setText(_translate("MainWindow", "2"))
        self.pushButton_5.setText(_translate("MainWindow", "="))
        self.pushButton_14.setText(_translate("MainWindow", "*"))
        self.pushButton_18.setText(_translate("MainWindow", "1"))
        self.pushButton_17.setText(_translate("MainWindow", "7"))
        self.pushButton_16.setText(_translate("MainWindow", "9"))
        self.pushButton_15.setText(_translate("MainWindow", "/"))
        self.pushButton_7.setText(_translate("MainWindow", "+"))
