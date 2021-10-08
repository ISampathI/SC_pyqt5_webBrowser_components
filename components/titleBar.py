######################################################
##  SihinaCode > Search YouTube for more tutorials  ##
######################################################
from PyQt5 import QtCore, QtGui, QtWidgets
from components.titleBarUi import Ui_tbWidget
from components.movableLabel import MovableLabel
import sys

class TitleBar(QtWidgets.QWidget, Ui_tbWidget):
    def __init__(self, parent = None):
        super(TitleBar, self).__init__(parent = parent)
        self.setupUi(self)
        self.parent = parent
        MovableLabel.mainWindow = self.parent

        self.tbPushButton.clicked.connect(self.parent.showMinimized)
        self.tbPushButton_2.clicked.connect(self.winShowMaximized)
        self.tbPushButton_3.clicked.connect(sys.exit)

    def winShowMaximized(self):
        if self.tbPushButton_2.isChecked():
            self.parent.showMaximized()
            self.tbPushButton_2.setText(";")
        else:
            self.parent.showNormal()
            self.tbPushButton_2.setText("")

    def insertTab(self, widget):
        self.horizontalLayout.addWidget(widget)
