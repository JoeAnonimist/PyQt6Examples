# https://wiki.qt.io/Qt_for_Python/Connecting_QML_Signals
# Use a top-level QML signal. Connect a QML signal
# with a Python slot in Python code.

import sys
from random import randint
from PyQt6.QtCore import QObject, pyqtSignal, pyqtSlot
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine


class SomeClass(QObject):
    
    randint_ready = pyqtSignal(int)
    
    def __init__(self):
        super().__init__()
    
    @pyqtSlot('QString')
    def outputStr(self, s):
        print(s)
        
    @pyqtSlot(int, result=int)
    def get_random_number(self, n):
        
        n = randint(0, n)
        print(n)
        self.randint_ready.emit(n)


if __name__ == '__main__':
    
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    
    some_context = SomeClass()
    
    engine.load('top_level_qml_signal.qml')
    
    root = engine.rootObjects()[0]

    root.messageButtonClicked.connect(some_context.outputStr)
    root.randomNumButtonClicked.connect(some_context.get_random_number)
    some_context.randint_ready.connect(root.updateLabel)
    
    sys.exit(app.exec())
