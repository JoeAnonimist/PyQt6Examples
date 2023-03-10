#

from PyQt6.QtWidgets import (QApplication, 
    QWidget, QVBoxLayout)
import sys


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)


if __name__ == '__main__':

    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())
