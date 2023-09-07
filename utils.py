
from kivy.core.window import Window
from kivy.graphics.texture import Texture
from PIL import Image

def capture(filename):
    # Captura la pantalla como una textura
    try:
        texture = Texture.create(size=(Window.width, Window.height))
        texture.blit_buffer(Window.screenshot(), colorfmt='rgba')

        # Obtén los datos de la textura como bytes
        image_data = texture.get_image_data().get_data('rgba', texture.size)

        # Guarda los datos de la textura como una imagen PNG
        image = Image.frombytes('RGBA', texture.size, image_data)
        image.save(filename, format='PNG')
    except:pass
