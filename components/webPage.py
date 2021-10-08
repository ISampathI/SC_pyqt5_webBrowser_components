######################################################
##  SihinaCode > Search YouTube for more tutorials  ##
######################################################
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineView
from components.webPageUi import Ui_wpWidget

class WebPage(QtWidgets.QWidget, Ui_wpWidget):
    def __init__(self, parent = None):
        super(WebPage, self).__init__(parent = parent)
        self.setupUi(self)

        self.webEngineView = QWebEngineView()
        self.webEngineView.page().setBackgroundColor(QtGui.QColor(45, 45, 45, 255))
        self.webEngineView.setObjectName("webEngineView")
        self.verticalLayout_3.addWidget(self.webEngineView)

        self.wpLineEdit.returnPressed.connect(self.load)
        self.wpPushButton.clicked.connect(self.backward)
        self.wpPushButton_2.clicked.connect(self.forward)
        self.wpPushButton_3.clicked.connect(self.reload)

    def load(self):
        url = QtCore.QUrl.fromUserInput(self.wpLineEdit.text())
        if url.isValid():
            self.webEngineView.load(url)    
    def backward(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Back)
    def forward(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Forward)
    def reload(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Reload)
