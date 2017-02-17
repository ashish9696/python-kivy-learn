from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
root=Builder.load_string('''
GridLayout:
    cols:3
    padding:50
    Button:
        text:'1'
        on_press:print 'you pressed 1'
    Button:
        text:'2'
        on_press:print 'you pressed 2'
    Button:
        text:'3'
        on_press:print 'you pressed 3'
    Button:
        text:'4'
        on_press:print 'you pressed 4'
    Button:
        text:'5'
        on_press:print 'you pressed 5'
    Button:
        text:'6'
        on_press:print 'you pressed 6'
    Button:
        text:'7'
        on_press:print 'you pressed 7'
    Button:
        text:'8'
        on_press:print 'you pressed 8'
    Button:
        text:'9'
        on_press:print 'you pressed 9'
''')
class Hello1(App):
    
    
    def build(self):
        return root

    
if __name__ == "__main__":
    Hello1().run()
