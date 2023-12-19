from PyQt5 import QtWidgets as qw, uic
from qdarktheme import setup_theme as set


app = qw.QApplication([])
main = uic.loadUi('src/main.ui')
set()

qf = qw.QFileDialog

main.show()
app.exec()