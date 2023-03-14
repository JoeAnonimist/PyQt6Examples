# The QQuickView class provides a window 

import sys
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication
from PyQt6.QtQuick import QQuickView


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    view = QQuickView()
    view.setSource(QUrl('04_flow.qml'))
    view.show()
    
    sys.exit(app.exec())
