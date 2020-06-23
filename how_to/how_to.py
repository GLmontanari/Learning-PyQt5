# Many times I have asked myself 'When will I quit searching the same
# stuff all over on Stack?'.
#
# Beginners like us just want stuff that is ready for use with very
# little knowledge of what is really happening.
# This is what you will find here. Just copy it and start playing with it.

# omit this part if have it in your app #######################################
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QHBoxLayout, QPushButton


class Window(QWidget):

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.button1 = QPushButton('Do something')
        self.button1.setMinimumSize(180, 180)  # an style example

        # the following means 'when you click on the button, it sends out
        # a SIGNAL to the connected SLOT function 'do_something'.
        # In practice, call 'do_something' when you click the button
        self.button1.clicked.connect(self.do_something)

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.button1, 0)
        self.setLayout(h_layout)

        self.setWindowTitle("GUI")
###############################################################################

# HOW TO...####################################################################
# Attach an action to a button ################################################
    def do_something(self):
        self.button1.setText('Woooooow!')


# omit this part if have it in your app #######################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec_()
###############################################################################
