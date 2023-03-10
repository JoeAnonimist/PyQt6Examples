import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QProgressBar
from PyQt6.QtCore import QThread, QObject, pyqtSignal as Signal, pyqtSlot as Slot
import time


class Worker(QObject):
    
    progress = Signal(int)
    completed = Signal(int)
    
    def __init__(self):
        super().__init__()
        self.cancel = False

    @Slot(int)
    def do_work(self, n):
        for i in range(1, n+1):
            print(self.cancel)
            if self.cancel:
                break
            time.sleep(1)
            self.progress.emit(i)

        self.completed.emit(i)
        
    @Slot()
    def cancel_work(self):
        print('in cancel work')
        self.cancel = True
        print(self.cancel + ' --- ')


class MainWindow(QMainWindow):
    
    work_requested = Signal(int)
    work_canceled = Signal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setGeometry(100, 100, 300, 50)
        self.setWindowTitle('QThread Demo')

        # setup widget
        self.widget = QWidget()
        layout = QVBoxLayout()
        self.widget.setLayout(layout)
        self.setCentralWidget(self.widget)       

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setValue(0)

        self.btn_start = QPushButton('Start', clicked=self.start)
        self.btn_stop = QPushButton('Stop', clicked=self.stop)

        layout.addWidget(self.progress_bar)
        layout.addWidget(self.btn_start)
        layout.addWidget(self.btn_stop)

        self.worker = Worker()
        self.worker_thread = QThread()

        self.worker.progress.connect(self.update_progress)
        self.worker.completed.connect(self.complete)

        self.work_requested.connect(self.worker.do_work)
        self.work_canceled.connect(self.worker.cancel_work)

        # move worker to the worker thread
        self.worker.moveToThread(self.worker_thread)

        # start the thread
        self.worker_thread.start()

        # show the window
        self.show()

    def start(self):
        self.btn_start.setEnabled(False)
        n = 10
        self.progress_bar.setMaximum(n)
        self.work_requested.emit(n)
        
    def stop(self):
        print('in stop method')
        self.work_canceled.emit()
        self.worker.cancel_work()

    def update_progress(self, v):
        self.progress_bar.setValue(v)

    def complete(self, v):
        self.progress_bar.setValue(v)
        self.btn_start.setEnabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
