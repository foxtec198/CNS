from PyQt5 import QtWidgets as qw, uic
from qdarktheme import setup_theme as set


app = qw.QApplication([])
main = uic.loadUi('src/main.ui')
set()

tab = main.tableCons

tab.setRowCount(1)

for i in range(0, 14):
    tab.setItem(0, i, qw.QTableWidgetItem(str('teste')))

main.show()
app.exec()