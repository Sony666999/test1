from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTextEdit, QPushButton, QTableWidget, QTableWidgetItem
import sys
from library import *

app = QtWidgets.QApplication([])
win = uic.loadUi("рабочие.ui")

gr = grup()
gr.read_data_from_file("text.txt")
print("!!!", gr.count)

sti = QtWidgets.QStandardItemModel(parent=win)
win.tableWidget = QtWidgets.QModelIndex()
win.label.setAlignment(QtCore.Qt.AlignHCenter)

def btn_load_table():
    win.tableWidget.setRowCount(gr.count)
    row = 0
    for x in gr.a:
        print(1)

        win.tableWidget.setItem(row, 0, QTableWidgetItem(gr.a[x].fam+' '+gr.a[x].name+' '+gr.a[x].otchestvo))
        win.tableWidget.setItem(row, 1, QTableWidgetItem(str(gr.a[x].year)))
        win.tableWidget.setItem(row, 2, QTableWidgetItem(gr.a[x].city))
        win.tableWidget.setItem(row, 3, QTableWidgetItem(str(gr.a[x].sb_inf)))
        win.tableWidget.setItem(row, 4, QTableWidgetItem(str(gr.a[x].sb_math))
        row += 1

def btn_append_person():
    str_person = win.lineEdit.text()
    gr.append_person(str_person)
    win.tableWidget.clear()
    btn_load_table()

win.pushButton.clicked.connect(btn_load_table)
print(gr.a[0].get_person_for_table())

win.pushButton_3.clicked.connect(btn_append_person)

win.show()
sys.exit(app.exec())
