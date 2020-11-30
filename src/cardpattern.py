import sys
import random
from PyQt5.QtWidgets import QWidget, QGridLayout
from PyQt5.QtWidgets import QPushButton
from card_picture import easyLevel, normalLevel, hardLevel

class Pattern():

    def __init__(self):
        super().__init__()
        self.button = []
        self.picture = [] #icons on cards
        self.count = 0
        self.range = 1
        self.column = 1

        cardLayout = QGridLayout()
        self.setLayout(cardLayout)

    def makeButtons(self):
        for x in range(100): # mix cards
            rnd = random.randint(0, len(self.picture)-1)
            self.picture[rnd], self.picture[0] = self.picture[0], self.picture[rnd]

        for r in range(4):
            for c in range(self.column):
                self.button = QPushButton(str(str(4*r+c)))
                self.cardLayout.addWidget(self.button, r, c)

class Easy(Pattern):
    def __init__(self):
        self.button = []
        self.picture = easyLevel
        self.range = 8
        self.column = 2
        self.cardLayout = QGridLayout()
class Normal(Pattern):
    def __init__(self):
        self.button = []
        self.picture = normalLevel
        self.range = 12
        self.column = 3
        self.cardLayout = QGridLayout()
class Hard(Pattern):
    def __init__(self):
        self.button = []
        self.picture = normalLevel
        self.range = 16
        self.column = 4
        self.cardLayout = QGridLayout()