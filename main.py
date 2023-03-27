import time

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from filesharer import FileSharer

Builder.load_file('frontend.kv')


class CameraScreen(Screen):

    def start(self):
        """Starts camera and changes button text"""
        self.ids.camera.play = True  # root ссылается на текущий обьект экземпляра
        self.ids.camera_button.text = "Stop"
        self.ids.camera_button.texture = self.ids.camera._camera.texture

    def stop(self):
        """Starts camera and changes button text"""
        self.ids.camera.play = False
        self.ids.camera_button.text = "Start"
        self.ids.camera.texture = None

    def capture(self):
        """Creates a filename with the current time and captures
        and saves a photo image under that filename"""
        current_time = time.strftime('%Y%m%d-%H%M%S')
        self.ids.camera.export_to_png('image.png')
        self.filepath = f"files/{current_time}.png"
        self.ids.camera.export_to_png(self.filepath)
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img.source = self.filepath


class ImageScreen(Screen):
    def create_link(self):
        """Accesses the photo filepath, uploads it to the web,
        and inserts the link in the label widget"""
        file_path = App.get_running_app().root.ids.camera_screen.filepath  # нужно получить доступ к скрину из верхнего класса
        filesharer = FileSharer(filepath=file_path)
        url = filesharer.share()
        self.ids.link.text = url


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
