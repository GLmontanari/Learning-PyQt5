# BASIC LAYOUTS ###############################################################
#
# Create a very simple window using the 3 basic ways to arrange objects in
# a window (actually two of them are a subclass of the third):
# there are four numbered buttons which span horizontally in the first row
# of a 'grid' (pretty much like WPF) and four buttons which span vertically
# in the first column.
#
# The horizontal layout goes from first row, first col (0,0) in the main grid
# to (0,2), spanning 1 row and 2 columns.
# The vertical layout goes from second row, first col (1,0) in the main grid
# to (2,0), spanning 2 rows and 1 column.
#

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QGridLayout, QVBoxLayout, QHBoxLayout, QPushButton


class Window(QWidget):

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        button1 = QPushButton('button 1')
        button2 = QPushButton('button 2')
        button3 = QPushButton('button 3')
        button4 = QPushButton('button 4')

        buttonA = QPushButton('button A')
        buttonB = QPushButton('button B')
        buttonC = QPushButton('button C')
        buttonD = QPushButton('button D')

        # an arbitrary shaped grid
        grid = QGridLayout(parent)

        # arrange items horizontally
        h_layout = QHBoxLayout()
        h_layout.addWidget(button1, 0)  # reorder using the first index
        h_layout.addWidget(button2, 1)  # objects with high index are placed to the right
        h_layout.addWidget(button3, 2)  # of objects with low index
        h_layout.addWidget(button4, 3)

        # arrange items vertically
        v_layout = QVBoxLayout()
        v_layout.addWidget(buttonA, 0)  # reorder using the first index
        v_layout.addWidget(buttonB, 1)  # object with high index are placed below objects
        v_layout.addWidget(buttonC, 2)  # with low index
        v_layout.addWidget(buttonD, 3)

        grid = QGridLayout()  # arrange the widgets in a grid
        grid.addLayout(h_layout, 0, 1, 1, 2)
        grid.addLayout(v_layout, 1, 0, 2, 1)
        self.setLayout(grid)  # set 'grid' as the layout for the main window

        self.setWindowTitle("GUI")
        self.resize(500, 200)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec_()
