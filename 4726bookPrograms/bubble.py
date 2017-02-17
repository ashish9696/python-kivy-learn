from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.bubble import Bubble

root=Builder.load_string('''
FloatLayout:
    size_hint: (None, None)
    size: (160, 120)
    pos_hint: {'center_x': .5, 'y': .6}
    BubbleButton:
        text: 'Cut'
    
''')



class TestBubbleApp(App):

    def build(self):
        return root

if __name__ == '__main__':
    TestBubbleApp().run()
