from PyQt5 import QtWidgets as qw, uic
from pyodbc import connect
import requests, json

class Consulta():
    def db(self):
        ...
        
    def dados(self):
        ...
        
    def login(self):
        user = input('user: ')
        pwd = input('pwd: ')
        r = requests.get('https://db-geradorqr-default-rtdb.firebaseio.com/login.json')

    def cadastroUser(self, user, pwd, server):
        d = {'user':user,
             'server':server, 
             'pwd':pwd}
        r = requests.post(f'https://db-geradorqr-default-rtdb.firebaseio.com/login.json', json=d)
        print(r.text)
        
Consulta().login()