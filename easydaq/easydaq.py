# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'easydaq/easydaq.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(806, 651)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 0, 0);")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.cBenable1 = QtWidgets.QCheckBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cBenable1.sizePolicy().hasHeightForWidth())
        self.cBenable1.setSizePolicy(sizePolicy)
        self.cBenable1.setMinimumSize(QtCore.QSize(100, 27))
        self.cBenable1.setObjectName("cBenable1")
        self.verticalLayout.addWidget(self.cBenable1)
        self.Bconfigure1 = QtWidgets.QPushButton(self.centralwidget)
        self.Bconfigure1.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Bconfigure1.sizePolicy().hasHeightForWidth())
        self.Bconfigure1.setSizePolicy(sizePolicy)
        self.Bconfigure1.setMinimumSize(QtCore.QSize(100, 27))
        self.Bconfigure1.setObjectName("Bconfigure1")
        self.verticalLayout.addWidget(self.Bconfigure1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(85, 170, 0);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.cBenable2 = QtWidgets.QCheckBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cBenable2.sizePolicy().hasHeightForWidth())
        self.cBenable2.setSizePolicy(sizePolicy)
        self.cBenable2.setMinimumSize(QtCore.QSize(100, 27))
        self.cBenable2.setObjectName("cBenable2")
        self.verticalLayout.addWidget(self.cBenable2)
        self.Bconfigure2 = QtWidgets.QPushButton(self.centralwidget)
        self.Bconfigure2.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Bconfigure2.sizePolicy().hasHeightForWidth())
        self.Bconfigure2.setSizePolicy(sizePolicy)
        self.Bconfigure2.setMinimumSize(QtCore.QSize(100, 27))
        self.Bconfigure2.setObjectName("Bconfigure2")
        self.verticalLayout.addWidget(self.Bconfigure2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.cBenable3 = QtWidgets.QCheckBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cBenable3.sizePolicy().hasHeightForWidth())
        self.cBenable3.setSizePolicy(sizePolicy)
        self.cBenable3.setMinimumSize(QtCore.QSize(100, 27))
        self.cBenable3.setObjectName("cBenable3")
        self.verticalLayout.addWidget(self.cBenable3)
        self.Bconfigure3 = QtWidgets.QPushButton(self.centralwidget)
        self.Bconfigure3.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Bconfigure3.sizePolicy().hasHeightForWidth())
        self.Bconfigure3.setSizePolicy(sizePolicy)
        self.Bconfigure3.setMinimumSize(QtCore.QSize(100, 27))
        self.Bconfigure3.setObjectName("Bconfigure3")
        self.verticalLayout.addWidget(self.Bconfigure3)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.cBenable4 = QtWidgets.QCheckBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cBenable4.sizePolicy().hasHeightForWidth())
        self.cBenable4.setSizePolicy(sizePolicy)
        self.cBenable4.setMinimumSize(QtCore.QSize(100, 27))
        self.cBenable4.setObjectName("cBenable4")
        self.verticalLayout.addWidget(self.cBenable4)
        self.Bconfigure4 = QtWidgets.QPushButton(self.centralwidget)
        self.Bconfigure4.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Bconfigure4.sizePolicy().hasHeightForWidth())
        self.Bconfigure4.setSizePolicy(sizePolicy)
        self.Bconfigure4.setMinimumSize(QtCore.QSize(100, 27))
        self.Bconfigure4.setObjectName("Bconfigure4")
        self.verticalLayout.addWidget(self.Bconfigure4)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.plotWidget = MPL_Widget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotWidget.sizePolicy().hasHeightForWidth())
        self.plotWidget.setSizePolicy(sizePolicy)
        self.plotWidget.setMinimumSize(QtCore.QSize(550, 532))
        self.plotWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.plotWidget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.plotWidget.setObjectName("plotWidget")
        self.verticalLayout_2.addWidget(self.plotWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.cBosc = QtWidgets.QCheckBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cBosc.sizePolicy().hasHeightForWidth())
        self.cBosc.setSizePolicy(sizePolicy)
        self.cBosc.setMinimumSize(QtCore.QSize(165, 22))
        self.cBosc.setMaximumSize(QtCore.QSize(165, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cBosc.setFont(font)
        self.cBosc.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cBosc.setAutoFillBackground(False)
        self.cBosc.setObjectName("cBosc")
        self.horizontalLayout_2.addWidget(self.cBosc)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setIconSize(QtCore.QSize(28, 28))
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusBar.sizePolicy().hasHeightForWidth())
        self.statusBar.setSizePolicy(sizePolicy)
        self.statusBar.setMinimumSize(QtCore.QSize(0, 25))
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionConfigure = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/config.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionConfigure.setIcon(icon)
        self.actionConfigure.setObjectName("actionConfigure")
        self.actionPlay = QtWidgets.QAction(MainWindow)
        self.actionPlay.setCheckable(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/resources/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPlay.setIcon(icon1)
        self.actionPlay.setObjectName("actionPlay")
        self.actionStop = QtWidgets.QAction(MainWindow)
        self.actionStop.setEnabled(False)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/resources/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStop.setIcon(icon2)
        self.actionStop.setObjectName("actionStop")
        self.actionCSV = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/resources/CSV.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCSV.setIcon(icon3)
        self.actionCSV.setObjectName("actionCSV")
        self.toolBar.addAction(self.actionConfigure)
        self.toolBar.addAction(self.actionPlay)
        self.toolBar.addAction(self.actionStop)
        self.toolBar.addAction(self.actionCSV)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        self.cBenable1.clicked['bool'].connect(self.Bconfigure1.setEnabled)
        self.cBenable2.clicked['bool'].connect(self.Bconfigure2.setEnabled)
        self.cBenable3.clicked['bool'].connect(self.Bconfigure3.setEnabled)
        self.cBenable4.clicked['bool'].connect(self.Bconfigure4.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Easydaq"))
        self.label.setText(_translate("MainWindow", "Experiment 1"))
        self.cBenable1.setText(_translate("MainWindow", "Enable"))
        self.Bconfigure1.setText(_translate("MainWindow", "Configure"))
        self.label_2.setText(_translate("MainWindow", "Experiment 2"))
        self.cBenable2.setText(_translate("MainWindow", "Enable"))
        self.Bconfigure2.setText(_translate("MainWindow", "Configure"))
        self.label_3.setText(_translate("MainWindow", "Experiment 3"))
        self.cBenable3.setText(_translate("MainWindow", "Enable"))
        self.Bconfigure3.setText(_translate("MainWindow", "Configure"))
        self.label_5.setText(_translate("MainWindow", "Waveform"))
        self.cBenable4.setText(_translate("MainWindow", "Enable"))
        self.Bconfigure4.setText(_translate("MainWindow", "Configure"))
        self.cBosc.setText(_translate("MainWindow", "Oscilloscope mode"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionConfigure.setText(_translate("MainWindow", "Configure"))
        self.actionPlay.setText(_translate("MainWindow", "play"))
        self.actionStop.setText(_translate("MainWindow", "stop"))
        self.actionCSV.setText(_translate("MainWindow", "CSV"))

from .widgets import MPL_Widget
from . import res_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

