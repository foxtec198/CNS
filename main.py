from PyQt5 import QtWidgets as qw, uic
from pyodbc import connect
import requests, json
from os import system

class Consulta():
    def __init__(self):
        self.xSenha = 0
        self.numeroDeTentativas = 3
        
    def dados(self):
        ...

    def DB(self):
        self.conex = connect(f"DRIVER = SQL Driver;SERVER = {self.server}; UID = {self.user}; PWD = {self.pwd}")
        self.c = self.conex.cursor()
        
    def login(self):
        user = input('user: ')
        passw = input('pwd: ')
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
                    print('Logado com sucesso')
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

c = Consulta()
        
c.login()