import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://google.com/'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('<-', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('->', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('R', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction('H', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('https://google.com/'))

    def navigate_to_url(self):
        url_input = self.url_bar.text()
        list_url = url_input.split(".")
        lenght_url = len(list_url)
        if(list_url[0] == "https://www"):
            url = url_input
        elif(list_url[0] == "www"):
            url = "https://"+url_input
        elif(list_url[0] != "https://www" and list_url[0] != "www"):
            if(lenght_url == 1):
                url = "https://www.google.com/search?q="+url_input
            else:
                url = "https://www."+url_input

        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())

    

app = QApplication(sys.argv)
QApplication.setApplicationName('Meu Navegador')
window = MainWindow()
app.exec_()

