# The QOpenGLWidget class is a widget 
# for rendering OpenGL graphics.

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtOpenGLWidgets import QOpenGLWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QPen, QBrush, QColor, QOpenGLContext
import sys


class MyOpenGLWidget(QOpenGLWidget):
    
    def __init__(self, parent=None):
        
        super().__init__(parent)
        
    def initializeGL(self):
        
        self.gl = self.context().functions()
        self.gl.glClearColor(1.0, 1.0, 1.0, 1.0)
        self.gl.glClear(self.gl.GL_COLOR_BUFFER_BIT)
        
    def paintEvent(self, event):
        
        painter = QPainter()
        
        painter.begin(self)
        
        self.draw_ellipse(event, painter)
        self.draw_rectangle(event, painter)
        
        painter(end)
        
    def draw_ellipse(self, event, painter):
        
        pen = QPen(Qt.SolidLine)
        pen.setColor(Qt.red)
        brush = QBrush(Qt.Dense3Pattern)
        brush.setColor(Qt.darkGreen)
        
        painter.setPen(pen)
        painter.setBrush(brush)
        painter.drawEllipse(200, 200, 100, 100)
        

    def draw_rectangle(self, event, painter):
        
        pen = QPen(Qt.black, 4, Qt.DashDotLine)
        brush = QBrush(Qt.NoBrush)
        painter.setPen(pen)
        painter.setBrush(brush)
        painter.drawRect(50, 50, 100, 100)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.setMinimumSize(500, 500)
        
        opengl_widget = MyOpenGLWidget()
        layout.addWidget(opengl_widget)


if __name__ == '__main__':

    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())
