from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivymd.uix.button import MDFlatButton
from kivymd.uix.screen import MDScreen
import webview

Builder.load_string("""
<MyWebView>
    MDFlatButton:
        text: "Push"
        pos_hint: {"center_x": .5, "center_y": .4}
        on_press: root.Push()
""")

class MyWebApp(MDApp):
    def build(self):
        webview.create_window('Hello world', 'https://pywebview.flowrl.com/hello')
        webview.start()

if __name__ == '__main__':
    MyWebApp().run()