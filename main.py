from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.theming import ThemeManager
from mainScreen import MainScreen
# from colorsScreen import ColorsScreen

from kivy.graphics.texture import Texture
from kivy.uix.image import Image
from kivy.core.window import Window

from enunciados import enunciados
from colors import COLORS
from utils import capture



if __name__ == "__main__":

    class MyApp(MDApp):
        def build(self):
            self.theme_cls.colors = COLORS
            self.theme_cls.primary_palette = "Blue"
            self.theme_cls.accent_palette = "Blue"
            self.enunciados = enunciados
            self.selectedColor = "#FFFFFF"
            self.sm = MDScreenManager()
            self.sm.add_widget(MainScreen(name="mainScreen"))
            # self.sm.add_widget(ColorsScreen(name="colorsScreen"))
            return self.sm

        def getColorSelected(self):
            return self.selectedColor

        def changeScreen(self, nameScreen):
            self.sm.current = nameScreen

        def captureScreen(self):
            capture("screen.png")
            # return image




        # def on_check_press(self, instanceButton):
        #     pass

        # def on_row_press(self, instanceButton):
        #     print(instance_row)


    MyApp().run()
