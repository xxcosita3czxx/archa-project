import webview
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


KV = '''
BoxLayout:
    orientation: 'vertical'
    padding: 20
    spacing: 20

    MDLabel:
        text: "Click the button to open a website in the app"
        halign: 'center'
        size_hint_y: None
        height: self.texture_size[1]
    
    Button:
        text: "Open Website"
        size_hint: (None, None)
        size: (200, 50)
        pos_hint: {'center_x': .5}
        on_release: app.open_website()
'''

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def open_website(self):
        # Opens the website in a window within the app
        webview.create_window('Website', 'http://localhost:5000')
        webview.start()

MainApp().run()
