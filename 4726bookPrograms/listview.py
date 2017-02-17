from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.base import runTouchApp

Builder.load_string("""
<MyListView>:
    ListView:
        item_strings: [str(index) for index in range(100)]
""")


class MyListView(BoxLayout):
    pass

if __name__ == '__main__':
    runTouchApp(MyListView())
