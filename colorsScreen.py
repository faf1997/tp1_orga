from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang.builder import Builder
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.gridlayout import MDGridLayout





coloresHex = [
    "#FF0000", "#00FF00", "#0000FF",  # Rojo, Verde, Azul
    "#FFFF00", "#FF00FF", "#00FFFF",  # Amarillo, Magenta, Cian
    "#FFFFFF", "#008000", "#808080",  # Marrón, Verde oscuro, Azul oscuro
    "#FF8000", "#FF0080", "#80FF00",  # Naranja, Rosa, Verde claro
    "#0080FF", "#8000FF", "#FF80FF",  # Azul claro, Púrpura, Rosa claro
    "#C0C0C0", "#808080", "#800000",  # Plata, Gris, Blanco
    "#FFC0C0", "#FF8080", "#FFFFC0",  # Rosa claro, Rojo claro, Amarillo claro
    "#C0FFC0", "#80FF80", "#C0FFFF",  # Verde claro, Cian claro, Azul claro
    "#FFC0FF", "#C080C0", "#FFCC99",  # Púrpura claro, Rosa oscuro, Rosa melocotón
    "#99CCFF", "#3399FF", "#99FF99",  # Azul melocotón, Azul claro, Verde melocotón
    "#FF99CC", "#FFCC66", "#6666FF",  # Rosa melocotón, Naranja melocotón, Azul violeta
    "#FF6600", "#00FF66", "#9933CC",  # Rojo oscuro, Verde melocotón claro, Púrpura oscuro
    "#666699", "#660066", "#996600",  # Azul grisáceo, Púrpura oscuro, Amarillo oscuro
    "#FF6666", "#99FFCC", "#339966",  # Rosa oscuro, Cian melocotón claro, Verde oscuro
    "#996633", "#669966", "#CCCC99"  # Marrón claro, Verde claro grisáceo, Amarillo grisáceo
]


Builder.load_string("""

<ColorsScreen>:
    id: colorsScreen
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            elevation: 0
            left_action_items:[["check-bold",lambda x: app.changeScreen("mainScreen")]]
            title: "Seleccione un color"
        MDBoxLayout:
            orientation: 'vertical'
            size_hint: 1, 1
            MDLabel:
                id:labelSelectedColor
                size_hint_y: None
                height: 100
                text: f"Color seleccionado: {app.getColorSelected()}"
                md_bg_color: app.selectedColor
            MDScrollView:
                GridButtonsColors:
                    size_hint_y: None
                    cols: 5


    
""")

class ColorsScreen(MDScreen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.__app = MDApp.get_running_app()

class GridButtonsColors(MDGridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__app = MDApp.get_running_app()
        self.addData(coloresHex)

    def setColorSelected(self,button):
        self.__app.selectedColor = button.text
        colorsScreen = self.__app.sm.get_screen("colorsScreen")
        labelSelectedColor = colorsScreen.ids.get("labelSelectedColor")
        labelSelectedColor.md_bg_color = self.__app.getColorSelected()
        labelSelectedColor.text = f"Color seleccionado: {button.text}"

    def addData(self, listData):
        button:MDRaisedButton
        for colorHex in listData:
            button = MDRaisedButton(text=colorHex,on_release = lambda x: self.setColorSelected(x))
            button.md_bg_color = colorHex
            button.text_color = [0,0,0,1]
            button.elevation = 0
            self.add_widget(button)




