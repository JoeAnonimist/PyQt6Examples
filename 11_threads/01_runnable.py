# https://doc.qt.io/qt-6/threads-technologies.html
#
# Run a new linear function within another thread, 
# optionally with progress updates during the run.
#
# Place the function in a reimplementation of 
# QRunnable::run() and add the QRunnable to a QThreadPool. 
# Write to a thread-safe variable to update progress. 

from PyQt6.QtWidgets import (QApplication, 
    QWidget, QVBoxLayout, QPushButton, QTextEdit)
from PyQt6.QtCore import (QObject, QThreadPool, 
    QRunnable, QThread, pyqtSlot, pyqtSignal)
import sys
import threading

# https://www.riverbankcomputing.com/static/Docs/PyQt5/signals_slots.html
# It appears you can add signals only to direct QObject subclasses,
# so use separate class to hold signals.

class Signals(QObject):
    
    started = pyqtSignal(str)
    completed = pyqtSignal(str)

# 1 - Create a QRunnable subclass and put the task
#     in its run() method.

class SomeTask(QRunnable):

    def __init__(self):
        super().__init__()
        self.signals = Signals()
        
    def run(self):
        
        # Communicate with the main thread using signals
        
        self.signals.started.emit('Started in: ' + 
            str(threading.current_thread().ident))
        
        # Run your task
        
        print('Running some task . . .')
        QThread.sleep(3)
        
        self.signals.completed.emit('Completed in ' +
            str(threading.current_thread().ident))


class Window(QWidget):

    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        start_button = QPushButton('Start the task')
        layout.addWidget(start_button)
        
        # Record the thread in which the task is run.
        
        self.progress_report = QTextEdit()
        self.progress_report.setReadOnly(True)
        layout.addWidget(self.progress_report)
        
        self.progress_report.append('main thread id: ' 
            + str(threading.current_thread().ident))
        self.progress_report.append(
            '----------------------------------------')
        
        start_button.clicked.connect(self.run_task)

    def run_task(self):
        
        # 2 - Create the worker instance

        worker = SomeTask()
        
        worker.signals.started.connect(self.update)
        worker.signals.completed.connect(self.update)
        
        # https://doc.qt.io/qt-6/threads-synchronizing.html
        # If signals and slots are used exclusively 
        # and no variables are shared between threads, 
        # a multithreaded program can do without 
        # low-level primitives altogether.
        
        # Connection type defaults to Qt.AutoConnection.
        # If the receiver lives in the thread 
        # that emits the signal, Qt.DirectConnection is used. 
        # Otherwise, Qt.QueuedConnection is used. 
        
        # 3 - Add the instance to a QThreadPool.
        #     Here I add the worker to the global thread pool.
        #     The thread pool takes ownership
        #     and deletes the instance automatically.

        QThreadPool.globalInstance().start(worker)
        
    def update(self, message):

        self.progress_report.append(message)
        self.progress_report.append(
            'Active threads: ' +
            str(QThreadPool.globalInstance().activeThreadCount()))


if __name__ == '__main__':

    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())
