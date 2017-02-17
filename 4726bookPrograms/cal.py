from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout

root=Builder.load_string("""
FloatLayout:
    
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        ScreenManager:
            size_hint: [1, .9]
            id: _screen_manager
            Screen:
                name: 'screen1'
                GridLayout:
                    cols:4
                    padding:50
                    Button:
                        text:'1'
                        id:_a
                        on_press:print 'you pressed 1'
                    Button:
                        text:'2'
                        id:_b
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
                    Label:
                        id:_result
                    Button:
                        text:'sum'
                        on_press: _result.text = str(int(_a.text) + int(_b.text))
                    Label:
                        id:_result
                    Button:
                        text:'Difference'
                        on_press: _result.text = str(int(_a.text) - int(_b.text))
                    Label:
                        id:_result
                    
                    Button:
                        text:'Difference'
                        on_press: _result.text = str(int(_a.text)* int(_b.text))

               
            Screen:
                name:'screen2'
                Label:
                    text:'hello'
                    """)
class Test1App(App):
    def build(self):
        return root
if __name__ == '__main__':
    Test1App().run()

                
                
