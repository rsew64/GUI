import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QFileDialog, QWidget, QHBoxLayout, QVBoxLayout, \
    QTableWidget
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.data = None

    def initUI(self):
        exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        openAct = QAction(QIcon('open.png'), '&Open', self)
        openAct.setShortcut('Ctrl+o')
        openAct.setStatusTip('Open file dialog')
        openAct.triggered.connect(self.openFile)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openAct)
        fileMenu.addSeparator()
        fileMenu.addAction(exitAct)

        LayoutH = QHBoxLayout()
        LayoutV = QVBoxLayout()

        widgetTable = QTableWidget()


        widgetSD = QWidget()
        widgetSD.setLayout(LayoutV)

        widgetStat = QWidget()
        widgetStat.setStyleSheet('background-color: purple;')

        widgetDetail = QWidget()
        widgetDetail.setStyleSheet('background-color : cyan;')

        LayoutV.addWidget(widgetStat, 1)
        LayoutV.addWidget(widgetDetail, 1)

        LayoutH.addWidget(widgetTable, 3)
        LayoutH.addWidget(widgetSD, 1)


        widget = QWidget()
        widget.setLayout(LayoutH)
        self.setCentralWidget(widget)


        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Simple menu')
        self.show()






    def openFile(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "open File","",
                                                  "All Files (*);;Excel Files (*.xlsx; *.xls) ;;"
                                                  "CSV Files (*csv)", options=options)
        if fileName:
            fichier = open(fileName, 'r')
            self.data = [i.split(";") for i in fichier.read().split('\n')]
            print(self.data)

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()