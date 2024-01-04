from PyQt5 import QtWidgets as qw, uic, QtCore
from qdarktheme import setup_theme as set
from time import strftime as st
from pyodbc import connect
from sqlite3 import connect as sq
import json
from openpyxl import load_workbook as lw

class Consulta():
    def __init__(self):
        self.xSenha = 0
        self.numeroDeTentativas = 3
        self.conn = sq('src/temp.db')
        self.cursor = self.conn.cursor()
        self.valor = 10
        self.valorMain = 10
        set()
        self.year = int(st('%Y'))
        self.month = int(st('%m'))
        self.day = int(st('%d'))
        
    def action(self, sqlCons):
        self.cursor.execute(sqlCons)
        self.conn.commit()

    def DB(self, server, user, pwd):
        driver = '{SQL Server}'
        strConn = f"DRIVER={driver}; SERVER={server}; UID={user}; PWD={pwd}"
        self.conex = connect(strConn)
        self.cursorSQL = self.conex.cursor()
    
    
    def msg(self, windown, msg, type = 1):
        tt = 'CNS'
        if type == 1:
            qw.QMessageBox.information(windown, tt, msg)
        elif type == 2:
            qw.QMessageBox.about(windown, tt, msg)
        if type == 3:
            qw.QMessageBox.warning(windown, tt, msg)
        
    def clear(self):
        boxCr.setCurrentText('')
        boxServico.setCurrentText('')


    def login(self):
        frameTop.show()
        server = entry_server.text()
        user = entry_user.text()
        pwd = entry_pwd.text()
        nome = user.replace('.',' ')
        nome = nome.split()
        self.addValue()
        if entry_saveUser.isChecked():
            c.action(f"INSERT INTO temp(server, user, pwd) VALUES ('{server}','{user}','{pwd}')")
            self.addValue()
        else:
            c.action("DELETE FROM temp")
            self.addValue()
        try:
            self.DB(server, user, pwd)
            self.run()
            self.msg(login, f'Login Realizado com sucesso! \nSeja bem vindo {nome[0]}')
            login.close()
            main.show()
        except:
            self.msg(login, f'Login não Realizado com sucesso! \nRevise o VPN e as Credenciais!', 3)

    def CRs(self):
        self.addValue()
        self.servicos = self.cursorSQL.execute("SELECT DISTINCT Servico FROM DW_Vista.dbo.DM_Servico").fetchall()
        self.addValue()
        self.contratos = self.cursorSQL.execute("SELECT DISTINCT Nivel_03 FROM DW_Vista.dbo.DM_Estrutura Es INNER JOIN DW_Vista.dbo.DM_CR CR on CR.ID_CR = Es.ID_CR WHERE CR.DiretorRegional = 'CLEVERSON DUTRA ZONTINI'").fetchall()
        self.addValue()

    def run(self):
        self.CRs()
        self.addValue()
        for i in c.contratos:
            boxCr.addItems(i)
        self.addValue()
        for i in c.servicos:
            boxServico.addItems(i)
        self.addValue()
    
    def zerar(self):
        tab.setRowCount(0)
            
    def consulta(self):
        mainBar.show()
        cr = boxCr.currentText()
        if cr != '':
            servico = boxServico.currentText()
            self.addValueBarMain()

            dataI = str(di.date())
            dataI = dataI[18:]
            dataI = dataI.replace('(','[')
            dataI = dataI.replace(')',']')
            dataI = json.loads(dataI)
            self.addValueBarMain()

            dataF = str(df.date())
            dataF = dataF[18:]
            dataF = dataF.replace('(','[')
            dataF = dataF.replace(')',']')
            dataF = json.loads(dataF)
            self.addValueBarMain()
            
            cons = self.cursorSQL.execute(f"""SELECT
            T.Numero,
            T.Nome,
            S.Servico,
            R.Recurso AS 'COLABORADOR',
            CR.Gerente,
            T.InicioReal,
            T.TerminoReal,
            T.Disponibilizacao,
            ES.Descricao AS 'Local',
            R.PerguntaDescricao AS 'Pergunta',
            R.Conteudo AS 'Resposta',
            E.Longitude_F,
            E.Latitude_F,
            ES.HIERARQUIADESCRICAO AS 'ESTRUTURA COMPLETA'
            FROM DW_VISTA.DBO.FT_TAREFA T WITH(NOLOCK)
            INNER JOIN DW_VISTA.DBO.FT_CHECKLIST_RESPOSTA_FULL R ON R.TarefaId = T.Id
            INNER JOIN DW_VISTA.DBO.DM_EXECUCAO E ON E.TarefaId = T.Id
            INNER JOIN DW_VISTA.DBO.DM_ESTRUTURA ES ON ES.Id_Estrutura = T.Id_Estrutura
            INNER JOIN DW_VISTA.DBO.DM_CR CR ON CR.Id_CR = ES.Id_CR
            inner JOIN DW_VISTA.DBO.DM_SERVICO S ON S.Id_Servico = T.Id_Servico
            WHERE Es.Nivel_03 = '{cr}'
            AND DAY(DISPONIBILIZACAO) >= {dataI[2]} 
            AND DAY(DISPONIBILIZACAO) <= {dataF[2]} 
            
            AND MONTH(DISPONIBILIZACAO) >= {dataI[1]} 
            AND MONTH(DISPONIBILIZACAO) <= {dataF[1]} 
            
            AND YEAR(DISPONIBILIZACAO) >= {dataI[0]} 
            AND YEAR(DISPONIBILIZACAO) <= {dataF[0]} """)
            self.addValueBarMain()
            self.tabela = cons.fetchall()
            self.addValueBarMain()

            # FILTRAR POR SERVIÇO
            if servico != '':
                for row in self.tabela:
                    if servico == row[2]:
                        self.tabela = self.tabela
                    else:
                        self.tabela = None
                        
            # 14 COLUNAS - X LINHAS 
            if self.tabela != None:
                x = 0
                for i in self.tabela:
                    x += 1
                    self.addValueBarMain()
                tab.setRowCount(x)
                linhas.setText(f'{x} Linhas')
                row = 0
                for r in self.tabela:
                    for c in range(0,14):
                        self.addTab(row, c, r[c])
                    row += 1
                    self.addValueBarMain()
                mainBar.hide()
            else:
                self.msg(main, 'Valores não encontrados! Tente novamente')
        else:
            self.msg(main, 'A estrutura de local não pode ficar em branco, selecione ao menos uma !!!!', 3)

    def addTab(self, row, column, item):
        tab.setItem(row, column, qw.QTableWidgetItem(str(item)))    

    def addValue(self):
        bar.setValue(self.valor)
        self.valor += 10
        
    def addValueBarMain(self):
        mainBar.setValue(self.valorMain)
        self.valorMain += 10

    def salvar(self):
        if tab.rowCount() != 0:
            diretorio = QFile.getSaveFileName()
            ws = lw(diretorio)
            linha = 0
            for row in self.tabela:
                ...
                
        else:
            self.msg(main, 'Primeiro realize uma consulta!', 3)
        
