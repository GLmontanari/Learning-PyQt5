import sys
from PyQt5.QtWidgets import QApplication, QWidget

# MINIMAL APP #################################################################
#
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget
#


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

# As in C++, the main container is QApplication.
# The main window is hidden unless you 'show()' it. Therefore 'window.show()'.
#
# __init__ calls the class constructor
# set some properties of the calling object from inside of it using 'self.'.
###############################################################################
