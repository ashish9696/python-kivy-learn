from kivy.uix.progressbar import ProgressBar
from kivy.app import App
pb = ProgressBar(max=1000)

# this will update the graphics automatically (75% done)
pb.value = 750
class Test4App(App):
  
            
    def build(self):
        return pb
if __name__ == '__main__':
    Test4App().run()
