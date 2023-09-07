from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.textfield import MDTextField
from kivy.clock import Clock
from kivy.lang.builder import Builder


Builder.load_string("""

<MyLabel>:
    text_color: "#000000"
    size_hint_y: None
    height: 40
    canvas.before:
        Color:
            rgba: 0, 0, 0, 1
        Line:
            width: 1
            rectangle: self.x, self.y, self.width, self.height


<MyTextField>:
    # mode: "line"
    mode: "rectangle"
    color_mode: 'custom'
    line_color_normal: [0,0,0,1]
    text_color_focus: [0,0,0,1]
    text_color_normal: [0,0,0,1]
    size_hint_y: None
    height: self.minimum_height
    radius: [0,0,0,0]


<EntryGrid>:
    cols: 2
    # padding: 10
    # spacing: 10
    size_hint_y: None
    height: self.minimum_height



""")



class MyLabel(MDLabel):
 pass


class MyTextField(MDTextField):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tarea = Clock.schedule_interval(self.updateHeight, 1)

    def updateHeight(self, dt):
        # mh = self.minimum_height
        if self.height != self.minimum_height:
            self.height = self.minimum_height




class EntryGrid(MDGridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__createCols()
        self.tarea = Clock.schedule_interval(self.updateGridHeight, 1)


    def updateGridHeight(self, dt):
        mh = self.minimum_height + 300
        if self.height != mh:
            self.height = mh


    def __createCols(self):
        orderItems = [
            "valor1",
            "valor2",
            "valor3",
            "Dato1",
            "Dato2",
            "mensaje"
        ]
        button:MDRectangleFlatButton
        self.add_widget(MyLabel(text="Variable",halign='center'))
        self.add_widget(MyLabel(text="Valor",halign='center'))
        for text in orderItems:
            self.add_widget(MyTextField(text=text,readonly=True))
            self.add_widget(MyTextField())

        
