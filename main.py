from PyQt5 import QtWidgets as qw, uic
from pyodbc import connect
import requests, json
from os import system

class Consulta():
    def __init__(self):
        self.xSenha = 0
        self.numeroDeTentativas = 3

    def db(self):
        ...
        
    def dados(self):
        ...
        
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
                    break
                else:
                    if self.xSenha == 3:
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
                print('Usuário Incorreto!') 
                self.login()
        
    def cadastroUser(self, user, pwd, server):
        d = {'user':user, 'server':server, 'pwd':pwd}
        dados = requests.get('https://db-geradorqr-default-rtdb.firebaseio.com/.json')
        
        for i in dados:
            users = dados[i]
            if user == users['user']:
                # LOGIN ATUALIZADO 
                r = requests.patch(f'https://db-geradorqr-default-rtdb.firebaseio.com/login/{i}/.json', json={'pwd':pwd, 'server':server})
            else:
                # LOGIN REALIZADO
                r = requests.post(f'https://db-geradorqr-default-rtdb.firebaseio.com/login.json', json=d)
        
c = Consulta()
        
c.cadastroUser(user='guilherme.breve', pwd='8458', server='10.56.6.56')
