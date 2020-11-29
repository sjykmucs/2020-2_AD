import sys
from PyQt5.QtWidgets import QApplication, QWidget

class Screen(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
            self.show()

app = QApplication(sys.argv)
w = Screen()
sys.exit(app.exec_())