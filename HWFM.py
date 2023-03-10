# The QSplitter class implements a splitter widget.
# A splitter lets the user control the size of 
# child widgets by dragging the boundary between them. 
# Any number of widgets may be controlled by a single splitter. 

from PyQt6.QtWidgets import (QApplication, 
    QWidget, QHBoxLayout, QVBoxLayout, QSplitter, QGroupBox, 
    QPushButton, QTreeWidget, QTreeWidgetItem, QLabel)
from PyQt6.QtCore import Qt
import sys
from binarytree import Node


class QFileWidget(QWidget):
    
    i = 0
    
    def __init__(self, parent):
        
        super().__init__(parent)
        self.setLayout(QVBoxLayout())

        self.splitter = QSplitter()
        self.layout().addWidget(self.splitter)

        self.other_widget = QLabel(str(self.i))
        self.i = self.i + 1
        self.layout().addWidget(self.other_widget)


class QFileManager(QWidget):
    
    def __init__(self):
        
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.widget = QFileWidget(self)
        self.root = Node(self.widget)
        self.layout.addWidget(self.widget)


if __name__ == '__main__':

    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()

    main_window = QFileManager()
    main_window.show()

    sys.exit(app.exec())
