# QPushButton generates 'clicked' signals when you click it duh

from PyQt6.QtWidgets import (QApplication, 
    QPushButton, QLabel, QWidget, QVBoxLayout)
from PyQt6.QtCore import Qt, QObject
from PyQt6.QtTest import QTest
import PyQt6
import sys
from random import randint


class FirstTest(QObject):
    
    def __init__(self):
        super().__init__()
        
    def initTestCase(self):
        print('Init test case')
        
    def cleanupTestCase(self):
        print('Cleanup test case')

        
    def button_click_test(self):
        print('Click button test')


class TestQString(QObject):
    
    def toUpper(self):
        str = 'Hello'
        QVERIFY(str.toUpper() == 'HELLO')


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 1 - Create the button and add it to the window layout
        
        button = QPushButton('Generate random integer')
        
        # 3 - Connect the button clicked event with the slot
        
        button.clicked.connect(self.on_button_clicked)
        
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        layout.addWidget(button)
        layout.addWidget(self.label)
    
    # 2 - Create the method/function to use as the slot
    
    def on_button_clicked(self):
        self.label.setText(str(randint(0, 100)))


if __name__ == '__main__':

    '''if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())'''
    
    #first_test = FirstTest()
    #QTest.QTest.qExec(first_test)
    
    for x in dir(QTest):
        print(x)
