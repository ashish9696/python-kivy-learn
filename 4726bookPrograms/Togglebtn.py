from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.lang import Builder
root=Builder.load_string('''
GridLayout:
    cols:3
    Label:
        text:'Choice1'
    ToggleButton:
        size_hint:[None,None]
        text:'A'
    ToggleButton:
        size_hint:[None,None]
        text:'B'
    Label:
        text:'Choice2'
    ToggleButton:
        size_hint:[None,None]
        text:'C'
    ToggleButton:
        size_hint:[None,None]
        text:'D'
        ''')
class TutorialApp(App):
    def build(self):
        
        return root

if __name__ == "__main__":
    TutorialApp().run()
