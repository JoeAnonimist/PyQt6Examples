# The QQuickView class provides a window 
# for displaying a Qt Quick user interface

import sys
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine


if __name__ == '__main__':
    
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine('01_rectangle.qml')
    sys.exit(app.exec())
