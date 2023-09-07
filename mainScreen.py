from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.gridlayout import MDGridLayout
from kivy.clock import Clock
from enunciados import *

from entryGrid import EntryGrid



tabla = [
    ["00", "2D", "00", "11", "00"],
    ["15", "FF", "F1", "01", "13"],
    ["00", "00", "00", "00", "00"],
    ["00", "53", "69", "20", "73"],
    ["65", "20", "70", "75", "65"],
    ["64", "65", "20", "69", "6D"],
    ["61", "67", "69", "6E", "61"],
    ["72", "2C", "20", "73", "65"],
    ["20", "70", "75", "65", "64"],
    ["65", "20", "70", "72", "6F"],
    ["67", "72", "61", "6D", "61"],
    ["72", "2E", "00", "00", "00"]
]

listaHex = ['00', '2D', '00', '11', '00',
            '15', 'FF', 'F1', '01', '13',
            '00', '00', '00', '00', '00',
            '00', '53', '69', '20', '73',
            '65', '20', '70', '75', '65',
            '64', '65', '20', '69', '6D',
            '61', '67', '69', '6E', '61',
            '72', '2C', '20', '73', '65', 
            '20', '70', '75', '65', '64',
            '65', '20', '70', '72', '6F',
            '67', '72', '61', '6D', '61',
            '72', '2E', '00', '00', '00']


Builder.load_string("""

<Enunciados@MDLabel>:
    text: app.enunciados["enunciado_b"]
    text_color: [0,0,0,1]
    size_hint_y: None
    height:150

<EntryText@MDTextField>:
    mode: "rectangle"
    color_mode: 'custom'
    line_color_normal: [0,0,0,1]
    text_color_focus: [0,0,0,1]
    text_color_normal: [0,0,0,1]

<MainScreen>:
    MDBoxLayout:
        id: mainLayout
        orientation: 'vertical'
        
        MDScrollView:
            id: scrollPage
            MDBoxLayout:
                id: boxLayoutMain
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height + 300
                padding: 20
                spacing: 20
                MDBoxLayout:
                    Enunciados:
                        text: app.enunciados["enunciado_a"]
                        height:310
                MDBoxLayout:
                    size_hint_y: None
                    height:400
                    GridButtons:
                        cols: 5
                        size_hint_y: None
                        height: 400
                        radius: [0,0,0,0]
                    MDAnchorLayout:
                        anchor_y: "top"
                        anchor_x: "left"
                        padding: 10
                        spacing: 10
                        MDRectangleFlatIconButton:
                            text: "Seleccionar color"
                            icon: "palette"
                            on_release: app.changeScreen("colorsScreen")

                MDBoxLayout:
                    size_hint_y: None
                    height: 300
                    Enunciados:
                        text: app.enunciados["enunciado_b"]
                        height:150

                EntryText:
                    multiline: True
                    
                MDBoxLayout:
                    size_hint_y: None
                    height: 300
                    Enunciados:
                        text: app.enunciados["enunciado_c"]
                        height:100


                EntryText:
                    multiline: True


                MDBoxLayout:
                    size_hint_y: None
                    height: 300
                    Enunciados:
                        text: app.enunciados["enunciado_d"]
                        height:80
                
                EntryGrid:

                MDBoxLayout:
                    size_hint_y: None
                    height: 300
                    Enunciados:
                        text: app.enunciados["enunciado_e"]
                        height:80

                EntryText:
                    multiline: True

    MDFloatLayout:
        MDAnchorLayout:
            anchor_x: 'right'
            anchor_y: 'bottom'
            padding: 20
            spacing: 20
            MDIconButton:
                icon: 'content-save'
                theme_icon_color: "Custom"
                icon_color: '#FFFFFF'
                md_bg_color: '#FF6600'
                on_release: app.captureScreen()
    
""")

class MainScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.posY = 300
        self.boxLayoutMain = self.ids.get("boxLayoutMain")
        self.tarea = Clock.schedule_interval(self.updateScreenHeight, 1)
        
    def updateScreenHeight(self, dt):
        h = self.boxLayoutMain.height
        mh = self.boxLayoutMain.minimum_height + 300
        if h != mh:
            self.boxLayoutMain.height = mh + 300
        


class GridButtons(MDGridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__app = MDApp.get_running_app()
        self.addData(listaHex)

    def setColorSelected(self, button):
        button.md_bg_color = self.__app.getColorSelected()
        button.elevation = 0

    def addData(self, listData):
        button:MDRectangleFlatButton
        for numHex in listData:
            button = MDRectangleFlatButton(text=numHex,on_release = lambda x: self.setColorSelected(x))
            button.md_bg_color="#FFFFFF"
            button.text_color = [0,0,0,1]
            button.elevation = 0
            self.add_widget(button)

    