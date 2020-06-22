#  A simple GUI with the very building blocks ov every GUI
import sys
from PyQt5.QtWidgets import QApplication, QWidget


class Window(QWidget):

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.setWindowTitle("GUI")
        self.resize(500, 200)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec_()
