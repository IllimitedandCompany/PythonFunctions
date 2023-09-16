import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget

class VirtualAssistantStatus(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 200, 200)  # Set the size of the widget
        self.setWindowTitle('Virtual Assistant Status')

        # Create labels for different status images
        self.red_dot = QLabel(self)
        self.green_dot = QLabel(self)
        self.blue_dot = QLabel(self)

        # Load and set images for the labels
        self.red_image = QPixmap('red_dot.png')
        self.green_image = QPixmap('green_dot.png')
        self.blue_image = QPixmap('blue_dot.png')

        self.red_dot.setPixmap(self.red_image)
        self.green_dot.setPixmap(self.green_image)
        self.blue_dot.setPixmap(self.blue_image)

        # Add labels to a vertical layout
        layout = QVBoxLayout()
        layout.addWidget(self.red_dot)
        layout.addWidget(self.green_dot)
        layout.addWidget(self.blue_dot)
        layout.setAlignment(Qt.AlignBottom | Qt.AlignRight)

        self.setLayout(layout)

        # Initially, show the red dot
        self.showRedDot()

    def showRedDot(self):
        self.red_dot.show()
        self.green_dot.hide()
        self.blue_dot.hide()

    def showGreenDot(self):
        self.red_dot.hide()
        self.green_dot.show()
        self.blue_dot.hide()

    def showBlueDot(self):
        self.red_dot.hide()
        self.green_dot.hide()
        self.blue_dot.show()

    def startListening(self):
        self.showGreenDot()

    def stopListening(self):
        self.showRedDot()

    def executingCommand(self):
        self.showBlueDot()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.statusBar().setVisible(False)
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('Virtual Assistant Status Demo')

        # Create and set the status widget
        self.status_widget = VirtualAssistantStatus()
        self.setCentralWidget(self.status_widget)

        # Simulate different states
        QTimer.singleShot(1000, self.startListening)
        QTimer.singleShot(5000, self.stopListening)
        QTimer.singleShot(8000, self.executingCommand)

    def startListening(self):
        self.status_widget.startListening()

    def stopListening(self):
        self.status_widget.stopListening()

    def executingCommand(self):
        self.status_widget.executingCommand()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
