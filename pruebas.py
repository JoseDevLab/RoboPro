from PIL import Image, ImageFilter
import numpy as np

# Supongamos que ya tienes una imagen en formato ndarray llamada "imagen_array"
# Cambia la imagen_array por tu propio arreglo
imagen_array = np.random.randint(0, 256, size=(100, 100, 3), dtype=np.uint8)

# Asignar el arreglo a un objeto Image
imagen_pillow = Image.fromarray(imagen_array)

# Aplicar un filtro (por ejemplo, filtro de desenfoque)
imagen_filtrada = imagen_pillow.filter(ImageFilter.BLUR)

# Ahora imagen_filtrada es un objeto Image con el filtro aplicado
