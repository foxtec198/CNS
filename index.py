from PyQt5 import QtWidgets as qw, uic
from qdarktheme import setup_theme as set
from main import Consulta
from time import strftime as st

class Front():
    def __init__(self):
        app = qw.QApplication([])
        set()

        self.login = uic.loadUi('src/login.ui')
        self.main = uic.loadUi('src/main.ui')

        self.boxCr = self.main.boxCr
        self.boxServico = self.main.boxServico
        self.boxGerente = self.main.boxGerente
        self.boxRegional = self.main.boxRegional

        self.login.show()

        # CALLBACK
        self.login
        app.exec()
        
    def run(self):
        c = Consulta()

        c.CRs()

        self.boxCr.addItems([''])
        self.boxServico.addItems([''])
        self.boxGerente.addItems([''])
        self.boxRegional.addItems([''])

        for i in c.contratos:
            self.boxCr.addItems(i)
        for i in c.servicos:
            self.boxServico.addItems(i)
        for i in c.gerentes:
            self.boxGerente.addItems(i)
        for i in c.regionais:
            self.boxRegional.addItems(i)

Front()