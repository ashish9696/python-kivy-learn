from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
textinput = TextInput(text='Hello world')
class MyApp(App):
    def build(self):
        return textinput

if __name__ == '__main__':
    MyApp().run()
