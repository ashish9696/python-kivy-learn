from kivy.uix.slider import Slider
from kivy.uix.pagelayout import PageLayout
from kivy.app import App
from kivy.uix.switch import Switch
switch = Switch(active=True)

class Test4App(App):
  
            
    def build(self):
        return switch
if __name__ == '__main__':
    Test4App().run()
