from PyQt6.QtWidgets import (QApplication, 
    QVBoxLayout, QHBoxLayout, QWidget, QPushButton,
    QListView, QLineEdit)
    
from PyQt6.QtCore import Qt, QAbstractListModel
from PyQt6.QtGui import QImage

import sys


class TodoModel(QAbstractListModel):
    
    def __init__(self, *args, todos=None, **kwargs):
        
        super(TodoModel, self).__init__(*args, **kwargs)
        self.todos = todos or []
        self.tick = QImage('tick.png')
        
    def data(self, index, role):
        
        if role == Qt.ItemDataRole.DisplayRole:
            status, text = self.todos[index.row()]
            return text
        
        if role == Qt.ItemDataRole.DecorationRole:
            status,text = self.todos[index.row()]
            if status:
                return self.tick
            
    def rowCount(self, index):
        return len(self.todos)



class MainWindow(QWidget):
    
    def __init__(self):
        
        super().__init__()
        self.resize(300, 300)
        self.setWindowTitle('PyQt6 Template')
        
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(self.layout)
        
        self.todoView = QListView()
        self.layout.addWidget(self.todoView)
        
        self.del_complete_layout = QHBoxLayout()
        self.del_complete_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.deleteButton = QPushButton('Delete')
        self.del_complete_layout.addWidget(self.deleteButton)
        
        self.completeButton = QPushButton('Complete')
        self.del_complete_layout.addWidget(self.completeButton)
        
        self.layout.addLayout(self.del_complete_layout)
        
        self.todoEdit = QLineEdit()
        self.layout.addWidget(self.todoEdit)
        
        self.addButton = QPushButton('Add Todo')
        self.layout.addWidget(self.addButton)
        
        self.model = TodoModel()
        self.todoView.setModel(self.model)
        
        self.addButton.pressed.connect(self.add)
        self.deleteButton.pressed.connect(self.delete)
        self.completeButton.pressed.connect(self.complete)
        
    def add(self):
        text = self.todoEdit.text()
        if text:
            self.model.todos.append((False, text))
            self.model.layoutChanged.emit()
            self.todoEdit.setText('')
            
    def delete(self):
        indexes = self.todoView.selectedIndexes()
        if indexes:
            index = indexes[0]
            del self.model.todos[index.row()]
            self.model.layoutChanged.emit()
            self.todoView.clearSelection()
            
    def complete(self):
        indexes = self.todoView.selectedIndexes()
        if indexes:
            index = indexes[0]
            row = index.row()
            status, text = self.model.todos[row]
            self.model.todos[row] = (True, text)
            self.model.dataChanged.emit(index, index)
            self.todoView.clearSelection()

        
        
app = QApplication(sys.argv)


main_window = MainWindow()
main_window.show()
sys.exit(app.exec())
