from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
root=Builder.load_string('''
BoxLayout:
    orientation:'vertical'
    Label:
        text:'HELLO WORLD'
    Button:
        text:'Submit'
        ''')
class Hello1(App):
    
    
    def build(self):
        return root

    
if __name__ == "__main__":
    Hello1().run()
