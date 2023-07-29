import sys
from PyQt6.QtCore import Qt
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QComboBox, QWidget, QSpinBox, QLabel, QPushButton


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, gamesList):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.tableWidget = LeaderboardWidget(self.centralwidget)
        self.game     = GamesComboBox(self.centralwidget, [20, 30, 271, 26] , "Game", gamesList)
        self.category = CategoriesComboBox(self.centralwidget, [320, 30, 211, 26], "Category")
        self.maxLabel = Label(self.centralwidget, [560, 30, 41, 21], "MaxLabel")
        self.maxSpinbox = MaxRowSpinBox(self.centralwidget, [610, 30, 45, 27], "MaxSpinbox")
        self.validButton = Button(self.centralwidget, [680, 15, 91, 51], "ValidButton")

        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.maxLabel.setText(_translate("MainWindow", "Runs"))
        self.validButton.setText(_translate("MainWindow", "PushButton"))

class LeaderboardWidget(QTableWidget):

    def __init__(self, parent) -> None:
        super().__init__(parent=parent)
        self.setGeometry(QtCore.QRect(20, 80, 771, 461))
        self.setObjectName("tableWidget")
        self.setColumnCount(0)
        self.setRowCount(0)

class CategoriesComboBox(QComboBox):
    def __init__(self, parent, geometry_list, name) -> None:
        super().__init__(parent)
        self.setGeometry(QtCore.QRect(geometry_list[0],geometry_list[1], geometry_list[2], geometry_list[3]))
        self.setObjectName(name)

class GamesComboBox(QComboBox):
    def __init__(self, parent, geometry_list, name, gamesList) -> None:
        super().__init__(parent)
        self.setGeometry(QtCore.QRect(geometry_list[0],geometry_list[1], geometry_list[2], geometry_list[3]))
        self.setObjectName(name)    
        self.addItems(gamesList)

class MaxRowSpinBox(QSpinBox):
    def __init__(self, parent, geometry_list, name) -> None:
        super().__init__(parent)
        self.setGeometry(QtCore.QRect(geometry_list[0],geometry_list[1], geometry_list[2], geometry_list[3]))
        self.setObjectName(name)

class Label(QLabel):
    def __init__(self, parent, geometry_list, name) -> None:
        super().__init__(parent)
        self.setGeometry(QtCore.QRect(geometry_list[0],geometry_list[1], geometry_list[2], geometry_list[3]))
        self.setObjectName(name)

class Button(QPushButton):
    def __init__(self, parent, geometry_list, name) -> None:
        super().__init__(parent)
        self.setGeometry(QtCore.QRect(geometry_list[0],geometry_list[1], geometry_list[2], geometry_list[3]))
        self.setObjectName(name)    


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.gamesDict = {
            "j1nem5x1": "RE 4 (steam)",
            "76rkwed8" : "Nier Automata" 
        }
        self.categoryDict ={}
        self.leaderBoard = []
        self.selectedGames = ""
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self, list(self.gamesDict.values()))
        self.ui.game.activated.connect(self.selectGames)

    def selectGames(self):
        self.selectGames = (list(self.gamesDict)[self.ui.game.currentIndex()]) 
        print(self.selectGames)
        self.updateCategory()

    def updateCategory(self):
        print("Hello world")
        
      

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())