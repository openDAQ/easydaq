# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'easydaq/configwave.ui'
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
        MainWindow.resize(263, 248)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setGeometry(QtCore.QRect(0, 0, 243, 232))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.cBmode = QtGui.QComboBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cBmode.sizePolicy().hasHeightForWidth())
        self.cBmode.setSizePolicy(sizePolicy)
        self.cBmode.setMinimumSize(QtCore.QSize(120, 27))
        self.cBmode.setObjectName(_fromUtf8("cBmode"))
        self.cBmode.addItem(_fromUtf8(""))
        self.cBmode.addItem(_fromUtf8(""))
        self.cBmode.addItem(_fromUtf8(""))
        self.cBmode.addItem(_fromUtf8(""))
        self.cBmode.addItem(_fromUtf8(""))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.cBmode)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(100, 27))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.cBmodoPeriod = QtGui.QComboBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cBmodoPeriod.sizePolicy().hasHeightForWidth())
        self.cBmodoPeriod.setSizePolicy(sizePolicy)
        self.cBmodoPeriod.setMinimumSize(QtCore.QSize(120, 27))
        self.cBmodoPeriod.setObjectName(_fromUtf8("cBmodoPeriod"))
        self.cBmodoPeriod.addItem(_fromUtf8(""))
        self.cBmodoPeriod.addItem(_fromUtf8(""))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.cBmodoPeriod)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(100, 27))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(100, 27))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_3)
        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QtCore.QSize(100, 30))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.label_6 = QtGui.QLabel(self.page)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 100, 27))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(100, 27))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.label_5 = QtGui.QLabel(self.page_2)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 100, 27))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(100, 27))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.stackedWidget.addWidget(self.page_2)
        self.page_10 = QtGui.QWidget()
        self.page_10.setObjectName(_fromUtf8("page_10"))
        self.stackedWidget.addWidget(self.page_10)
        self.page_9 = QtGui.QWidget()
        self.page_9.setObjectName(_fromUtf8("page_9"))
        self.stackedWidget.addWidget(self.page_9)
        self.page_5 = QtGui.QWidget()
        self.page_5.setObjectName(_fromUtf8("page_5"))
        self.stackedWidget.addWidget(self.page_5)
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.stackedWidget)
        self.stackedWidget_2 = QtGui.QStackedWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget_2.sizePolicy().hasHeightForWidth())
        self.stackedWidget_2.setSizePolicy(sizePolicy)
        self.stackedWidget_2.setMinimumSize(QtCore.QSize(120, 30))
        self.stackedWidget_2.setObjectName(_fromUtf8("stackedWidget_2"))
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.sBtimeon = QtGui.QDoubleSpinBox(self.page_3)
        self.sBtimeon.setGeometry(QtCore.QRect(0, 0, 120, 27))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sBtimeon.sizePolicy().hasHeightForWidth())
        self.sBtimeon.setSizePolicy(sizePolicy)
        self.sBtimeon.setMinimumSize(QtCore.QSize(120, 27))
        self.sBtimeon.setDecimals(3)
        self.sBtimeon.setMinimum(0.0)
        self.sBtimeon.setMaximum(65536.0)
        self.sBtimeon.setSingleStep(1.0)
        self.sBtimeon.setProperty("value", 40.0)
        self.sBtimeon.setObjectName(_fromUtf8("sBtimeon"))
        self.stackedWidget_2.addWidget(self.page_3)
        self.page_4 = QtGui.QWidget()
        self.page_4.setObjectName(_fromUtf8("page_4"))
        self.sBriseTime = QtGui.QDoubleSpinBox(self.page_4)
        self.sBriseTime.setGeometry(QtCore.QRect(0, 0, 120, 27))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sBriseTime.sizePolicy().hasHeightForWidth())
        self.sBriseTime.setSizePolicy(sizePolicy)
        self.sBriseTime.setMinimumSize(QtCore.QSize(120, 27))
        self.sBriseTime.setDecimals(3)
        self.sBriseTime.setMaximum(65536.0)
        self.sBriseTime.setProperty("value", 40.0)
        self.sBriseTime.setObjectName(_fromUtf8("sBriseTime"))
        self.stackedWidget_2.addWidget(self.page_4)
        self.page_8 = QtGui.QWidget()
        self.page_8.setObjectName(_fromUtf8("page_8"))
        self.stackedWidget_2.addWidget(self.page_8)
        self.page_7 = QtGui.QWidget()
        self.page_7.setObjectName(_fromUtf8("page_7"))
        self.stackedWidget_2.addWidget(self.page_7)
        self.page_6 = QtGui.QWidget()
        self.page_6.setObjectName(_fromUtf8("page_6"))
        self.stackedWidget_2.addWidget(self.page_6)
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.stackedWidget_2)
        self.Bsubmit = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Bsubmit.sizePolicy().hasHeightForWidth())
        self.Bsubmit.setSizePolicy(sizePolicy)
        self.Bsubmit.setMinimumSize(QtCore.QSize(120, 27))
        self.Bsubmit.setObjectName(_fromUtf8("Bsubmit"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.Bsubmit)
        self.stackedWidget_3 = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget_3.setMinimumSize(QtCore.QSize(120, 27))
        self.stackedWidget_3.setObjectName(_fromUtf8("stackedWidget_3"))
        self.page_11 = QtGui.QWidget()
        self.page_11.setObjectName(_fromUtf8("page_11"))
        self.sBperiodms = QtGui.QDoubleSpinBox(self.page_11)
        self.sBperiodms.setGeometry(QtCore.QRect(0, 0, 120, 27))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sBperiodms.sizePolicy().hasHeightForWidth())
        self.sBperiodms.setSizePolicy(sizePolicy)
        self.sBperiodms.setMinimumSize(QtCore.QSize(120, 27))
        self.sBperiodms.setDecimals(3)
        self.sBperiodms.setMinimum(1.0)
        self.sBperiodms.setMaximum(65536.0)
        self.sBperiodms.setSingleStep(0.1)
        self.sBperiodms.setProperty("value", 100.0)
        self.sBperiodms.setObjectName(_fromUtf8("sBperiodms"))
        self.stackedWidget_3.addWidget(self.page_11)
        self.page_12 = QtGui.QWidget()
        self.page_12.setObjectName(_fromUtf8("page_12"))
        self.sBperiodus = QtGui.QSpinBox(self.page_12)
        self.sBperiodus.setGeometry(QtCore.QRect(0, 0, 120, 27))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sBperiodus.sizePolicy().hasHeightForWidth())
        self.sBperiodus.setSizePolicy(sizePolicy)
        self.sBperiodus.setMinimumSize(QtCore.QSize(120, 27))
        self.sBperiodus.setMaximum(65536000)
        self.sBperiodus.setProperty("value", 10000)
        self.sBperiodus.setObjectName(_fromUtf8("sBperiodus"))
        self.stackedWidget_3.addWidget(self.page_12)
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.stackedWidget_3)
        self.sBoffset = QtGui.QDoubleSpinBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sBoffset.sizePolicy().hasHeightForWidth())
        self.sBoffset.setSizePolicy(sizePolicy)
        self.sBoffset.setMinimumSize(QtCore.QSize(120, 27))
        self.sBoffset.setDecimals(3)
        self.sBoffset.setMaximum(4.0)
        self.sBoffset.setSingleStep(0.1)
        self.sBoffset.setProperty("value", 0.0)
        self.sBoffset.setObjectName(_fromUtf8("sBoffset"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.sBoffset)
        self.sBamplitude = QtGui.QDoubleSpinBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sBamplitude.sizePolicy().hasHeightForWidth())
        self.sBamplitude.setSizePolicy(sizePolicy)
        self.sBamplitude.setMinimumSize(QtCore.QSize(120, 27))
        self.sBamplitude.setDecimals(3)
        self.sBamplitude.setMaximum(8.0)
        self.sBamplitude.setSingleStep(0.1)
        self.sBamplitude.setProperty("value", 1.0)
        self.sBamplitude.setObjectName(_fromUtf8("sBamplitude"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.sBamplitude)
        self.horizontalLayout.addLayout(self.formLayout)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(0)
        QtCore.QObject.connect(self.cBmode, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), self.stackedWidget.setCurrentIndex)
        QtCore.QObject.connect(self.cBmode, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), self.stackedWidget_2.setCurrentIndex)
        QtCore.QObject.connect(self.cBmodoPeriod, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), self.stackedWidget_3.setCurrentIndex)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Config", None))
        self.label.setText(_translate("MainWindow", "Select mode", None))
        self.cBmode.setItemText(0, _translate("MainWindow", "Square", None))
        self.cBmode.setItemText(1, _translate("MainWindow", "Triangle", None))
        self.cBmode.setItemText(2, _translate("MainWindow", "Sine", None))
        self.cBmode.setItemText(3, _translate("MainWindow", "Sawtooth", None))
        self.cBmode.setItemText(4, _translate("MainWindow", "Fixed potential", None))
        self.label_2.setText(_translate("MainWindow", "Period", None))
        self.cBmodoPeriod.setItemText(0, _translate("MainWindow", "ms", None))
        self.cBmodoPeriod.setItemText(1, _translate("MainWindow", "us", None))
        self.label_4.setText(_translate("MainWindow", "Offset", None))
        self.label_3.setText(_translate("MainWindow", "Amplitude", None))
        self.label_6.setText(_translate("MainWindow", "Time On", None))
        self.label_5.setText(_translate("MainWindow", "Rise Time", None))
        self.Bsubmit.setText(_translate("MainWindow", "Submit", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QDialog()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

