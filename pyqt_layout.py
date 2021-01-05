import sys
from PyQt5.QtWidgets import *


class Experiment(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # build button layout
        button1 = QPushButton("Button 1")
        button1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button2 = QPushButton("Button 2")
        button2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button3 = QPushButton("Button 3")
        button3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        button_layout = QVBoxLayout()
        button_layout.addWidget(button1)
        button_layout.addWidget(button2)
        button_layout.addWidget(button3)

        button4 = QPushButton("Button 4")
        button4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        h_layout = QHBoxLayout()
        h_layout.addLayout(button_layout)
        h_layout.addWidget(button4)

        central_widget = QWidget()
        central_widget.setLayout(h_layout)

        self.setCentralWidget(central_widget)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Experiment()
    sys.exit(app.exec_())
