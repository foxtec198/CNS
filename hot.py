from kivymd.tools.hotreload.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import Screen
from kivymd.uix.screenmanager import MDScreenManager

class Login(Screen):...

class HotReload(MDApp):
    KV_FILES = ['src/style.kv']
    DEBUG = True
    def build_app(self):
        sm = MDScreenManager()
        sm.add_widget(Login())
        th = self.theme_cls
        th.theme_style = 'Dark'
        th.primary_palette = 'Blue'
        Builder.load_file('src/style.kv')
        return sm

if __name__ == '__main__': HotReload().run()