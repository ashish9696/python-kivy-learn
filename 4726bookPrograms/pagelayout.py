from kivy.uix.slider import Slider
from kivy.uix.pagelayout import PageLayout
from kivy.app import App
from kivy.uix.switch import Switch
from kivy.lang import Builder

root=Builder.load_string('''
PageLayout:
    Button:
        text: 'page1'
    Button:
        text: 'page2'
    Button:
        text: 'page3' ''')
class Test4App(App):
  
            
    def build(self):
        return root
if __name__ == '__main__':
    Test4App().run()
