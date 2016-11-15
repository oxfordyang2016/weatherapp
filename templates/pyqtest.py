from PyQt5.QtWidgets import (
#from PyQt4.QtGui import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel,
    )

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.button = QPushButton('Test', self)
        self.label = QLabel(self)
        self.button.clicked.connect(self.handleButton)
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.button)

    def handleButton(self):
        self.label.setText('Button Clicked!')
        print("hahhahhhah")

if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())