# The QQuickView class provides a window 
# for displaying a Qt Quick user interface

import sys
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication
from PyQt6.QtQuick import QQuickView


if __name__ == '__main__':
    
    # 1 - Create a QApplication object
    
    app = QApplication(sys.argv)
    
    # 2 - Create a QQuickView object
    
    view = QQuickView()
    
    # 3 - Set QQuickView QML source
    
    view.setSource(QUrl('01_hello_world.qml'))
    
    # 4 - Show the QQuickView
    
    view.show()
    
    sys.exit(app.exec())
