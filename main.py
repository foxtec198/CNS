from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import Screen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.label import MDLabel
from kivymd.toast import toast
from time import sleep
from sqlite3 import connect
from time import time
import pyodbc

class Login(Screen):...

class Main(Screen):...

class hide:
    def __init__(self, id):
        id.opacity = 0

class LGC:
    def __init__(self):
        self.temp = connect('src/temp.db')
        self.c = self.temp.cursor()
    
    def cons(self):
        self.dd = self.c.execute('select * from temp order by Id DESC').fetchone()
    
    def ins(self, uid, pwd, server):
        self.cons()
        self.c.execute(f'delete from temp where Id <> {self.dd[0]}')
        self.c.execute(f'insert into temp(user, pwd, server) values("{uid}","{pwd}","{server}")')
        self.temp.commit()
    def delete(self):
        self.c.execute(f'delete from temp where Id <> {self.dd[0]}')
        self.temp.commit()
        
    def loginSql(self, server, uid, pwd, driver="{ODBC Driver 17 for SQL Server}"):
        if server != '' and uid != '' and pwd != '':
            try:
                conSql = pyodbc.connect(f'DRIVER={driver};SERVER={server};UID={uid};PWD={pwd}')
                self.c2 = conSql.cursor()
                return True
            except: return False
        else: return False
        
class CNS(MDApp):
    def build(self):
        Builder.load_file('src/style.kv')
        sm = MDScreenManager()
        th = self.theme_cls
        th.theme_style = 'Dark'
        th.primary_palette = 'Red'
        sm.add_widget(Login())
        sm.add_widget(Main())
        self.title = 'CNS'
        # self.icon = 'src/img/icon.ico'
        return sm
    
    def on_start(self):
        # self.root.current = 'loginWin'
        self.root.current = 'mainWin'
        self.idsLogin = self.root.get_screen('loginWin').ids
        self.idsMain = self.root.get_screen('mainWin').ids
        lgc.cons()
        if lgc.dd != None:
            self.idsLogin.salvarUser.active = True
            self.idsLogin.user.text = lgc.dd[1]
            self.idsLogin.pwd.text = lgc.dd[2]
            self.idsLogin.server.text = lgc.dd[3]

        
    def login(self):
        if self.idsLogin.salvarUser.active: lgc.ins()
        else: lgc.delete()
        s = self.idsLogin.server.text
        u = self.idsLogin.user.text
        p = self.idsLogin.pwd.text
        self.lg = lgc.loginSql(server=s, uid=u, pwd=p)
        if self.lg: 
            toast('Logado com sucesso')
            self.root.current = 'mainWin'
        else:
            toast('Credenciais Invalidas')
            
        
lgc = LGC()
CNS().run()