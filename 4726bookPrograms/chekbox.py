import kivy

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout


class MyApp(App):

    def build(self):        

        def on_act(*args):
            print "OK"
            print args[0], args[1]

        parent=Widget()

        layout = GridLayout(rows=1, spacing=5, size_hint_y=None)

        layout.bind(minimum_height=layout.setter('height'))     

        btn1 = CheckBox( size=(25,25), group= "gr1")
        layout.add_widget(btn1) 
        btn1.bind(active= on_act)

        btn2 = CheckBox( size=(25,25), group= "gr1")
        layout.add_widget(btn2) 
        btn2.bind(active= on_act)

        btn3 = CheckBox( size=(25,25), group= "gr1")
        layout.add_widget(btn3)
        btn3.bind(active= on_act)

        btn4 = CheckBox( size=(25,25), group= "gr1")
        layout.add_widget(btn4) 
        btn4.bind(active= on_act)

        parent.add_widget(layout)


        return parent


if __name__ == '__main__':
    MyApp().run()
