from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import  Label
from kivy.lang import Builder
from kivy.uix.textinput import TextInput
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button

Builder.load_string("""
<ScreenUI>:
    orientation: 'lr-bt'
    Button:
        text: 'Button 1'
        size: 100, 100
        size_hint: None, None
    Button:
        text: 'Button 2'
        size_hint: None, None
        size: 200, 100""")

class ScreenUI(StackLayout):
    pass

class WidgetApp(App):

    def build(self):
        app = ScreenUI()
        return app

if __name__ == '__main__':
    WidgetApp().run()
