
import sys
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication
from PyQt6.QtQuick import QQuickView, QQuickItem



if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    view = QQuickView()
    view.setSource(QUrl('02_text.qml'))
    view.show()
    
    sys.exit(app.exec())
