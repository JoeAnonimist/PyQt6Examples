# The signature of a signal must match 
# the signature of the receiving slot. 

# (In fact a slot may have a shorter signature 
# than the signal it receives 
# because it can ignore extra arguments.)

# Demonstrate using a Python lambda function
# as a slot. Lambdas are anonymous functions,
# ie. they have no name.


from PyQt6.QtWidgets import (QApplication, 
    QWidget, QPushButton, QVBoxLayout)
import sys


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 1 - Create the event source, same as
        #     in the basic example
        
        button = QPushButton('Click me!')
        
        # 2 - In this case the slot is a Python lambda
        #     placed in the button.clicked.connect() call.

        
        button.clicked.connect(
            lambda: print('Message from lambda...'))
        
        layout.addWidget(button)
        

if __name__ == '__main__':
    
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()

    main_window = Window()
    main_window.show()
    
    sys.exit(app.exec())
