from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label

class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        btn_hello = Button(
            text="Click để chào",
            size_hint=(None, None),
            size=(200, 80),
            pos_hint={'center_x': 0.5}
        )
        btn_hello.bind(on_press=self.show_hello)
        self.add_widget(btn_hello)

        btn_bye = Button(
            text="Click để tạm biệt",
            size_hint=(None, None),
            size=(200, 80),
            pos_hint={'center_x': 0.5}
        )
        btn_bye.bind(on_press=self.show_bye)
        self.add_widget(btn_bye)

    def show_hello(self, instance):
        popup = Popup(
            title="Message",
            content=Label(text="xin chào"),
            size_hint=(0.6, 0.4)
        )
        popup.open()

    def show_bye(self, instance):
        popup = Popup(
            title="Message",
            content=Label(text="tạm biệt"),
            size_hint=(0.6, 0.4)
        )
        popup.open()


class MyApp(App):
    def build(self):
        return MainLayout()

if __name__ == "__main__":
    MyApp().run()