# Qt Style Sheets support various properties, 
# pseudo-states, and subcontrols that make it 
# possible to customize the look of widgets.

from PyQt6.QtWidgets import (QApplication, 
    QWidget, QVBoxLayout, QLabel, QPushButton, 
    QRadioButton, QCheckBox,  QComboBox, 
    QFontComboBox, QLineEdit, QGroupBox, 
    QToolBox, QTabWidget, QScrollArea, 
    QPlainTextEdit, QGridLayout, QVBoxLayout, QSizePolicy)
from PyQt6.QtGui import QTextOption
import sys
from random import randint


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        # 1 - Create some widgets
        
        self.init_ui()
        
        # 2 - Open the stylesheet file
        
        with open('styles.qss', 'r') as stylesheet:
            
            # 3 - Apply the style sheet
            
            self.setStyleSheet(stylesheet.read())
        
    def init_ui(self):
        
        layout = QGridLayout()
        self.setLayout(layout)
        
        vbox_1 = QVBoxLayout()
        
        groupbox_1 = QGroupBox()
        groupbox_1.setObjectName('groupbox_1')
        groupbox_1.setMinimumWidth(260)
        groupbox_1.setLayout(vbox_1)
        
        vbox_2 = QVBoxLayout()
        
        groupbox_2 = QGroupBox()
        groupbox_2.setObjectName('groupbox_2')
        groupbox_2.setLayout(vbox_2)
        
        vbox_3 = QVBoxLayout()
        
        groupbox_3 = QGroupBox()
        groupbox_3.setObjectName('groupbox_3')
        groupbox_3.setLayout(vbox_3)
        
        for i in range(3):
            
            radio_button = QRadioButton(
                    'Sample radio button {}'.format(i))
            vbox_1.addWidget(radio_button)
            
            checkbox = QCheckBox(
                    'Sample checkbox {}'.format(i))
            vbox_2.addWidget(checkbox)
            
            button = QPushButton(
                    'Sample Push button {}'.format(i))
            vbox_3.addWidget(button)
        
        layout.addWidget(groupbox_1, 0, 0)
        layout.addWidget(groupbox_2, 1, 0)
        layout.addWidget(groupbox_3, 2, 0)
        
        toolbox = QToolBox()
        toolbox.setMinimumHeight(200)        
        
        linux_button = QPushButton('Linux')
        windows_button = QPushButton('Windows')       
        toolbox.addItem(linux_button, 'Linux')        
        mac_button = QPushButton('Mac')
        
        toolbox.addItem(windows_button, 'Windows')
        toolbox.addItem(mac_button, 'Mac')
        toolbox.setMinimumHeight(200)        
        
        
        tab_widget = QTabWidget()
        tab_widget.insertTab(
                0, QLabel('Linux'), 'Linux')
        tab_widget.insertTab(
                1, QLabel('Windows'), 'Windows')
        tab_widget.insertTab(
                2, QLabel('Mac'), 'Mac')
        tab_widget.setMinimumHeight(200)
        
        plain_text_edit = QPlainTextEdit()
        plain_text_edit.setWordWrapMode(
                QTextOption.WrapMode.NoWrap)

        scroll_area = QScrollArea()
        scroll_area.setWidget(plain_text_edit)
        scroll_area.setWidgetResizable(True)
        scroll_area.setMinimumHeight(200)        

        
        layout.addWidget(toolbox, 0, 1)
        layout.addWidget(tab_widget, 1, 1)
        layout.addWidget(scroll_area, 2, 1)
        
        scroll_area = QScrollArea()


if __name__ == '__main__':

    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())
