import sys
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView
from ModuleCedric.Module_Cédric import * 
from moduleAnne.classesPandas import JsonToDictionnary
import time


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, gamesList, categoriesList):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # Leaderboard Definition
        self.leaderboard = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.leaderboard.setGeometry(QtCore.QRect(20, 80, 771, 461))
        self.leaderboard.setObjectName("Leaderboard")
        self.leaderboard.setColumnCount(0)
        self.leaderboard.setRowCount(0)
        # Definition Games ComboBox
        self.gamesComboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.gamesComboBox.setGeometry(QtCore.QRect(20, 30, 271, 26))
        self.gamesComboBox.setObjectName("gamesComboBox")
        self.gamesComboBox.addItems(gamesList)
        # Definition Categories ComboBox
        self.categoriesComboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.categoriesComboBox.setGeometry(QtCore.QRect(320, 30, 211, 26))
        self.categoriesComboBox.setObjectName("categoriesComboBox")
        self.categoriesComboBox.addItems(categoriesList)
        self.categoriesComboBox.setEnabled(False)
        
        # Definition Max Row Label and spinbox
        self.maxRowLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.maxRowLabel.setGeometry(QtCore.QRect(560, 30, 41, 21))
        self.maxRowLabel.setObjectName("labelMaxRow")
        self.maxRowSpinBox = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.maxRowSpinBox.setGeometry(QtCore.QRect(610, 30, 45, 27))
        self.maxRowSpinBox.setObjectName("spinBox")
        self.maxRowSpinBox.setMaximum(30)
        self.maxRowSpinBox.setMinimum(10)
        self.maxRowSpinBox.lineEdit().setReadOnly(True)

        # Definition Button of validation
        self.validButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.validButton.setGeometry(QtCore.QRect(680, 15, 91, 51))
        self.validButton.setEnabled(False)
        self.validButton.setObjectName("validButton")

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
        MainWindow.setWindowTitle(_translate("MainWindow", "API Tool request speedrun.com"))
        self.maxRowLabel.setText(_translate("MainWindow", "Runs"))
        self.validButton.setText(_translate("MainWindow", "Search"))

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        # Déclaration des données de l'application
        self.jsonTool = JsonToDictionnary()
        self.gamesDict = {
            "placeholder": "Select a game",
            "j1nem5x1": "RE 4 (steam)",
            "76rkwed8" : "Nier Automata" 
        }
        self.categoriesDict ={
            "placeholder": "Select a Category"
        }
        self.cachedGameData = {}
        self.cachedLeaderboardData = {}
        self.cachedRunners = {}
        self.leaderBoard = []
        self.selectedGame = ""
        self.selectedCategory = ""
        
        # Déclaration des éléments visuels
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self, list(self.gamesDict.values()) , list(self.categoriesDict.values()))
        self.resetLeaderboard()
        
        # Déclaration des triggers des élémpents visuels
        self.ui.gamesComboBox.activated.connect(self.selectGame)
        self.ui.categoriesComboBox.activated.connect(self.selectCategory)
        self.ui.validButton.pressed.connect(self.valid)

    def selectGame(self):
        if self.ui.gamesComboBox.currentIndex() > 0 :
            selected = list(self.gamesDict)[self.ui.gamesComboBox.currentIndex()]
            if self.selectedGame != selected:
                self.selectedGame = selected 
                self.ui.categoriesComboBox.setEnabled(True)
                self.ui.validButton.setEnabled(False)
                self.resetCategoriesComboBox()
                self.resetLeaderboard()
                self.updateCategories()
        else:
            self.resetAndDisableCategoriesComboBox()
            self.selectedGame = ""
            self.ui.validButton.setEnabled(False)
            self.resetLeaderboard()

    def updateCategories(self):
        
        if self.selectedGame in self.cachedGameData:
            game_json = self.cachedGameData[self.selectedGame]
        else:
            game_categories = SearchCategory(self.selectedGame)
            game_json = game_categories.get_category()
            self.cachedGameData[self.selectedGame] = game_json

        catogories_dict = self.jsonTool.export_json_categories(game_json)
        for key, value in catogories_dict.items():
            self.categoriesDict[value[0]] = value[1]
        self.populateCategoriesComboBox()

    def selectCategory(self):
        if self.ui.categoriesComboBox.currentIndex() > 0 :
            selected = list(self.categoriesDict)[self.ui.categoriesComboBox.currentIndex()]
            if self.selectedCategory != selected:
                self.selectedCategory = selected
                self.ui.validButton.setEnabled(True)
                self.resetLeaderboard()
        else:
            self.selectedCategory = ""
            self.ui.validButton.setEnabled(False)
            self.resetLeaderboard()

    def valid(self):
        if self.selectedGame in self.cachedLeaderboardData:
            leadeboard_json = self.cachedLeaderboardData[f"{self.selectedGame}{self.selectedCategory}"]
        else:
            game_categories = SearchCategory(self.selectedGame)
            game_categories.set_category(self.selectedCategory)
            leadeboard_json = game_categories.get_leaderboard()
            self.cachedLeaderboardData[f"{self.selectedGame}{self.selectedCategory}"] = leadeboard_json

        leaderboardDict = self.jsonTool.export_json_leaderboard(leadeboard_json)
        self.formatLeaderboardWithPseudo(leaderboardDict)

        self.showLeaderboard()

    def formatLeaderboardWithPseudo(self, leaderboardDict):
        self.leaderBoard = [["Rank", "Player", "RealTime"]]

        max_range = self.ui.maxRowSpinBox.value()
        if len(leaderboardDict) < max_range:
            max_range = len(leaderboardDict)
    
        for i in range(1,  max_range + 1):
            playerId = leaderboardDict[str(i)][0]
            if "guest =" in playerId:
                pseudo = playerId[8:]
            elif playerId in self.cachedRunners:
                pseudo = self.cachedRunners[playerId]
            else:
                pseudo = self.jsonTool.export_pseudo(Runner(playerId).get_runner())
                time.sleep(1)
            player_time = leaderboardDict[str(i)][1]
            self.leaderBoard.append([str(i),pseudo, player_time[2:]])
        

    def showLeaderboard(self):
        if len(self.leaderBoard) > 15:
            self.ui.leaderboard.setRowCount(len(self.leaderBoard))
        for row in range(len(self.leaderBoard)):
            for column in range(len(self.leaderBoard[row])):
                self.ui.leaderboard.setItem(row, column, QTableWidgetItem(self.leaderBoard[row][column]))
                if row == 0:
                    self.ui.leaderboard.item(row, column).setBackground(QColor(160,160,160))
                elif (row % 2) == 0:
                    self.ui.leaderboard.item(row, column).setBackground(QColor(224,224,224))

    def resetCategoriesComboBox(self):
        self.categoriesDict ={ "placeholder": "Select a Category"}
        self.populateCategoriesComboBox()
        self.ui.categoriesComboBox.setCurrentIndex(0)

    def populateCategoriesComboBox(self):
        self.ui.categoriesComboBox.clear()
        self.ui.categoriesComboBox.addItems(list(self.categoriesDict.values()))

    def resetAndDisableCategoriesComboBox(self):
        self.resetCategoriesComboBox()
        self.ui.categoriesComboBox.setEnabled(False)

    def resetLeaderboard(self):
        self.ui.leaderboard.clear()
        self.ui.leaderboard.setRowCount(15)
        self.ui.leaderboard.setColumnCount(3)
        self.ui.leaderboard.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.ui.leaderboard.verticalHeader().setVisible(False)
        self.ui.leaderboard.horizontalHeader().setVisible(False)
        self.leaderBoard = [["Rank", "Player", "RealTime"]]
        
        for row in range(15):
            for column in range(3):
                if row == 0:
                    self.ui.leaderboard.setItem(row, column, QTableWidgetItem(self.leaderBoard[0][column]))
                    self.ui.leaderboard.item(row, column).setBackground(QColor(160,160,160))
                elif (row % 2) == 0:
                    self.ui.leaderboard.setItem(row, column, QTableWidgetItem(""))
                    self.ui.leaderboard.item(row, column).setBackground(QColor(224,224,224))
                else:
                    self.ui.leaderboard.setItem(row, column, QTableWidgetItem(""))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())