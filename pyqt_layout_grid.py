import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Experiment(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # build button layout

        pixmap = QPixmap("images/Header1.jpg")
        header1 = QLabel()
        header1.setScaledContents(True)
        header1.setMinimumHeight(100)
        header1.setMinimumWidth(100)
        header1.setPixmap(pixmap)

        pixmap = QPixmap("images/Header2.png")
        header2 = QLabel()
        header2.setScaledContents(True)
        header2.setMinimumHeight(100)
        header2.setMinimumWidth(100)
        header2.setPixmap(pixmap)

        pixmap = QPixmap("images/Header3.jpg")
        header3 = QLabel()
        header3.setScaledContents(True)
        header3.setMinimumHeight(100)
        header3.setMinimumWidth(100)
        header3.setPixmap(pixmap)

        pixmap = QPixmap("images/Header4.jpg")
        header4 = QLabel()
        header4.setScaledContents(True)
        header4.setMinimumHeight(100)
        header4.setMinimumWidth(100)
        header4.setPixmap(pixmap)

        grid_layout = QGridLayout()
        grid_layout.addWidget(header1, 0, 0)
        grid_layout.addWidget(header2, 1, 0)
        grid_layout.addWidget(header3, 2, 0)
        grid_layout.addWidget(header4, 3, 0)

        pixmap = QPixmap("images/Tall.jpg")
        main_image = QLabel()
        # main_image.setScaledContents(True)
        main_image.setMinimumHeight(100)
        main_image.setMinimumWidth(100)
        main_image.setPixmap(pixmap)
        main_image.setAlignment(QtCore.Qt.AlignRight)

        grid_layout.addWidget(main_image, 0, 1, 4, 1)

        central_widget = QWidget()
        central_widget.setLayout(grid_layout)

        self.setCentralWidget(central_widget)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Experiment()
    sys.exit(app.exec_())
