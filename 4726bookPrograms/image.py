from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder


root=Builder.load_string('''
BoxLayout:
    Image:
        source:'C:\Users\Admin\Desktop\login-page1.png'
        ''')

class MainApp(App):

    def build(self):
        return root

if __name__ == '__main__':
    MainApp().run()
