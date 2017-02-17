from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout

Builder.load_string("""
<Calc>:
   
    a: _a
    b: _b
    result: _result
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        ScreenManager:
            size_hint: 1, .9
            id: _screen_manager
            Screen:
                name: 'screen1'
                GridLayout:
                    cols:1
                    TextInput:
                        id: _a
                        text: 'Enter one number'
                    TextInput:
                        id: _b
                        text: 'Enter second number'
                    Label:
                        id: _result
                    
                
                    Button:
                        text:'Sum'
                        on_press: _result.text = str(int(_a.text) +int(_b.text))
                    Button:
                        text:'Product'
                        on_press: _result.text = str(int(_a.text) *int(_b.text))

            Screen:
                name: 'screen2'
                GridLayout:
                    cols:1
                    TextInput:
                        id: _a
                        text: 'Enter one number'
                    TextInput:
                        id: _b
                        text: 'Enter second number'
                    Label:
                        id: _result
                   
                
                    Button:
                        text:'Difference'
                        on_press: _result.text = str(int(_a.text) -int(_b.text))
                    Button:
                        text:'Divide'
                        on_press: _result.text = str(int(_a.text) /int(_b.text))
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'bottom'
        BoxLayout:
            orientation: 'horizontal'
            size_hint: 1, .1
            Button:
                text: 'Go to Screen 1'
                on_press: _screen_manager.current = 'screen1'
            Button:
                text: 'Go to Screen 2'
                on_press: _screen_manager.current = 'screen2'""")

class Calc(FloatLayout):
   
    def product(self, instance):
        
        self.result.text = str(int(self.a.text) * int(self.b.text))

class TestApp(App):
    def build(self):
        return Calc()

if __name__ == '__main__':
    TestApp().run()
