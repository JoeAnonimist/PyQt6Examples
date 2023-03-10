# https://doc.qt.io/qt-6/threads-technologies.html

# Have an object living in another thread 
# that can perform different tasks upon request 
# and/or can receive new data to work with.

# Subclass a QObject to create a worker. 
# Instantiate this worker object and a QThread. 
# Move the worker to the new thread. 
# Send commands or data to the worker object 
# over queued signal-slot connections.

from PyQt6.QtWidgets import (QApplication, 
    QWidget, QVBoxLayout, QPushButton, QLabel)
from PyQt6.QtCore import (QObject, QThread, 
    pyqtSignal, pyqtSlot)
import sys
import threading
from random import randint
from datetime import datetime

# 1 - Create a QObject subclass to do the work

class Worker(QObject):
    
    work_done = pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
    
    @pyqtSlot(int)
    def do_work(self, data):
        
        # do the actual work
        
        thread_id = str(threading.current_thread().ident)
        print('Worker thread id: {}'.format(thread_id))
        print('Data sent from main: {}\n'.format(data))
        
        # emit signal when work done
        
        now = datetime.now().strftime('%H:%M:%S')
        self.work_done.emit(now)


class Window(QWidget):
    
    request_work = pyqtSignal(int)
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        print('Main thread id: {}\n'.format(
            str(threading.current_thread().ident)))
        
        button = QPushButton('Do the work')
        layout.addWidget(button)
        
        self.label = QLabel()
        layout.addWidget(self.label)
        
        # 2 - Instantiate the worker object and the thread
        
        # Need the self references so that worker and thread objects
        # don't get destroyed before the Worker instance.

        self.worker_object = Worker()
        self.worker_thread = QThread()
        self.worker_thread.start()
        
        # 3 - Move the worker object to the thread
        
        self.worker_object.moveToThread(self.worker_thread)
        
        # 4 - Use signals and slots to communicate between
        #     with the worker object
        
        # main -> worker : start communicating with the worker
        
        button.clicked.connect(self.start_work)
        
        # main -> worker : the worker actually starts 
        # doing the work only when it receives this signal.
        
        self.request_work.connect(self.worker_object.do_work)
        
        # worker -> main : report work done
        # Send some data from the worker to the main thread.
        
        self.worker_object.work_done.connect(self.report_work)
    
    @pyqtSlot()        
    def start_work(self):
        
        # start_work() does not call Worker.do_work() directly.
        # It emits the request_work signal instead
        
        data = randint(0, 100)
        self.request_work.emit(data)
        
    @pyqtSlot(str)
    def report_work(self, done_time):
        self.label.setText('Work done at: ' + done_time)


if __name__ == '__main__':

    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())
