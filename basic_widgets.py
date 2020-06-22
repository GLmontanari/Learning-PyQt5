#  A simple GUI with the very building blocks ov every GUI
#
#  The various widgets actually do nothing.
import sys
from PyQt5.QtWidgets import QApplication, QWidget  # import for the main window
from PyQt5.QtWidgets import (QGridLayout, QVBoxLayout, QLabel,  # a multi-line import
                             QPushButton, QRadioButton, QCheckBox,
                             QGroupBox, QLineEdit, QComboBox)


class Window(QWidget):

    # class constructor
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        label = QLabel('a label')
        button = QPushButton('a button')
        radio = QRadioButton('a radio button')
        check = QCheckBox('a checkbox')

        grid = QGridLayout()  # arrange the widgets in a grid
        grid.addWidget(label, 0, 0, 1, 1)  # first index = row
        grid.addWidget(button, 1, 0, 1, 1)  # second index = column
        grid.addWidget(radio, 2, 0, 1, 1)  # third index = row span
        grid.addWidget(check, 2, 1, 1, 1)  # fourth index = column span
        # col span and row span indexes are optional
        grid.addWidget(self.create_example_group(), 3, 0)
        self.setLayout(grid)

        self.setWindowTitle("GUI")
        self.resize(500, 200)

    def create_example_group(self):
        groupbox = QGroupBox('a groupbox')

        radio1 = QRadioButton('first')
        radio1.setChecked(True)

        radio2 = QRadioButton('second')

        textbox = QLineEdit('a textbox', self)

        combo = QComboBox()
        combo.addItem('YES', 10)
        combo.addItem('NO', 20)

        vbox = QVBoxLayout()
        vbox.addWidget(radio1)
        vbox.addWidget(radio2)
        vbox.addWidget(textbox)
        vbox.addWidget(combo)
        vbox.addStretch(1)
        groupbox.setLayout(vbox)

        return groupbox


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec_()
