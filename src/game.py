from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtWidgets import QAction, QMenu
from PyQt5.QtWidgets import QLayout, QGridLayout, QSizePolicy
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton
from cardpattern import Pattern, Easy, Normal, Hard

class Cards(QWidget):

    def __init__(self):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

    def sizeHint(self):
        size = super(Cards, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size

class mainMenu(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        menu = self.menuBar()
        menu_game = menu.addMenu('Game')
        menu_difficulty = menu.addMenu('Difficulty')

        game_newgame = QAction('New Game', self)
        game_newgame.setShortcut('Ctrl+N')
        game_newgame.setStatusTip("Start a new game.")

        game_exit = QAction('Exit', self)
        game_exit.setShortcut('Esc')

        difficulty_easy = QAction('Easy', self)
        difficulty_normal = QAction('Normal', self)
        difficulty_hard = QAction('Hard', self)

        menu_game.addAction(game_newgame)
        menu_game.addAction(game_exit)
        menu_difficulty.addAction(difficulty_easy)
        menu_difficulty.addAction(difficulty_normal)
        menu_difficulty.addAction(difficulty_hard)

        game_exit.triggered.connect(QCoreApplication.instance().quit)

        while True:
            if difficulty_easy.triggered.connect(bool):
                self.statusBar().showMessage("Easy Mode!")
                start = Easy()
                start.makeButtons()
            elif difficulty_normal.triggered.connect(bool):
                self.statusBar().showMessage("Normal Mode!")
                start = Normal()
                start.makeButtons()
            elif difficulty_hard.triggered.connect(bool):
                self.statusBar().showMessage("Hard Mode!")
                start = Hard()
                start.makeButtons()
            elif game_newgame.triggered.connect(bool):
                self.statusBar().showMessage("New Game as Easy Mode!")
                start = Easy()
                start.makeButtons()

        self.setWindowTitle("Memory Card Game")

        self.resize(1000, 1500)
        self.show()

 #   def buttonClicked(self):



if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    window = mainMenu()
    window.show()
    sys.exit(app.exec_())