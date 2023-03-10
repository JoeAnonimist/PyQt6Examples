#

from PyQt6.QtWidgets import (QApplication, 
    QWidget, QVBoxLayout)
from PyQt6.QtCore import Qt, QTimer
import sys


class Display(QWidget):
    
    WIDTH = 800
    HEIGHT = 480
    SPEED = 300
    
    def __init__(self, parent):
        
        super().__init__(parent)
        self.init_display()
        
    def init_display(self):
        
        self.resize(Display.WIDTH, Display.HEIGHT)
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_event)
        
        self.started = False
        self.paused = False
        
    def start(self):
        
        if self.paused:
            return
        
        self.started = True
        self.timer.start(Display.SPEED)
        
    def pause(self):
        
        if not self.started:
            return
            
        self.paused = not self.paused
        
        if self.paused:
            self.timer.stop()
        else:
            self.timer.start(Board.Speed)

    def paintEvent(self, event):
        print('paint event ...')

    def timer_event(self):
        self.repaint()
        print('timer event ...')


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        display = Display(self)
        layout.addWidget(display)
        display.start()
        
        self.show()


if __name__ == '__main__':

    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())
