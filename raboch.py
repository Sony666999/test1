from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTextEdit, QPushButton, QTableWidget, QTableWidgetItem

from library import *

import sys

app = QApplication([])
win = uic.loadUi("рабочие.ui")

gr = Group()
gr.read_data_from_file("text.txt")
print("!!!", gr.count)

win.tableWidget = QTableWidget()

def btn_load_table():
    row = 0
    for x in gr.a:
        win.tableWidget.setItem(row, 0, QTableWidgetItem(gr.a[x].fam + ' ' + gr.a[x].name + ' ' + gr.a[x].otchestvo))
        win.tableWidget.setItem(row, 1, QTableWidgetItem(str(gr.a[x].year)))
        win.tableWidget.setItem(row, 2, QTableWidgetItem(gr.a[x].city))
        win.tableWidget.setItem(row, 3, QTableWidgetItem(str(gr.a[x].sbinf)))
        win.tableWidget.setItem(row, 4, QTableWidgetItem(str(gr.a[x].sbmath)))
        row += 1

def btn_append_person():
    str_person = win.lineEdit.text()
    gr.append_person(str_person)

win.pushButton.clicked.connect(btn_load_table)
print(gr.a[0].get_person_for_table())

win.show()
sys.exit(app.exec())
