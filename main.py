from pyodbc import connect
import requests, json
from tkinter import messagebox as msg

class Consulta():
    def __init__(self):
        self.xSenha = 0
        self.numeroDeTentativas = 3
        
    def dados(self):
        ...

    def DB(self):
        driver = '{SQL Server}'
        strConn = f"DRIVER={driver}; SERVER={self.server}; UID={self.user}; PWD={self.pwd}"
        self.conex = connect(strConn)
        self.c = self.conex.cursor()
        
    def login(self):
        user = 'guilherme.breve'
        passw = '8458@Guilherme'
        r = requests.get('https://db-geradorqr-default-rtdb.firebaseio.com/.json')
        d = json.loads(r.text)
        d = d['login']
        
        for i in d:
            users = d[i]
            if user == users['user']:
                self.server = users['server']
                self.user = users['user']
                self.pwd = users['pwd']
                if self.pwd == passw:
                    self.xSenha = 0
                    msg('Login','Logado com sucesso')
                    self.DB()
                    break
                else:
                    if self.xSenha == 2: # 3x é o numero de tentativas
                        print('Numero de tentativas execedidas, tente redefenir sua senha')
                        break
                    else:
                        print('Senha incorreta')
                        print(f'Voce ainda tem {self.numeroDeTentativas} tentativas')
                        self.numeroDeTentativas -= 1
                        self.xSenha += 1
                        self.login()
                    break
            else:
                print('Usuário Incorreto')
        
    def cadastroUser(self, userP, pwd, server):
        d = {'user':userP, 'server':server, 'pwd':pwd}
        dados = requests.get('https://db-geradorqr-default-rtdb.firebaseio.com/.json')
        dados = json.loads(dados.text)
        dados = dados['login']
        
        self.totalDeUsuarios = len(dados)
        self.contx = 0
        for i in dados:
            key = dados[i]
            self.contx += 1
            if userP == key['user']:
                r = requests.patch(f'https://db-geradorqr-default-rtdb.firebaseio.com/login/{i}.json', json=d)
                print('LOGIN ATUALIZADO')
                break
            elif self.contx == self.totalDeUsuarios:
                r = requests.post(f'https://db-geradorqr-default-rtdb.firebaseio.com/login.json', json=d)
                print('LOGIN REALIZADO')
                break
    
    def CRs(self):
        self.login()
        self.contratos = self.c.execute("SELECT DISTINCT Nivel_03 FROM DW_Vista.dbo.DM_Estrutura").fetchall()
        self.servicos = self.c.execute("SELECT DISTINCT Servico FROM DW_Vista.dbo.DM_Servico").fetchall()
        self.gerentes = self.c.execute("SELECT DISTINCT Gerente FROM DW_Vista.dbo.DM_CR").fetchall()
        self.regionais = self.c.execute("SELECT DISTINCT DiretorRegional FROM DW_Vista.dbo.DM_CR").fetchall()

c = Consulta().login()