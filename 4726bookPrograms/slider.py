from kivy.uix.slider import Slider
from kivy.app import App
s = Slider(min=-100, max=100, value=25)
class Test4App(App):
  
            
    def build(self):
        return s
if __name__ == '__main__':
    Test4App().run()
