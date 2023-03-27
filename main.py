import time
import webbrowser
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.clipboard import Clipboard
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
    link_message = "Create a Link First"
    def create_link(self):
        """Accesses the photo filepath, uploads it to the web,
        and inserts the link in the label widget"""
        file_path = App.get_running_app().root.ids.camera_screen.filepath  # нужно получить доступ к скрину из верхнего класса
        filesharer = FileSharer(filepath=file_path)
        self.url = filesharer.share()   # добавляю указатель чтобы в следующем методе был доступ к ссылке
        self.ids.link.text = self.url

    def copy_link(self):
        """Copy link to the clipboard available for pasting"""
        try:
            Clipboard.copy(self.url)  # copy the link in clipboard
        except:
            self.ids.link.text = self.link_message


    def open_link(self):
        """Open link with default browser"""
        try:
            webbrowser.open(self.url)
        except:
            self.ids.link.text = self.link_message
class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
