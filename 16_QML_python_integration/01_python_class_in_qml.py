# Create a Python class that can be used in QML
# https://www.riverbankcomputing.com/static/Docs/PyQt6/qml.html

import sys
from random import randint
from PyQt6.QtCore import QUrl, QObject, pyqtProperty, QCoreApplication, QFile
from PyQt6.QtWidgets import QApplication
from PyQt6.QtQuick import QQuickView
from PyQt6.QtQml import qmlRegisterType, QQmlComponent, QQmlEngine

# 1 - Create a QObject subclass

class Person(QObject):
    
    def __init__(self, parent=None):
        
        super().__init__(parent)
        
        self._name = ''
        self._shoeSize = 0

    @pyqtProperty('QString')
    def name(self):
        return self._name
        
    @name.setter
    def name(self, name):
        self._name = name
        
    @pyqtProperty(int)
    def shoeSize(self):
        return self._shoeSize
        
    @shoeSize.setter
    def shoeSize(self, shoeSize):
        self._shoeSize = shoeSize
        
    @pyqtProperty(int)
    def my_rand(self):
        return randint(0, 100)


if __name__ == '__main__':
    
    app = QCoreApplication(sys.argv)
    
    qmlRegisterType(Person, 'People', 1, 0, 'Person')
    
    engine = QQmlEngine()
    
    component = QQmlComponent(engine)
    component.loadUrl(QUrl.fromLocalFile('my_man.qml'))
    
    my_man = component.create()

    print(my_man.name)
    print(my_man.shoeSize)
    print(my_man.my_rand)

