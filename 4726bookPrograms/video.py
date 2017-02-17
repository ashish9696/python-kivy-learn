import kivy
kivy.require('1.4.0')
 
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.videoplayer import VideoPlayer
     
parent= Widget()
button= Button()
         
class MyApp(App):
    def build(self):
         button = Button(text='Play video', font_size=14)
         button.bind(on_press=on_button_press)  
         parent.add_widget(button) 
         return parent
               
def on_button_press(self):
        video= VideoPlayer(source='C:\Users\Admin\Desktop\videos\Data Analysis.wmv', state='play')
        parent.add_widget(video) 
        return parent
     
if __name__ == '__main__':
    MyApp().run()
