from kivy.app import App
from kivy.uix.button import Button

class QrApp(App):
    def build(self):
        return Button(text = "TEST_BUTTON", font_size = "60sp")

if __name__ == '__main__':
    QrApp().run()