app = qw.QApplication([])
c = Consulta()
login = uic.loadUi('src/login.ui')
main = uic.loadUi('src/main.ui')

# WIDGETS
boxCr = main.boxCr
boxServico = main.boxServico
df = main.dataFinal
di = main.dataInicial
tab = main.tableCons
linhas = main.totalLinhas
mainBar = main.mainBar
QFile = qw.QFileDialog

entry_saveUser = login.saveUser
entry_server = login.entryServer
entry_user = login.entryUser
entry_pwd = login.entryPwd
bar = login.bar
frameTop = login.TOP


# CALLBACK
login.btnLogin.clicked.connect(c.login)
main.btnLimparTabela.clicked.connect(c.zerar)
main.btnLimpar.clicked.connect(c.clear)
main.btnConsulta.clicked.connect(c.consulta)
main.btnExcel.clicked.connect(c.salvar)

dados = c.cursor.execute('SELECT * FROM temp ORDER BY Id DESC').fetchone()
if dados != None:
    c.action(f'DELETE FROM temp WHERE Id <> "{dados[0]}"')
    entry_user.setText(dados[1])
    entry_pwd.setText(dados[2])
    entry_server.setText(dados[3])
    entry_saveUser.setChecked(True)

d = QtCore.QDate(c.year, c.month, c.day)

di.setDate(d)
df.setDate(d)

frameTop.hide()
mainBar.hide()
login.show()
boxCr.addItems([''])
boxServico.addItems([''])

app.exec()