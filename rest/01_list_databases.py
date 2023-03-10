
import sys
import psycopg2

from PyQt6.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem


data = ('Project A', 'Project B', 'Project C')

app = QApplication(sys.argv)
app.setStyle('Fusion')
tree = QTreeWidget()
tree.setColumnCount(1)
tree.setHeaderLabels(['Name'])


conn = psycopg2.connect(
    host='localhost',
    database='pagila',
    user='jon')

sql = 'SELECT datname FROM pg_database'
cursor = conn.cursor()
cursor.execute(sql)
rows = cursor.fetchall()

items = []

for row in rows:
    
    item = QTreeWidgetItem([row[0]])
    items.append(item)
    
tree.insertTopLevelItems(0, items)

tree.show()
sys.exit(app.exec())
