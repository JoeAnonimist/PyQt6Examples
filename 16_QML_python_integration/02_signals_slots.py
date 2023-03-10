# https://wiki.qt.io/Qt_for_Python/Connecting_QML_Signals
# Connect QML signal to Python slot. The connecting
# is done in the QML file.

import sys
from random import randint
from PyQt6.QtCore import QObject, pyqtSignal, pyqtSlot
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtQuick import QQuickView


class SomeClass(QObject):
    
    def __init__(self):
        super().__init__()
    
    @pyqtSlot('QString')
    def outputStr(self, s):
        print(s)
        
    @pyqtSlot(int, result=int)
    def get_random_number(self, n):
        return randint(0, n)


if __name__ == '__main__':
    
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    
    some_context = SomeClass()
    
    context = engine.rootContext()
    context.setContextProperty('some_context', some_context)
    
    engine.load('signals_slots.qml')
    
    sys.exit(app.exec())
