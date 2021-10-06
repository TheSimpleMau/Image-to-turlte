#Importamos nuestra clase hecha para simplemente poner imagen y zoom que queremos
from funcs import ImageToTurtle

if __name__ == '__main__':
    imagen = ImageToTurtle('./aguacate.jpeg',2)
    imagen.image_maker()