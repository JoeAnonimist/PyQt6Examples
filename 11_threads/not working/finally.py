

import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGridLayout

from PyQt6.QtCore import QThread, QObject, pyqtSignal


class Window(QWidget):


    def __init__(self):

        super().__init__()
        self.initUi()
        self.show()


    def initUi(self):

        self.button_start = QPushButton(
                'Start long running task')
        self.button_start.clicked.connect(self.run_task)
        
        self.button_stop = QPushButton(
                'Stop long running task')
        self.button_stop.clicked.connect(self.end_task)
        
        self.label = QLabel()

        self.layout = QGridLayout()        
        self.layout.addWidget(self.button_start, 0, 0)
        self.layout.addWidget(self.button_stop, 1, 0)
        self.layout.addWidget(self.label, 2, 0)
        self.setLayout(self.layout)
        
        
    def run_task(self):
        
        self.thread = QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.thread)
        self.worker.incremented.connect(self.set_label_value)        
        
        self.thread.started.connect(self.worker.do_work)
        self.thread.finished.connect(self.thread.deleteLater)        
        
        if not self.thread.isRunning():
            self.thread.start()
            
            
    def end_task(self):
        
        self.worker.stop()
        if self.thread.isRunning():
            self.thread.quit()
            self.label.setText('')
            
            
    def set_label_value(self, value):        
        self.label.setText(value)


class Worker(QObject):
    
    incremented = pyqtSignal(str)
    
    
    def __init__(self, parent=None):

        QObject.__init__(self)
        self.stopped = False
        self.i = 0


    def do_work(self):
        
        while self.i < 30:
            
            QThread.sleep(1)
            
            if not self.stopped:
                print('running . . . ' + str(self.i))
                self.i = self.i + 1
                self.incremented.emit(str(self.i))            
        
    
    def stop(self):
        self.stopped = True



def main(args):

    app = QApplication(args)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main(sys.argv)
