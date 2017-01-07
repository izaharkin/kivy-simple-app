from kivy.App import App

from kivy.uix.scatter import scatter
from kivy.uix.label import label
from kivy.uix.FloatLayout import FloatLayout

class HelloApp(App):
    def build(self):
        f = FloatLayout()
        s = scatter()
        l = label(text="Hello, World!",
                  font_size=150)
        f.add_widget(s)
        s.add_widget(l)
        return f

if __name__ == "__main__":
    HelloApp().run()
