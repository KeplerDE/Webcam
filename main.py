from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from filesharer import FileSharer

Builder.load_file('frontend.kv')


class CameraScreen(Screen):
    def start(self):
        self.ids.camera.play = True  # root ссылается на текущий обьект экземпляра
        self.ids.camera_button.text = "Stop"
        self.ids.camera_button.texture = self.ids.camera._camera.texture


    def stop(self):
        self.ids.camera.play = False
        self.ids.camera_button.text = "Start"
        self.ids.camera.texture = None

    def capture(self):
        pass


class ImageScreen(Screen):
    pass


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
