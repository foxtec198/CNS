from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import Screen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.toast import toast

class CNS(MDApp):
    def build(self):
        sm = MDScreenManager()
        Builder.load_file('src/style.kv')
        return sm