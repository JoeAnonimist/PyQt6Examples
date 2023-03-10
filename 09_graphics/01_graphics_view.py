# The QGraphicsView class provides a widget 
# for displaying the contents of a QGraphicsScene

from PyQt6.QtWidgets import (QApplication, 
    QWidget, QVBoxLayout, QGraphicsView, QGraphicsScene)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPen, QBrush, QColor
import sys


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 1 - Create the graphics view
        
        graphics_view = QGraphicsView()
        layout.addWidget(graphics_view)
        
        width = graphics_view.frameGeometry().width()
        height = graphics_view.frameGeometry().height()
        
        # 2 - Create the graphics scene
        
        scene = QGraphicsScene()
        scene.setSceneRect(0.0, 0.0, float(width), float(height))
        
        # 3 - Add shapes to the scene
        
        # This draws a rectangle
        
        scene.addRect(100, 100, 150, 150)
        
        # Draw a circle
        
        pen = QPen(Qt.PenStyle.SolidLine)
        pen.setColor(Qt.GlobalColor.red)
        brush = QBrush(Qt.BrushStyle.Dense3Pattern)
        brush.setColor(Qt.GlobalColor.darkGreen)
        scene.addEllipse(300, 300, 100, 100, pen, brush)
        
        # 4 - Set the scene as the graphics view scene
        
        graphics_view.setScene(scene)


if __name__ == '__main__':

    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())
