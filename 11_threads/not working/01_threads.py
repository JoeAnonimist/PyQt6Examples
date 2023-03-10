# The QThread class provides a platform-independent 
# way to manage threads. Move long running tasks
# into a separate thread so the GUI keeps being responsive.

from PyQt6.QtWidgets import (QApplication, 
    QWidget, QVBoxLayout, QPushButton, QLabel)
from PyQt6.QtCore import QThread, QObject, QRunnable, pyqtSlot, pyqtSignal
import sys
from random import randint


class MyTask(QObject, QRunnable):
    
    def run(self):
        pass
        
    @pyqtSlot()
    def finish_task(self):
        pass



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
